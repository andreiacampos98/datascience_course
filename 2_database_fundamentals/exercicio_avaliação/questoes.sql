SELECT * FROM public.artista;
SELECT * FROM public.espetaculo;
SELECT * FROM public.espetador;
SELECT * FROM public.bilhete;

/*P1) Quais os títulos, dias e horas dos espetáculos registados na BD?*/
SELECT titulo, dia, hora FROM public.espetaculo;


/*P2) Quais as categorias e os títulos dos espetáculos registados na BD?*/
SELECT titulo, categoria FROM public.espetaculo;

/*P3) Quais os nomes e datas de nascimento dos cantores registados? Ordene o resultado por data de nascimento crescente.*/
SELECT nome, d_nasc FROM public.artista
WHERE tipo='cantor'
ORDER BY d_nasc ASC;

/*P4) Quais os emails e os nomes dos espectadores do Porto? Ordene o resultado por email.*/
SELECT email, nome FROM public.espetador
WHERE cidade='Porto'
ORDER BY email;

/*P5) Relativamente a cada artista, liste o seu nome e o dia e o título dos espetáculos em 
que foi o artista principal. Ordene o
resultado por nome crescente e por data decrescente*/
SELECT a.nome, e.dia, e.titulo FROM public.artista a
JOIN public.espetaculo e ON e.artista=a.nif
ORDER BY a.nome ASC, e.dia DESC;

/*P6) Relativamente a cada espetador, liste o seu nome e o lugar e o custo dos bilhetes que adquiriu.
Ordene o resultado por nome crescente e por custo decrescente.*/
SELECT e.nome, b.lugar, b.custo  FROM public.espetador e
JOIN public.bilhete b ON b.email=e.email
ORDER BY e.nome ASC, b.custo DESC;

/*P7) Indique, sem repetições, o nome dos espectadores que compraram bilhetes para os espetáculos 
e o nome do artista.*/
SELECT distinct e.nome, es.titulo, a.nome  FROM public.espetador e
JOIN public.bilhete b ON b.email=e.email
JOIN public.espetaculo es ON es.id=b.id 
JOIN public.artista a ON a.nif=es.artista;

/*P8) Liste os nomes de todas as pessoas, espectadores e artistas, desde que os espectadores sejam do Porto e os
artistas sejam atores.*/
SELECT nome FROM public.espetador
WHERE cidade='Porto'
UNION 
SELECT nome FROM public.artista
WHERE tipo='ator';


/*P9) Liste os nomes de todas as pessoas que não são do Porto e que não têm nomes de artistas.*/
SELECT nome 
FROM public.espetador
WHERE cidade!='Porto'
EXCEPT 
SELECT nome 
FROM public.artista;

/*P10) Qual a receita total por espetáculo? Indique o id, o título e o valor total dos bilhetes.*/
SELECT es.id, es.titulo, sum(b.custo) as valor_total FROM public.espetaculo es
JOIN public.bilhete b ON es.id=b.id 
GROUP BY es.id, es.titulo
ORDER BY es.id;

/*P11) Qual a receita total por categoria de espetáculo? 
Indique a categoria e o valor total dos bilhetes.*/
SELECT es.categoria, sum(b.custo) as valor_total FROM public.espetaculo es
JOIN public.bilhete b ON es.id=b.id 
GROUP BY es.categoria;

/*P12) Quem (email) foi a todos os espetáculos do TONy Carreira?*/
SELECT b.email FROM public.bilhete b
JOIN public.espetaculo es ON es.id=b.id
JOIN public.artista a ON a.nif=es.artista
WHERE a.nome='Tony Carreira'
GROUP BY b.email
HAVING COUNT(DISTINCT es.id) = (
    SELECT COUNT(DISTINCT es2.id) 
    FROM public.espetaculo es2
    JOIN public.artista a2 ON a2.nif=es2.artista
    WHERE a2.nome='Tony Carreira'
);
