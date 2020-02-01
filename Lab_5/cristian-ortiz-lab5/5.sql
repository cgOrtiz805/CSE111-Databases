SELECT  s.s_name , p.p_size, MIN(ps.ps_supplycost)
FROM part p 
INNER JOIN partsupp ps ON p.p_partkey = ps.ps_partkey
INNER JOIN supplier s ON s.s_suppkey = ps.ps_suppkey
INNER JOIN nation n ON s.s_nationkey = n.n_nationkey
INNER JOIN region r ON r.r_regionkey = n.n_regionkey
WHERE
p.p_type LIKE "%STEEL%"

AND
r.r_name = "AMERICA"
GROUP BY p.p_size
ORDER BY s.s_name ASC;

