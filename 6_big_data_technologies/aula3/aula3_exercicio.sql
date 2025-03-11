/*Tempo medio de Entrega: Qual é o tempo médio de entrega por hub, loja ou canal de venda?
Métrica: Tempo total de entrega dividido pelo número de entregas*/

SELECT 
    c.CHANNEL_ID, 
    c.CHANNEL_NAME, 
    AVG(o.ORDER_METRIC_TRANSIT_TIME) AS avg_transit_time
FROM orders o
JOIN CHANNELS c ON c.CHANNEL_ID = o.CHANNEL_ID
GROUP BY c.CHANNEL_ID, c.CHANNEL_NAME;


SELECT 
    s.STORE_ID, 
    s.STORE_NAME,
    h.HUB_ID, 
    h.HUB_NAME,
    AVG(o.ORDER_METRIC_TRANSIT_TIME) AS avg_transit_time
FROM orders o
JOIN STORES s ON s.STORE_ID = o.STORE_ID
JOIN HUBS h ON s.hub_id = h.hub_id
GROUP BY s.STORE_ID,s.STORE_NAME, h.HUB_ID, h.HUB_NAME
ORDER BY s.STORE_ID, h.HUB_ID DESC;

