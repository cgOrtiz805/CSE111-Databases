SELECT r.r_name, COUNT(DISTINCT o.o_orderkey)
FROM customer c, orders o, region r, nation n
WHERE o.o_custkey = c.c_custkey
AND c.c_nationkey = n.n_nationkey
AND r.r_regionkey = n.n_regionkey
AND o.o_orderstatus = "F"
GROUP BY r.r_name 
ORDER BY COUNT(DISTINCT o.o_orderkey ) DESC;