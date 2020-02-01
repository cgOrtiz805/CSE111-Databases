SELECT s_nation, COUNT(DISTINCT o_orderkey)
FROM Q5, Q2, lineitem l
WHERE
l.l_suppkey = s_suppkey
AND
l_orderkey = o_orderkey
AND
o_orderyear LIKE "1995%"
AND
s_region = "AMERICA"
AND
o_orderstatus = "F"

GROUP BY s_nation,o_orderstatus;