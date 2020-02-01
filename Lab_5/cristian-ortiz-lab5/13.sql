SELECT o.o_orderpriority, COUNT(DISTINCT o.o_orderkey)
FROM lineitem l INNER JOIN orders o ON l.l_orderkey = o.o_orderkey
WHERE o.o_orderdate BETWEEN "1996-10-01" AND "1996-12-31"
AND
l.l_receiptdate > l.l_commitdate
GROUP BY o.o_orderpriority;
