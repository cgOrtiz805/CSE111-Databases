SELECT MAX(DISTINCT l.l_discount)
FROM lineitem l
WHERE
l.l_discount < (SELECT AVG(l_discount) 
FROM lineitem INNER JOIN orders ON o_orderkey = l_orderkey WHERE
o_orderdate HAVING substr(o_orderdate,1,8));
