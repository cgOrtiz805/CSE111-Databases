SELECT p_type, max_discount
FROM Q10
WHERE
p_type LIKE "ECONOMY%"
GROUP BY p_type;