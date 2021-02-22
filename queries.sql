-- initialize tables
CREATE TABLE grids
	(
     id integer primary key,
     size integer
    );

CREATE TABLE nodes
	(
     id integer primary key,
     grid_id integer,
     index_number integer,
     x integer,
     y integer,
     foreign key(grid_id) references grids(id)
    );
CREATE INDEX node_index ON nodes(index_number);

-- get x, y given grid_id and index_number
select x, y
from nodes
where grid_id = 1
  and index_number = 0;

-- find neighbors
-- write recursive query
-- or materialize nodes in neighbors table
CREATE TABLE neighbors
	(
     id integer primary key,
     node_id integer,
     origin_node_id integer,
     radius integer,
     type text,
     foreign key(node_id) references nodes(id),
     foreign key(origin_node_id) references nodes(id)
    );