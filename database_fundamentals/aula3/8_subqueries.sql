/*Subqueries*/

/*Usando WHERE*/
/*Obter o valor pago pelos clientes acima da média do valor pago*/
select * from payment
where amount >= (select round(avg(amount),2)as valor_medio from payment )
ORDER BY amount asc

/*Usando a clausula FROM*/
/*Obter a média do total pago por cada cliente*/
select round(avg(total_pago),2) as media_total 
	from (select customer_id, sum(amount) as total_pago from payment
			group by customer_id
			order by sum(amount))
	

/*Usando a clausula select*/
/*Adicionar a coluna da média na tabela */
select *, (select round(avg(amount),2)as valor_medio from payment ) from payment



/*Exercicio*/
select * from film
limit 10

select * from category
limit 10

SELECT c.name, COUNT(DISTINCT fc.film_id) AS total_films
FROM category c
INNER JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name
HAVING COUNT(DISTINCT fc.film_id) > 65
ORDER BY total_films DESC;


SELECT
    (SELECT name FROM category a WHERE a.category_id = b.category_id) AS name,
    COUNT(DISTINCT film_id)
FROM film_category b
GROUP BY b.category_id
HAVING COUNT(DISTINCT film_id) > 65
ORDER BY 2 DESC;

SELECT name,
	(SELECT COUNT(DISTINCT film_id)
	FROM film_category fc
	WHERE fc.category_id =c.category_id) AS total_filmes
FROM category c
WHERE c.category_id IN
	( SELECT category_id
	FROM film_category
	GROUP BY category_id
	HAVING COUNT(DISTINCT film_id) > 65
)
ORDER BY total_filmes DESC;



/*Clausula with não é muito utilizada. É semelhante à subquery*/

/*Exercicios - clausula with*/
/*1*/
WITH actor_name AS (
SELECT first_name
, COUNT(*) as num
FROM actor
GROUP BY first_name
)
SELECT c.first_name, ac.num
FROM customer c
LEFT JOIN actor_name ac ON c.first_name = ac.first_name;

/*2*/
WITH c_total AS (
	SELECT customer_id, SUM(amount) AS total
	FROM payment
	GROUP BY customer_id
	HAVING SUM(amount) >= 150
	),
	c_email AS (
	SELECT customer_id, email
	FROM customer
	WHERE SUBSTRING(email, 2, 1) = 't'
)
SELECT f.title
FROM film f
INNER JOIN inventory i on f.film_id = i.film_id
INNER JOIN rental r on i.inventory_id = r.inventory_id
INNER JOIN c_total ct on r.customer_id = ct.customer_id
INNER JOIN c_email ce on r.customer_id = ce.customer_id;

