
CREATE TRIGGER PartD
AFTER DELETE ON part
FOR EACH ROW
BEGIN 
DELETE FROM partsupp WHERE ps_partkey = OLD.p_partkey;
DELETE FROM lineitem WHERE l_partkey = OLD.p_partkey;
END;


DELETE FROM part
WHERE p_partkey IN 
(SELECT ps_partkey
 FROM partsupp 
INNER JOIN supplier ON ps_suppkey=s_suppkey
INNER JOIN nation ON s_nationkey = n_nationkey
 WHERE n_name IN('FRANCE','GERMANY'));




SELECT AVG(ps_supplycost), n_name
FROM
partsupp INNER JOIN supplier ON ps_suppkey = s_suppkey 
INNER JOIN nation ON n_nationkey = s_nationkey
INNER JOIN region ON n_regionkey = r_regionkey
WHERE r_name = 'EUROPE'
GROUP BY n_name;