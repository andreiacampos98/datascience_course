CREATE TABLE espetador(
	email character varying PRIMARY KEY,
	nome character varying,
	cidade character varying
);

CREATE TABLE artista (
	nif character varying PRIMARY KEY,
	nome character varying,
	d_nasc date,
	tipo character varying
);

CREATE TABLE espetaculo (
	id character varying PRIMARY KEY,
	titulo character varying,
	dia date,
	hora int NOT NULL,
	preco int NOT NULL,
	categoria character varying,
	artista character varying REFERENCES artista(nif)
);

CREATE TABLE bilhete (
	id character varying REFERENCES espetaculo(id),
	lugar character varying,
	email  character varying REFERENCES espetador(email),
	custo int NOT NULL,
	PRIMARY KEY( id, lugar)
);

