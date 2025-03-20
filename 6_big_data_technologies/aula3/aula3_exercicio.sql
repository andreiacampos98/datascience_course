/*Descrição dos datasets

channels: Este dataset possui informações sobre os canais de venda (marketplaces)
onde são vendidos os good e food de nossos lojistas.
deliveries: Este dataset possui informações sobre as entregas realizadas por 
nossos entregadores parceiros.
drivers: Este dataset possui informações sobre os entregadores parceiros. 
Eles ficam em nossos hubs e toda vez que um pedido é processado, 
são eles fazem as entregas na casa dos consumidores.
hubs: Este dataset possui informações sobre os hubs do Delivery Center. 
Entenda que os Hubs são os centros de distribuição dos pedidos e é dali que 
saem as entregas.
orders: Este dataset possui informações sobre as vendas processadas através da 
plataforma do Delivery Center.
payments: Este dataset possui informações sobre os pagamentos realizados ao 
Delivery Center.
stores: Este dataset possui informações sobre os lojistas. Eles utilizam a 
Plataforma do Delivery Center para vender seus itens (good e/ou food) nos marketplaces.*/

/*Eficiência Operacional*/

/*Tempo Médio de Entrega: Qual é o tempo médio de entrega por hub, 
loja ou canal de venda?
Métrica: Tempo total de entrega dividido pelo número de entregas.
Tabelas: deliveries, hubs, orders.*/
SELECT 
    c.CHANNEL_ID, 
    c.CHANNEL_NAME, 
    AVG(o.ORDER_METRIC_TRANSIT_TIME) AS avg_transit_time
FROM orders o
JOIN CHANNELS c ON c.CHANNEL_ID = o.CHANNEL_ID
GROUP BY c.CHANNEL_ID, c.CHANNEL_NAME;

/*Desempenho dos Entregadores: Quais entregadores têm o melhor 
desempenho em termos de tempo de entrega e número de entregas completadas?
Métrica: Tempo médio de entrega por entregador, número de entregas completadas.
Tabelas: deliveries, drivers.*/
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


/*Experiência do Cliente*/

/*3. Nível de Satisfação do Cliente: Como podemos correlacionar o tempo de entrega com a satisfação do cliente?
Métrica: Tempo de entrega versus feedback do cliente (se disponível).
Tabelas: deliveries, orders*/



/*4. Pedidos Cancelados: Qual é a taxa de cancelamento de pedidos e quais 
são os motivos mais comuns para cancelamentos?
Métrica: Número de pedidos cancelados dividido pelo número total de pedidos, 
motivos de cancelamento.
Tabelas: orders*/


/*Desempenho Financeiro*/

/*6.Receita por Canal de Venda: Qual é a receita gerada por cada canal de venda?
Métrica: Soma dos valores dos pedidos por canal de venda.
Tabelas: payments, channels, orders.*/


/*7.Custo de Entrega: Qual é o custo médio de entrega por pedido, loja ou hub?
Métrica: Custo total de entrega dividido pelo número de entregas.
Tabelas: deliveries, orders, hubs.*/

/*Otimização de Vendas*/

/*8. Produtos Mais Vendidos: Quais são os produtos mais vendidos por categoria (good e food)?
Métrica: Número de vendas por produto.
Tabelas: orders, stores.*/

/*9. Desempenho das Lojas: Quais lojas têm o maior número de vendas e receita?
Métrica: Número de vendas e receita por loja.
Tabelas: stores, orders, payments.*/