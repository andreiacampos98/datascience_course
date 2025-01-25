/*Conhecer como a tabela é constituida*/
select * from actor
limit 10;

/*Select all actor’s data sorted by last_name.*/
SELECT * FROM actor
ORDER BY last_name ASC;

/*Select all actor’s data sorted by last name but by
descending order.*/
SELECT * FROM actor
ORDER BY last_name DESC;

/*Select ﬁrst and last names, sorted by last name by
ascending order, from actors whose ﬁrst name starts
with a ‘B’.*/
SELECT first_name, last_name FROM actor
WHERE first_name LIKE 'B%'
ORDER BY last_name ASC;