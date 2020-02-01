SELECT COUNT(DISTINCT s.s_suppkey)

FROM part p 
 INNER JOIN partsupp ps ON p.p_partkey = ps.ps_partkey
 INNER JOIN supplier s ON s.s_suppkey = ps.ps_suppkey
 WHERE 
 p.p_type LIKE "%MEDIUM%POLISHED%"
 AND p.p_size IN (3,23,26,49);