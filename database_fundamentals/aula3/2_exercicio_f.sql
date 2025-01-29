/*Exercicio F*/


select * from customer
limit 10

select * from actor
limit 10

/*1. Count the number of customers.*/
select count(customer_id) from customer


/*2. Count the number of actors.*/
select count(*) from actor

/*3. List the distinct ﬁrst names of actors and customers in the
same column.*/
select first_name from customer UNION SELECT first_name FROM actor

/*4. List the ﬁrst names of actors and customers in the same
column.*/

select first_name from customer UNION ALL SELECT first_name FROM actor
