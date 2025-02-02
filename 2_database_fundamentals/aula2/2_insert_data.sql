INSERT INTO socios("bi", "nome")
values
	('6078','Ana'),
	('5819', 'Rui'),
	('4526', 'Nuno'),
	('3955', 'Rita'),
	('9999', 'Jose')


INSERT INTO monitores("bi", "nome")
values
	('9876','Luis'),
	('1234', 'Joana')


INSERT INTO desportos (sigla, designacao)
VALUES
    ('KB', 'Kickbox'),
    ('NT', 'Natação'),
    ('AE', 'Aerobica');

INSERT INTO public.orienta (bi, sigla, salario)
VALUES
    ('1234', 'KB', '40'),
    ('1234', 'NT','30'),
	('9876', 'NT','30'),
    ('9876', 'AE','35');

INSERT INTO public.pratica (bi, sigla, quota)
VALUES
    ('6078', 'AE', '25'),
    ('5819', 'KB','30'),
	('4526', 'KB','30'),
    ('4526', 'NT','20'),
	('3955', 'NT', '30'),
	('3955', 'NT', '20'),
    ('3955', 'AE','25'),
	('9876', 'KB','0'); /*ERRO Porque nao existe o socio com o BI 9876*/
	
select * from monitores
select * from socios
select * from desportos
select * from orienta
select * from pratica
