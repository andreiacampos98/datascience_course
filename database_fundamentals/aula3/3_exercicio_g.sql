/*Exercício G – INTERSECT & EXCEPT*/

/*1. List the common ﬁrst names of both actors and customers
in the same column.*/
select first_name from actor INTERSECT SELECT first_name FROM customer


/*2. List the ﬁrst names of actors that don’t exist on customer
table.*/
select first_name from actor EXCEPT SELECT first_name FROM customer
