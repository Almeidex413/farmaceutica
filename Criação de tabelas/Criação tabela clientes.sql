WITH pedidos_com_lag AS (
    SELECT
        p.id_cliente,
        p.data_pedido,
        p.valor_total,
        LAG(p.data_pedido) OVER (PARTITION BY p.id_cliente ORDER BY p.data_pedido) AS data_ultimo_pedido,
        COUNT(*) OVER (PARTITION BY p.id_cliente) AS total_pedidos,
        SUM(p.valor_total) OVER (PARTITION BY p.id_cliente) AS soma_valores
    FROM pedidos p
),
pedidos_mais_recentes AS (
    SELECT *,
           CURRENT_DATE - data_ultimo_pedido AS dias_desde_ultimo_pedido,
           soma_valores::DECIMAL / total_pedidos AS ticket_medio
    FROM pedidos_com_lag
),
ultimos_por_cliente AS (
    SELECT DISTINCT ON (id_cliente)
        id_cliente,
        dias_desde_ultimo_pedido,
        total_pedidos,
        ticket_medio
    FROM pedidos_mais_recentes
    ORDER BY id_cliente, data_pedido DESC
)

SELECT 
    uc.id_cliente,
    c.nome,
	uc.total_pedidos,
	uc.dias_desde_ultimo_pedido,
    uc.ticket_medio
FROM ultimos_por_cliente uc
JOIN clientes c ON c.id_cliente = uc.id_cliente
ORDER BY dias_desde_ultimo_pedido DESC;
