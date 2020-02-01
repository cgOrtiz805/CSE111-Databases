SELECT c_name, COUNT(o_orderkey)
FROM Q1, Q5
WHERE
c_custkey = o_custkey
AND
c_nation = "GERMANY"
AND
o_orderyear LIKE "1995%"
GROUP BY
c_name;
