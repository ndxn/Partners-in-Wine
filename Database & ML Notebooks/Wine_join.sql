select * into Red_soil_table
from red_table
inner join soil_table
using(appellation);

select * from Red_soil_table;

select * into White_soil_table
from white_table
inner join soil_table
using(appellation);

select * from White_soil_table;