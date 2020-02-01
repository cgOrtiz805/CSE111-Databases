SELECT DISTINCT p.p_name
FROM customer c 
INNER JOIN orders o ON c.c_custkey = o.o_custkey 
INNER JOIN lineitem l ON l.l_orderkey = o.o_orderkey
INNER JOIN part p ON l.l_partkey = p.p_partkey
INNER JOIN nation n ON n.n_nationkey = c.c_nationkey
INNER JOIN region r ON r.r_regionkey = n.n_regionkey
WHERE 
r.r_name = "AMERICA"
AND
p.p_partkey IN
(SELECT DISTINCT p_partkey FROM
part INNER JOIN partsupp ON p_partkey = ps_partkey
INNER JOIN supplier ON s_suppkey = ps_suppkey
INNER JOIN nation ON s_nationkey = n_nationkey
INNER JOIN region ON n_regionkey = r_regionkey
WHERE r_name = "ASIA"
GROUP BY p_partkey
HAVING COUNT(DISTINCT s_suppkey) ==4)
ORDER BY p.p_name;