CREATE TABLE espetador(
	email character varying PRIMARY KEY,
	nome character varying NOT NULL,
	cidade character varying NOT NULL
);

CREATE TABLE artista (
	nif character varying PRIMARY KEY,
	nome character varying NOT NULL,
	d_nasc date NOT NULL,
	tipo character varying NOT NULL
);

CREATE TABLE espetaculo (
	id character varying PRIMARY KEY,
	titulo character varying NOT NULL,
	dia date NOT NULL,
	hora int NOT NULL,
	preco int NOT NULL CHECK (preco >= 0),
	categoria character varying NOT NULL,
	artista character varying REFERENCES artista(nif)
);

CREATE TABLE bilhete (
	id character varying REFERENCES espetaculo(id),
	lugar character varying,
	email  character varying REFERENCES espetador(email),
	custo int NOT NULL CHECK (custo >= 0),
	PRIMARY KEY( id, lugar)
);

