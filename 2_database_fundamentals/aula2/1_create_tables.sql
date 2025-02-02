CREATE TABLE socios(
	bi character varying (20) PRIMARY KEY,
	nome character varying (100) NOT NULL
);

CREATE TABLE monitores(
	bi character varying (20) PRIMARY KEY,
	nome character varying (100) NOT NULL
);

CREATE TABLE desportos(
	sigla character varying (20) PRIMARY KEY,
	designacao character varying (50) NOT NULL
);

CREATE TABLE pratica(
	bi character varying (20) REFERENCES socios(bi), /*como adicionar uma foreign key*/
	sigla character varying (20) REFERENCES desportos(sigla),
	quota integer NOT NULL
);

CREATE TABLE orienta(
	bi character varying (20) REFERENCES monitores(bi), /*como adicionar uma foreign key*/
	sigla character varying (20) REFERENCES desportos(sigla),
	salario integer NOT NULL
);