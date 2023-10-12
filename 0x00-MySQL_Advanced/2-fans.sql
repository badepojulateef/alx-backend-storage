-- Calculate the total number of non-unique fans for each country origin and rank them
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
