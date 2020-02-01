SELECT (SUM(ps.ps_supplycost))
FROM partsupp ps INNER JOIN part p ON p.p_partkey = ps.ps_partkey

WHERE

p.p_retailprice < 1000 AND

p.p_partkey IN ( SELECT l_partkey FROM lineitem INNER JOIN partsupp ON ps_suppkey = l_suppkey WHERE l_shipdate LIKE "1996%") 
AND
ps_suppkey NOT IN( SELECT DISTINCT ps_suppkey FROM  part INNER JOIN lineitem ON p_partkey = l_partkey INNER JOIN partsupp ON ps_suppkey = l_suppkey WHERE
l_extendedprice < 1000 AND l_shipdate LIKE "1995%")
;






