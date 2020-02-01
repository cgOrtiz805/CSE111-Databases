SELECT COUNT(DISTINCT o.o_orderkey)
FROM orders o,Q151,Q152, lineitem l
WHERE
l.l_orderkey = o.o_orderkey
AND
l.l_suppkey NOT IN (SELECT s_suppkey FROM Q152)
AND
 o.o_custkey = c_custkey;