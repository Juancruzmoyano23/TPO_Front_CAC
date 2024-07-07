select * FROM countries;
select name, city from characters;

select * from recetas
	
select * from recetas where rating > 8;

select * from recetas where rating < 8;

select * from recetas where rating != 8.5;

select * from recetas where rating = 6.5;

select * from recetas where name like '%cos%';


select name, rating,
	case 
		when rating >= 9 then 'Excelente!'
		when rating >= 7.5 then 'Muy Buena'
		else 'Pobre'
	end as rating_category

	from recetas;


select * from recetas;

select distinct description from recetas;

select name from recetas
union
select name from characters;

-- aggregations
-- COUNT, SUM, AVG, MAX, MIN

select COUNT(*) as total_recetas from recetas;