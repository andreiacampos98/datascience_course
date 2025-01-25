/*Conhecer como a tabela é constituida*/
select * from actor
limit 10;

/*Number of records of the actor's table*/
select count(*) from actor;

/*How many actors have the same first name,
sorted by first name but descending*/
select first_name, count(first_name) from actor
group by first_name 
ORDER BY first_name DESC;


/*Create an alias for the count column named howmany*/
select first_name, count(first_name) as howmany from actor
group by first_name 
ORDER BY first_name DESC;

/*Reuse the previous query and sort it by ‘howmany’ in
descending order and by ‘ﬁrst_name’ ascending.*/
SELECT first_name, COUNT(*) howmany FROM actor
GROUP BY first_name
ORDER BY howmany DESC, first_name ASC;


/*Tests*/
select first_name, count(first_name) as howmany from actor
group by first_name 
ORDER BY 1 DESC; /*1 significa a primeira coluna que eu tenho no select*/

select last_name, count(last_name) as howmany from actor
group by last_name 
ORDER BY 1 DESC;