/*Conhecer como a tabela é constituida*/
select * from actor
limit 10;

/*Number of records of the actor's table*/
select count(*) from actor

/*How many actors have the same first name,
sorted by first name but descending*/
select first_name, count(first_name) from actor
group by first_name 
ORDER BY first_name DESC;


/*Create an alias for the count column named howmany*/
select first_name, count(first_name) as howmany from actor
group by first_name 
ORDER BY first_name DESC;
