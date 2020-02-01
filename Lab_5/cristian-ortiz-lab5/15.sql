SELECT SUM2/SUM1
FROM
(SELECT SUM(l.l_extendedprice * (1 - l.l_discount)) as SUM1
FROM lineitem l
INNER JOIN supplier s ON s.s_suppkey = l.l_suppkey 
INNER JOIN orders o ON o.o_orderkey = l.l_orderkey 
INNER JOIN customer c ON c.c_custkey = o.o_custkey
INNER JOIN  nation n ON n.n_nationkey = c.c_nationkey
INNER JOIN region r ON r.r_regionkey = n.n_regionkey
INNER JOIN nation nn ON nn.n_nationkey = s.s_nationkey
WHERE 
nn.n_name NOT IN (SELECT r_name FROM region WHERE r_name == "UNITED STATES")
AND l.l_shipdate LIKE "1996%" AND
r.r_name == "EUROPE")
,
(SELECT SUM(l_extendedprice * (1 - l_discount)) as SUM2
FROM lineitem 
INNER JOIN supplier ON s_suppkey = l_suppkey 
INNER JOIN orders ON o_orderkey = l_orderkey 
INNER JOIN customer ON c_custkey = o_custkey
INNER JOIN  nation n1 ON n1.n_nationkey = c_nationkey
INNER JOIN region ON r_regionkey = n1.n_regionkey
INNER JOIN nation n2 ON n2.n_nationkey = s_nationkey
WHERE
l_shipdate LIKE "1996%" AND
r_name == "EUROPE" AND
n2.n_name == "UNITED STATES");


