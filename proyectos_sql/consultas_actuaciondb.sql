/*1. Mostrar todas las series de Netflix*/

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


/*2. Calcular la media de la duración de las series de MIVI*/ 

SELECT c.id_plataforma, AVG(s.duracion)
FROM series s
INNER JOIN cartelera c ON s.cod_serie = c.cod_serie
WHERE c.id_plataforma = 'MIVI';

+---------------+-----------------+
| id_plataforma | AVG(s.duracion) |
+---------------+-----------------+
| MIVI          |         60.0000 |
+---------------+-----------------+
1 row in set (0.000 sec)



/*3. Contar cuantas series de genero ROMANTICA hay en la plataforma MIVI*/

SELECT COUNT(categoria)
FROM cartelera 
WHERE id_plataforma = 'MIVI' 
AND categoria = 'romantica';

+------------------+
| COUNT(categoria) |
+------------------+
|                1 |
+------------------+
1 row in set (0.000 sec)



/*4. Mostrar el nombre de las series que ha protagonizado “Brad Pitt”*/

SELECT a.nombre_act, s.nombre_serie
FROM series s
INNER JOIN actores a ON s.actor_prota = a.actor_prota
WHERE a.nombre_act = 'Brad Pitt';

+------------+--------------+
| nombre_act | nombre_serie |
+------------+--------------+
| Brad Pitt  | The Crown    |
+------------+--------------+
1 row in set (0.000 sec)



/*5. Mostrar el nombre del actor/actriz más viejo que ha protagonizado una serie de más de 4 temporadas*/
SELECT a.nombre_act, MAX(a.edad) AS edad, s.temporadas
FROM series s
INNER JOIN actores a ON s.actor_prota = a.actor_prota
GROUP BY a.edad
HAVING s.temporadas > 4;

+---------------+------+------------+
| nombre_act    | edad | temporadas |
+---------------+------+------------+
| Daniel Br├╝hl  |   43 |          5 |
| Javier Bardem |   52 |          8 |
| Daniel Craig  |   53 |         10 |
| Brad Pitt     |   58 |          5 |
+---------------+------+------------+
4 rows in set (0.000 sec)


/* 6. Mostrar el nombre de la serie con más temporadas emitida en Netflix.*/




7. Mostrar todos los datos de los actores Españoles con más de 15 películas que tengan menos de 45 años. 
8. Mostrar el nombre de la serie con más temporadas con una duración mayor de 60 
9. Mostrar el nombre y el argumento de las series emitidas en HBOM 
10. Mostrar el total de las series que protagonice “Leonardo Di Caprio” 
11. Calcular la media del precio de las plataformas “Semestrales” 
