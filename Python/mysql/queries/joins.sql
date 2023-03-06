use lead_gen_business;

select * from clients
join billing on clients.id = billing.clients_id;

select clients.first_name, clients.last_name, sum(billing.amount)
from clients
left join billing on clients.id = billing.clients_id
group by clients.id;