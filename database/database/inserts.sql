INSERT INTO countries (name, city, year)
VALUES
('Argentina', 'Tucuman', 1970),
('Mexico', 'Guadalajara', 1987),
('Japon', 'Tokio', 2001);


INSERT INTO characters (name, city, year)
VALUES
('Argentina', 'Tucuman', 1970),
('Mexico', 'Guadalajara', 1987);

insert into types (name)
values
('Pastas'),
('Carnes'),
('Pescados');

insert into recetas (name, description, ingredient, rating, country_id) 
values 
('Tacos', 'lorem 1', 'carne verdura', 8.5, 1),
('Sushi', 'lorem 2', 'arroz salmon', 6.5, 2);

insert into receta_types (receta_id, type_id)
values
(1, 1),
(1, 3),
(2, 3);


insert into receta_characters (receta_id, character_id)
values
(1, 1),
(1, 2),
(2, 1);