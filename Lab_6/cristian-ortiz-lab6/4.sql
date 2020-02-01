SELECT COUNT(s_suppkey)
FROM
    (SELECT s.s_suppkey FROM part
 INNER JOIN partsupp ON p_partkey = ps_partkey
 INNER JOIN supplier s ON s.s_suppkey = ps_suppkey
 INNER JOIN nation ON s.s_nationkey = n_nationkey
WHERE 
n_name = "CANADA"

GROUP BY s_name HAVING COUNT(p_partkey) > 4);