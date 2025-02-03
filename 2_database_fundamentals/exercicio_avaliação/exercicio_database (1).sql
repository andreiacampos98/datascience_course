CREATE TABLE "espetador" (
  "email" varchar PRIMARY KEY,
  "nome" varchar NOT NULL,
  "cidade" varchar NOT NULL
);

CREATE TABLE "bilhete" (
  "id" varchar,
  "lugar" varchar,
  "email" varchar NOT NULL,
  "custo" int NOT NULL,
  PRIMARY KEY ("id", "lugar")
);

CREATE TABLE "espetaculo" (
  "id" varchar PRIMARY KEY,
  "titulo" varchar NOT NULL,
  "dia" date NOT NULL,
  "hora" int NOT NULL,
  "preco" int NOT NULL,
  "categoria" varchar NOT NULL,
  "artista" varchar NOT NULL
);

CREATE TABLE "artista" (
  "nif" varchar PRIMARY KEY,
  "nome" varchar NOT NULL,
  "d_nasc" date NOT NULL,
  "tipo" varchar NOT NULL
);

ALTER TABLE "bilhete" ADD FOREIGN KEY ("email") REFERENCES "espetador" ("email");

ALTER TABLE "bilhete" ADD FOREIGN KEY ("id") REFERENCES "espetaculo" ("id");

ALTER TABLE "espetaculo" ADD FOREIGN KEY ("artista") REFERENCES "artista" ("nif");
