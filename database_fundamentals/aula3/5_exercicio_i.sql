/*Exercício I – JOIN*/

/*1. For each customer in customer table, show ﬁrst and
last names and the corresponding address, from
address table.*/

select * from customer
LIMIT 10

select * from address
LIMIT 10

SELECT c.first_name, c.last_name, a.address FROM customer c
JOIN address a on c.address_id=a.address_id

/*Outra forma de fazer join*/
SELECT c.first_name, c.last_name, a.address FROM customer c, address a
WHERE c.address_id=a.address_id


/*2. Identify the existing ‘address_id’s on table address
which have no corresponding customer. (without using
JOIN)*/
select address_id from address EXCEPT select address_id from customer

select address_id from address 
Where address_id not in (select address_id from customer)

/*3. List ‘address_id’, ‘address’, ‘ﬁrst_name’ for customers
with ‘address_id’<=7, sorted by ‘address_id’.*/
SELECT c.first_name, a.address_id, a.address FROM customer c
JOIN address a on c.address_id=a.address_id
WHERE a.address_id <=7
ORDER BY a.address_id

/*4. List ‘address_id’, ‘address’, ‘ﬁrst_name’ for
customers with ‘address_id’<=7, sorted by
‘address_id’, using LEFT JOIN.
Also, try to adapt the same query now using RIGHT
JOIN.*/
SELECT c.first_name, a.address_id, a.address FROM customer c
LEFT JOIN address a on c.address_id=a.address_id
WHERE a.address_id <=7
ORDER BY a.address_id

SELECT c.first_name, a.address_id, a.address FROM customer c
RIGHT JOIN address a on c.address_id=a.address_id
WHERE a.address_id <=7
ORDER BY a.address_id


/*5. For each customer last_name, 
list the film titles he rented and the corresponding 
language name and rental rate.
Records should be sorted starting on the most expensive ones. 
Only show the films with a rental rate equal or bigger than 2.99€. */
select c.last_name, f.title, l.name, f.rental_rate 
from customer c
JOIN rental r ON r.customer_id=c.customer_id
JOIN inventory i ON i.inventory_id=r.inventory_id
JOIN film f ON f.film_id=i.film_id
JOIN language l ON f.language_id=l.language_id
WHERE f.rental_rate >= 2.99
order by f.rental_rate DESC

