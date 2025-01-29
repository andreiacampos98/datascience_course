/*Exercício J – CASE*/


/*1. For each record having ‘address2’ as NULL, on address
table, present:
- address2
- address3, as result of using COALESCE to replace
NULL values by ‘Unknown’ on address2
- address
- last char, as result of (Using case) is ‘e’, return ‘E’;
- if address’ last character is ‘d’, return ‘D’;
- if address’ last character is anything else, return ‘X’*/

SELECT 	
	address2,
	COALESCE (address2, 'UNKNOWN') as address3,
	address,
	CASE
		WHEN address LIKE '%e' THEN 'E'
		WHEN address LIKE '%d' THEN 'D'
		ELSE 'X'
	END as last_char
from address
WHERE address2 is null


select * from address
limit 10


/*Exemplos de queries com case Where*/
SELECT
  amount,
  CASE
    WHEN amount <= 5.99 THEN 'baixo'
    WHEN amount BETWEEN 6.99 AND 10.99 THEN 'medio'
    ELSE 'alto'
  END AS values_group
FROM public.payment
	order by amount desc;


SELECT
  sum (amount),
   CASE
    WHEN amount <= 5.99 THEN 'baixo'
    WHEN amount BETWEEN 6.99 AND 10.99 THEN 'medio'
    ELSE 'alto'
  END AS values_group
FROM public.payment
	group by values_group;



ALTER TABLE public.payment
ADD COLUMN values_group VARCHAR(10);

UPDATE public.payment
SET values_group =
  CASE
    WHEN amount <= 5.99 THEN 'baixo'
    WHEN amount BETWEEN 6.99 AND 10.99 THEN 'medio'
    ELSE 'alto'
  END;


ALTER TABLE public.payment
DROP COLUMN values_group;


/*Create a view*/
CREATE OR REPLACE VIEW payment_with_values_group AS
SELECT
  amount,
  CASE
    WHEN amount <= 5.99 THEN 'baixo'
    WHEN amount BETWEEN 6.99 AND 10.99 THEN 'medio'
    ELSE 'alto'
  END AS values_group
FROM public.payment;


