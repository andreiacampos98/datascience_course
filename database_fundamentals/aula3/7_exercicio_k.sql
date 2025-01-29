/*Exercícios – K*/

/*1. For each customer ﬁrst_name in lower case, list the year of
his last_update.*/
SELECT first_name
	, LOWER(first_name)
	, last_update
	, EXTRACT(YEAR FROM last_update)
from customer;

SELECT
  c.address_id,
  a.address,
  c.first_name,
  c.last_update AS customer_last_update,
  a.last_update AS address_last_update,
  EXTRACT(YEAR FROM c.last_update) AS customer_last_update_year,
  EXTRACT(YEAR FROM a.last_update) AS address_last_update_year
FROM customer c
INNER JOIN address a
  ON c.address_id = a.address_id;


/*2. For each customer ﬁrst_name, list: store_id, active,
store_id+active (eg.: “1+2”), and store_idactive (eg.: “12”).*/

select first_name
	, store_id
	, active
	, CAST(store_id AS text) || CAST(active AS text) store_active
	, store_id || '+' || active store_plus_active
from customer;