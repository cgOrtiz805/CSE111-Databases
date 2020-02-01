SELECT s.s_name, c.c_name
FROM
customer c INNER JOIN orders o ON c.c_custkey = o.o_custkey
INNER JOIN lineitem l ON l.l_orderkey = o.o_orderkey
INNER JOIN supplier s ON s.s_suppkey = l.l_suppkey 
WHERE 
o.o_totalprice = (SELECT MAX(o_totalprice) FROM orders WHERE o_orderstatus = "F");