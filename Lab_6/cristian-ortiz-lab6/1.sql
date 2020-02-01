SELECT strftime ('%m', l_shipdate),AVG(l_quantity)
FROM lineitem
WHERE l_shipdate LIKE "1996%"
GROUP BY strftime ('%m', l_shipdate);
