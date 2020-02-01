SELECT COUNT(DISTINCT o.o_orderkey)
FROM orders o, supplier s, customer c, lineitem l
WHERE
l.l_orderkey = o.o_orderkey
AND
 o.o_custkey = (SELECT c.c_custkey FROM customer WHERE c.c_acctbal < 0)
AND
 l.l_suppkey = (SELECT s.s_suppkey FROM supplier WHERE s.s_acctbal >=0);