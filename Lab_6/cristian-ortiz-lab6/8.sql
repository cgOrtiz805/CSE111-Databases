SELECT COUNT(DISTINCT c_name)
FROM customer 
INNER JOIN orders ON c_custkey = o_custkey
INNER JOIN lineitem ON l_orderkey = o_orderkey
INNER JOIN supplier ON l_suppkey = s_suppkey
INNER JOIN nation ON n_nationkey = s_nationkey 
INNER JOIN region ON n_regionkey = r_regionkey
WHERE 
r_name = "ASIA"
AND
o_orderkey NOT IN (
SELECT o_orderkey FROM 
customer 
INNER JOIN orders ON c_custkey = o_custkey
INNER JOIN lineitem ON l_orderkey = o_orderkey
INNER JOIN supplier ON l_suppkey = s_suppkey
INNER JOIN nation ON n_nationkey = s_nationkey 
INNER JOIN region ON n_regionkey = r_regionkey
WHERE r_regionkey <> 2);
