SELECT r_name
FROM
customer INNER JOIN orders on c_custkey = o_custkey 
INNER JOIN lineitem ON l_orderkey = o_orderkey
INNER JOIN supplier ON s_suppkey = l_suppkey
INNER JOIN nation ON s_nationkey = n_nationkey
INNER JOIN region ON r_regionkey = n_regionkey
WHERE n_nationkey = c_nationkey
AND
l_extendedprice IN
(SELECT MAX(l_extendedprice)
FROM
customer INNER JOIN orders on c_custkey = o_custkey 
INNER JOIN lineitem ON l_orderkey = o_orderkey
INNER JOIN supplier ON s_suppkey = l_suppkey
INNER JOIN nation ON c_nationkey = n_nationkey
INNER JOIN region ON r_regionkey = n_regionkey
WHERE
c_nationkey = s_nationkey
GROUP BY r_name
ORDER BY SUM(l_extendedprice) DESC LIMIT 1
);