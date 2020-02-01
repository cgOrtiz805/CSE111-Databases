SELECT c_nation, COUNT(o.o_orderkey)
FROM Q1, orders o
WHERE
c_custkey = o.o_custkey
AND
c_region = "EUROPE"
GROUP BY c_nation;
