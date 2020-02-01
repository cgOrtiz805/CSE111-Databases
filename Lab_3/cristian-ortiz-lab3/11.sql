SELECT COUNT(DISTINCT o.o_custkey) AS Customers
FROM lineitem l, orders o
WHERE l.l_orderkey = o.o_orderkey
AND
l.l_discount >= .04;
