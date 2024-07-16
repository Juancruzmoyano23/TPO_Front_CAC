CREATE TABLE recetas (
    receta_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    ingredient TEXT NOT NULL,
    rating DECIMAL(2, 1),
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    year INT
);

create table if not exists characters (
	character_id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	city VARCHAR(50),
	year INT
);

create table if not exists types (
	type_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);


create table if not exists receta_types (
	receta_id INTEGER,
	type_id INTEGER,
	PRIMARY KEY (receta_id, type_id),

	FOREIGN KEY (receta_id) REFERENCES recetas(receta_id),
	FOREIGN KEY (type_id) REFERENCES types(type_id)
);

create table if not exists receta_characters (
	receta_id INTEGER,
	character_id INTEGER,
	PRIMARY KEY (receta_id, character_id),

	FOREIGN KEY (receta_id) REFERENCES recetas(receta_id),
	FOREIGN KEY (character_id) REFERENCES characters(character_id)
);