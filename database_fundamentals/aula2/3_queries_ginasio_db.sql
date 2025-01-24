select bi, nome from socios
	WHERE bi <'6000'
	
select bi, nome from socios
	WHERE nome like'R%'

select bi, nome from socios
	WHERE nome like'%a'

select bi, nome from socios
	WHERE nome like'%A' /*é case sensitive e por isso nao tem nenhum resuktado*/

select bi, nome from socios
	WHERE nome like 'R%' OR bi BETWEEN '4000' AND '5000'

select DISTINCT(sigla) from pratica

select DISTINCT sigla, bi from pratica	

select bi, sigla, salario * 1.2 as novo_salario from orienta
	WHERE salario * 1.2 > 40

select bi, sigla, salario * 1.2 as novo_salario from orienta
	WHERE novo_salario > 40 /*isto nao e possivel porque o codigo é executado da seguinte ordem, from, where e select*/


select 
	round(avg(salario),2) as mean 

from orienta

select nome, sigla from socios
join pratica on socios.bi=pratica.bi 
where sigla in ('AE', 'NT')

select nome, sigla from socios s
join pratica p on s.bi=p.bi 
where sigla in ('AE', 'NT')

select * from pratica

select * from monitores

select * from desportos

select * from orienta

select * from pratica
