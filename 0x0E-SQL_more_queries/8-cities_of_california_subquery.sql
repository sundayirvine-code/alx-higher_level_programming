-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword

SELECT id, name FROM cities WHERE state_id IN (
  SELECT state_id FROM states WHERE name = 'California') ORDER BY cities.id;
  
