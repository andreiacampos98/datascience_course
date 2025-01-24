/*Conhecer como a tabela é constituida*/
select * from actor
limit 10;

/*Select only the first name*/
select first_name from actor;

/*Select only the first and last name*/
select first_name, last_name from actor;

/*Select only distint first name*/
select DISTINCT first_name from actor;

/*Select only distint first names that are different from NICK*/
select DISTINCT first_name from actor
WHERE first_name!='Nick';