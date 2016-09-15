CREATE TABLE todolists (
	id serial primary key,
	name text
);

CREATE TABLE todoitems (
	id serial primary key,
	item text,
	list_id int references todolists(id)
);
