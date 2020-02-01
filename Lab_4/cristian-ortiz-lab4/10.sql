SELECT p.p_type, MAX(l.l_discount)
FROM lineitem l, part p
WHERE
p.p_partkey = l.l_partkey
AND
p.p_type LIKE "ECONOMY%"
GROUP BY p.p_type;