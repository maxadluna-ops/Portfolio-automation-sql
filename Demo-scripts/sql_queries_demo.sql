-- Top 5 productos más vendidos
SELECT producto_id, SUM(cantidad) AS total_vendido
FROM ventas
GROUP BY producto_id
ORDER BY total_vendido DESC
LIMIT 5;

-- Clientes frecuentes (más de 10 compras)
SELECT c.nombre, COUNT(v.id) AS total_compras
FROM clientes c
JOIN ventas v ON c.id = v.cliente_id
GROUP BY c.nombre
HAVING COUNT(v.id) > 10
ORDER BY total_compras DESC;
