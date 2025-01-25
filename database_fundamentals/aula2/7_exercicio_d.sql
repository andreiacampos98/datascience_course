/*Select the first 6 rows of actor's table*/
select * from actor
limit 6;


/*Select the 4 rows (from 3rd until 6th) from actor's table*/
select * from actor
	OFFSET 2 ROWS;
	LIMIT 4 


/*Same as before but using FETCH*/
SELECT *
FROM actor
	OFFSET 2 ROWS
	FETCH FIRST 4 ROWS ONLY;


/*Same as before but with two groups*/
(SELECT *
FROM actor
	OFFSET 2 ROWS
	FETCH FIRST 4 ROWS ONLY)
UNION (SELECT *
FROM actor
	OFFSET 10 ROWS
	FETCH FIRST 4 ROWS ONLY);