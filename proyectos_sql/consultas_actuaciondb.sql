/*Mostrar todas las series de Netflix*/

SELECT c.id_plataforma, s.nombre_serie
FROM cartelera c
INNER JOIN series s ON c.cod_serie = s.cod_serie
WHERE c.id_plataforma = 'NETF';

+---------------+-----------------+
| id_plataforma | nombre_serie    |
+---------------+-----------------+
| NETF          | Breaking Bad    |
| NETF          | Game of Thrones |
+---------------+-----------------+
2 rows in set (0.000 sec)


