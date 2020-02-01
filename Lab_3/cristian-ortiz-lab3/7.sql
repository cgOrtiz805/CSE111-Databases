SELECT l.l_recieptdate, COUNT(l.l_recieptdate)
FROM customer c, lineitem l, orders o
WHERE o.o_orderkey = l.l_orderkey
AND
o.o_custkey = c.c_custkey
AND
c.c_name = "Customer#000000118"
GROUP BY
l_recieptdate;