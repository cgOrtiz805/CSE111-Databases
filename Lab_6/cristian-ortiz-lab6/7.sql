SELECT COUNT(*)
FROM (
SELECT s_name
FROM customer 
INNER JOIN orders ON c_custkey = o_custkey
INNER JOIN lineitem ON l_orderkey = o_orderkey
INNER JOIN supplier ON s_suppkey = l_suppkey
INNER JOIN nation ON c_nationkey = n_nationkey 
WHERE
n_name  = "GERMANY" OR n_name = "FRANCE"
GROUP BY s_name
HAVING COUNT(DISTINCT o_orderkey)<30);


