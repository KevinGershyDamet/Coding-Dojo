/*
select *
from users
where first_name not like "K%";

select first_name
from users
order by first_name asc
limit 3 /* establece el número máximo de salidas 
offset 2; /* indica cuánto se desplaza desde la primera salida 
*/

/*insert into users (first_name, last_name, birthday)
values ('Kev','G-D',02/08/1995);*/
select * from users;

UPDATE users
SET first_name = 'Erasmo', last_name = 'Wong'
WHERE id = 9;

select * from users;

delete from users where id = 8;

select upper(concat('Mr.', ' ', first_name, ' ', last_name)) as full_name from users;


use lead_gen_business;

 
 