SELECT COUNT()
FROM partsupp INNER JOIN supplier ON ps_suppkey = s_suppkey INNER JOIN part ON  p_partkey = ps_partkey INNER JOIN nation ON s_nationkey = n_nationkey
WHERE  
n_name = "CANADA" AND
ps_supplycost * ps_availqty
 IN (
SELECT ps_supplycost * ps_availqty 
FROM partsupp
ORDER BY ps_supplycost * ps_availqty DESC
LIMIT (
    SELECT COUNT(*) * .03
    FROM partsupp
    )
    );