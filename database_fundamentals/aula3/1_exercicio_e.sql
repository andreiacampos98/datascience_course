/*Exercicio E*/

/*1. For each ‘customer_id’ in payment’s table, show the total of
the amounts paid.*/
select * from payment
limit 10

select customer_id, sum(amount) from payment
group by customer_id
ORDER BY sum(amount) DESC

/*2. Same as before, ﬁltering the customers that spent more
than 200€*/

select customer_id, sum(amount) from payment
group by customer_id
HAVING sum(amount)>200
