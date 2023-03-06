USE twitter;

select first_name as Nombre, last_name as Apellido
from users;

insert into users (first_name, last_name)
values ('Kevin', 'Gershy-Damet');

select * from users;

update users
set first_name = 'Eduardo'
where id = 5;

delete
from users
where id = 5;
