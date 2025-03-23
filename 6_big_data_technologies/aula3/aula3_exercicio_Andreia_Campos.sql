/*
O que é o Delivery Center

Com seus diversos hubs operacionais espalhados pelo Brasil, o Delivery Center é 
uma plataforma integra lojistas e marketplaces, criando um ecossistema saudável 
para vendas de good (produtos) e food (comidas) no varejo brasileiro.
Atualmente temos um cadastro (catálogo + cardápio) com mais de 900 mil itens, 
milhares de pedidos e entregas são operacionalizados diariamente com uma rede de 
milhares lojistas e entregadores parceiros espalhados por todas as regiões do país.
Tudo isso gera dados e mais dados a todo momento!
Diante disso, nosso negócio está cada vez data driven, ou seja, utilizando dados 
para tomar decisões e numa visão de futuro sabemos que utilizar os dados de forma
inteligente pode ser o nosso grande diferencial no mercado.
Este é o nosso contexto e com ele lhe propomos um desafio em que você possa aplicar
seus conhecimentos técnicos objetivando resolver problemas cotidianos de uma equipe de dados.

Descrição dos datasets

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

/*Vamos considerar todas as orders que foram entregues e que estejam como terminada.
Posteriormente calculamos a média do tempo que demorou para produzir os produtos e entregar
(ORDER_METRIC_CYCLE_TIME = order_metric_production_time + order_metric_expediton_speed_time +
order_metric_transit_time).
Mostramos os valores agrupados pelo channel, hub e store.*/
/*A loja MZU PIEO SZIP com o Hub Pagode Shopping tem o maior tempo de entrega no canal Other Place.
A loja IUMPICA com o Hub Beach Shopping tem o menor tempo de entrga no canl Other Place.*/
SELECT 
    c.channel_id,
    c.channel_name,
    h.hub_id,
    h.hub_name,
    s.store_id,
    s.store_name,
    AVG(o.ORDER_METRIC_CYCLE_TIME) AS avg_transit_time
FROM ORDERS o
JOIN DELIVERIES d ON d.delivery_order_id = o.delivery_order_id
JOIN STORES s ON s.store_id = o.store_id
JOIN HUBS h ON h.hub_id = s.hub_id
JOIN CHANNELS c ON c.channel_id=o.channel_id
WHERE d.delivery_status='DELIVERED'
AND o.order_status = 'FINISHED'
GROUP BY s.store_id, s.store_name, h.hub_id, h.hub_name, c.channel_id, c.channel_name
ORDER BY avg_transit_time DESC;


/*Analisando apenas por channel, podemos concluir que o channel "Beatles Place" tem o maior tempo de entrega,
seguidamente London Place, San Place, Ahora Place, Munich Place.
E o channel "Speed place" tem o menor tempo de entrega, seguidamente o On Place, Atchin Place, Super Place, Riba Place.*/
SELECT 
    c.channel_id,
    c.channel_name,
    AVG(o.ORDER_METRIC_CYCLE_TIME) AS avg_transit_time
FROM ORDERS o
JOIN DELIVERIES d ON d.delivery_order_id = o.delivery_order_id
JOIN STORES s ON s.store_id = o.store_id
JOIN HUBS h ON h.hub_id = s.hub_id
JOIN CHANNELS c ON c.channel_id=o.channel_id
WHERE d.delivery_status='DELIVERED'
AND o.order_status = 'FINISHED'
GROUP BY c.channel_id, c.channel_name
ORDER BY avg_transit_time DESC;


/*Ao nível dos hubs, conseguimos concluir que o Hub "Hubless Shopping" tem o tempo de entrega mais elevado, 
seguidamente Elixir Shopping, Pagode Shopping, Sampa Shopping, Wolf Shopping.
E o hub "PHP Shopping" tem o menor tempo, seguidamente de Hotmilk Shopping, R Shopping, SQL Shopping, Star Shopping.*/
SELECT 
    h.hub_id,
    h.hub_name,
    AVG(o.ORDER_METRIC_CYCLE_TIME) AS avg_transit_time
FROM ORDERS o
JOIN DELIVERIES d ON d.delivery_order_id = o.delivery_order_id
JOIN STORES s ON s.store_id = o.store_id
JOIN HUBS h ON h.hub_id = s.hub_id
WHERE d.delivery_status='DELIVERED'
AND o.order_status = 'FINISHED'
GROUP BY h.hub_id, h.hub_name
ORDER BY avg_transit_time DESC;


/*Ao nível das lojas, a loja Cumoiaras tem o maior tempo de entrega, seguidamente a Liggaplus, Mzu Pieo Szip, Aeruir, Cisi Ruvavi. 
A loja de Iamur é a loja com menor tempo de entrega, seguidamente a Sirsumg, Gumoua, Zizulo, Ro Prismaus.*/
SELECT 
    s.store_id,
    s.store_name,
    AVG(o.ORDER_METRIC_CYCLE_TIME) AS avg_transit_time
FROM ORDERS o
JOIN DELIVERIES d ON d.delivery_order_id = o.delivery_order_id
JOIN STORES s ON s.store_id = o.store_id
JOIN HUBS h ON h.hub_id = s.hub_id
WHERE d.delivery_status='DELIVERED'
AND o.order_status = 'FINISHED'
GROUP BY s.store_id, s.store_name
ORDER BY avg_transit_time DESC;


/*Desempenho dos Entregadores: Quais entregadores têm o melhor 
desempenho em termos de tempo de entrega e número de entregas completadas?
Métrica: Tempo médio de entrega por entregador, número de entregas completadas.
Tabelas: deliveries, drivers.*/
/*O condutor que tem o menor tempo de entrega é o 47032 com um tempo de 14.07. 
No entanto, apenas entregou uma encomenda. Não temos uma amostra significativa para avaliar este condutor.
O condutor que tem o maior tempo de entrega é o 47016 com um tempo de 43 452.32 e só realizou uma entrega.
O condutor com maior número de entregas é o 25651 que realizou 10 709 entregs e tem um tempo médido de entrega de 63.19.
*/
SELECT 
    dr.driver_id,
    AVG(o.ORDER_METRIC_CYCLE_TIME) AS avg_delivery_time,
    COUNT(d.delivery_order_id) AS total_deliveries
FROM ORDERS o
JOIN DELIVERIES d ON d.delivery_order_id = o.delivery_order_id
JOIN DRIVERS dr ON dr.driver_id = d.driver_id
WHERE d.delivery_status = 'DELIVERED'
AND o.order_status = 'FINISHED'
GROUP BY dr.driver_id
HAVING COUNT(d.delivery_order_id) > 0 
ORDER BY total_deliveries ASC, avg_delivery_time ASC;


/*Experiência do Cliente*/

/*3. Nível de Satisfação do Cliente: Como podemos correlacionar o tempo de entrega com a satisfação do cliente?
Métrica: Tempo de entrega versus feedback do cliente (se disponível).
Tabelas: deliveries, orders*/



/*Não temos informação acerca do feedback do cliente. 
Necesitariamos de criar métricas para avaliar a satisfação do cliente. Poderiamos por exemplo, 
tentar perceber se o cliente voltou a comprar e se o tempo de entrega por cliente influencia no numero de compras.

Portanto, para cada store vou ver o tempo de entrega das orders que não foram canceladas e o numero de orders canceladas. De modo a tentar perceber se existe uma correlação.
Não faz sentido analisar o tempo de entrega para as orders que foram canceladas, uma vez que, nem sempre temos esta informação.*/

/*Podemos concluir que há tempos de entregas muitos elevados para algumas lojas. Também conseguimos perceber que há bastantes encomendas canceladas. 
No entanto, não podemos dizer com grande certeza que pelo tempo de espera ser grande, os clientes cancelam as suas encomendas. 
Precisariamos de perceber quanto tempo depois da encomenda ser realizada o cleinte cancelou a encomenda.*/
SELECT 
    o.store_id,
    AVG(CASE WHEN d.delivery_status <> 'CANCELLED' THEN o.ORDER_METRIC_CYCLE_TIME END) AS avg_delivery_time,
    SUM(CASE WHEN d.delivery_status = 'CANCELLED' THEN 1 ELSE 0 END) AS total_cancelled_orders,
    COUNT(d.delivery_order_id) AS total_orders,
    (total_cancelled_orders/total_orders) AS perc_cancelled
FROM ORDERS o
JOIN DELIVERIES d ON d.delivery_order_id = o.delivery_order_id
GROUP BY o.store_id
ORDER BY avg_delivery_time DESC;


/*4. Pedidos Cancelados: Qual é a taxa de cancelamento de pedidos e quais 
são os motivos mais comuns para cancelamentos?
Métrica: Número de pedidos cancelados dividido pelo número total de pedidos, 
motivos de cancelamento.
Tabelas: orders*/
/*A perentagem de cancelamento é de 4.6%. De momento, não conseguimos perceber o motivo do cancelamento. Temos de obter mais kpis.*/
SELECT 
    SUM(CASE WHEN o.order_status = 'CANCELED' THEN 1 ELSE 0 END) AS total_cancelled_orders,
    COUNT(o.order_id) AS total_orders,
    (total_cancelled_orders/total_orders)*100 AS perc_cancelled
FROM ORDERS o




/*Desempenho Financeiro*/

/*6.Receita por Canal de Venda: Qual é a receita gerada por cada canal de venda?
Métrica: Soma dos valores dos pedidos por canal de venda.
Tabelas: payments, channels, orders.*/
/*O canal que tem o maior valor de vendas é o Food Place.*/
SELECT 
    c.channel_id,
    c.channel_name,
    SUM(p.PAYMENT_AMOUNT) AS Soma_pedidos
FROM PAYMENTS p
JOIN ORDERS o ON o.payment_order_id=p.payment_order_id 
JOIN CHANNELS c ON c.channel_id= o.channel_id
GROUP BY c.channel_id, c.channel_name
ORDER BY Soma_pedidos DESC;



/*7.Custo de Entrega: Qual é o custo médio de entrega por pedido, loja ou hub?
Métrica: Custo total de entrega dividido pelo número de entregas.
Tabelas: deliveries, orders, hubs.*/
/*A loja Mar tem um custo médio de entrega mais eleveado, cerca de 65.*/
SELECT
    h.hub_id,
    h.hub_name,
    s.store_id,
    s.store_name,
    AVG(o.order_delivery_fee) AS custo_medio_delivery
FROM DELIVERIES d
JOIN ORDERS o ON o.delivery_order_id = d.delivery_order_id
JOIN STORES s ON s.store_id = o.store_id
JOIN HUBS h ON h.hub_id = s.hub_id
WHERE d.delivery_status = 'DELIVERED'
GROUP BY h.hub_id ,h.hub_name, s.store_id, s.store_name
ORDER BY custo_medio_delivery DESC;



/*Otimização de Vendas*/

/*8. Produtos Mais Vendidos: Quais são os produtos mais vendidos por categoria (good e food)?
Métrica: Número de vendas por produto.
Tabelas: orders, stores.*/
/*Temos mais vendas de produtos do segmento food*/

SELECT
    s.store_segment,
    count(o.order_id)
FROM ORDERS o 
JOIN STORES s ON s.store_id = o.store_id 
GROUP BY s.store_segment;


/*9. Desempenho das Lojas: Quais lojas têm o maior número de vendas e receita?
Métrica: Número de vendas e receita por loja.
Tabelas: stores, orders, payments.*/
/*A loja que tem  mais vendas em valor é a 676. No entanto a loja 53 tem mais vendas em quantidade.*/

SELECT
    s.store_id,
    s.store_name,
    count(o.order_id) AS nb_vendas,
    sum(p.payment_amount) valor_vendas
FROM ORDERS o 
JOIN STORES s ON s.store_id = o.store_id 
JOIN PAYMENTS p ON p.payment_order_id=o.payment_order_id
GROUP BY s.store_id, s.store_name
ORDER BY nb_vendas DESC;
