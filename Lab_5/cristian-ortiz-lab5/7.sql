SELECT o.o_orderpriority, COUNT(o.o_orderkey)
FROM lineitem l
INNER JOIN orders o ON o.o_orderkey = l.l_orderkey 
WHERE
o.o_orderdate LIKE "1996%"
AND
l.l_receiptdate < l.l_commitdate
GROUP BY o.o_orderpriority;