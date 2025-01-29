/*Exercício H – BETWEEN, IN, IS NULL*/


/*1. Select customer information where the customer_id is
bigger than 9 and lower than 15.*/
select * from customer
where customer_id between 9 and 15

/*2. Select customer information where the ﬁrst name is Lisa or
Marion.*/
select * from customer
where first_name in ('Lisa', 'Marion')


select * from staff
/*3. Select staff information where picture is NULL.*/
select * from staff
where picture is null

/*4. Select staff information where picture is not NULL.*/
select * from staff
where picture is not null