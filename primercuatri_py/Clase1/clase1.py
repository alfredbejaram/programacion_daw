#TIPOS NUMERICOS EN PYTHON
from Lib.prueba2 import numero_negativo, division
from builtins import PythonFinalizationError
from ctypes import oledll

#  ENTEROS (int)

# Los enteros son numeros sin decimales, pueden ser positivos o negativos
numero_entero = 43
numero_negativo = -10
print("Numero entero: ", numero_entero)
print("Numero negativo: ", numero_negativo)
print("Tipo de dato: ", type(numero_entero))


print("Numero entero es: ", numero_entero)

# Decimales (float)
# Los numeros flotantes son aquellos que tienen decimales

numero_decimal = 3.14159
temperatura = -12.5

print("Numero decimal:", numero_decimal)
print("Temperatura:", temperatura)
print("Tipo de dato:", type(numero_decimal))


# Numeros complejos (complex)
# Los numeros complejos tienen una parte real y una imaginaria (se usa "j").

num_complejo = 2 + 3j
print("Numero complejo: ", num_complejo)
print("Parte real: ", num_complejo.real, " | Parte imaginaria: ", num_complejo.imag)
print("Tipo de dato:", type(num_complejo))



# Operaciones matematicas basicas con numeros

suma = 10 + 5
resta = 10 - 3
multiplicacion = 4 * 2
division = 10 / 3 #siempre devuelve un float o decimal (/)
divison_entera = 10 // 3 #devuelve un int (//)
modulo = 10 % 3
potencia = 2 ** 3

print("\nOperaciones matematicas:")
print ("Suma: ", suma, " | Resta: ", resta, "| Multiplicación:", multiplicacion)
print ("Division:", division, "| División entera:", divison_entera)
print("Módulo: ", modulo, "| Potencia:", potencia)

# Ejercicio Practico 1:
# Crea dos numeros enteros y muestra la suma y la resta de ellos
# Declara un numero flotante y muestra su valor dividido entre 2

# Booleanos (bool)

# Un booleano solo puede tener dos valores: True (verdadero) o False (falso)
es_python_facil = True
es_python_dificil = False

print("\nBooleanos:")
print("Es Python fácil?", es_python_facil)
print("Es Python dificil?", es_python_dificil)


# Comparaciones que devuelven valores booleanos

mayor_que = 10 > 5 # True porque 10 es mayor que 5
menor_que = 10 < 5 # False porque 10 es menor que 5
igualdad = 10 == 10 # True porque ambos son iguales
diferente = 10 != 5 # True porque 10 y 5 son distintos

print ("10 es mayor que 5: ", mayor_que)
print("10 es menor que 5: ", menor_que)
print("10 es igual que 10: ", igualdad)
print("10 es distinto que 5:", diferente)


# Operaciones logicas con booleanos
and_logico = True and False
or_logico = True and False
not_logico = not True

print("\nOperaciones lógicas:")
print ("True AND False:", and_logico)
print ("True OR False:", or_logico)
print("NOT True: ", not_logico)

#Ejercicio Práctico 2:

# Declara una variable booleana que sea True si 15 es mayor que 8.
# Escribe una expresión que use "and" y otra que use "or" y otra que muestra el resultado

# CADENA DE TEXTO (str)

# Una cadena de texto es una secuencia de caracteres delimitados por comillas

texto_simple = "Hola, mundo"
texto_doble = "Python es genial"

print("\nCadenas de texto:")
print("Texto simple:", texto_simple)
print("Texto doble:", texto_doble)


#Concatenación de cadenas (unir textos)
mensaje = "Python" + "es" + "increible"
print("Concatenacion de cadenas:" + mensaje)


#Repeticion de cadenas
palabra = "Python"

primera_letra = palabra[0] #primer caracter
ultima_letra = palabra[-1] #ultimo caracter

print("\nAcceso a caracteres:")
print("Primera letra: " + primera_letra)
print("Ultima letra: " + ultima_letra)

# Slicing (extraer partes de una cadena)

subcadena = palabra [0:3] #Obtiene Pyt
print("Subcadena: ", subcadena)


# Métodos utiles para cadenas
mayusculas = palabra.upper() # Convierte en mayusculas
minusculas = palabra.lower() # Convierte en minusculas
longitud = len(palabra) # Devuelve la cantidad de caracteres

print("\nMétodos de cadenas: ")
print("Mayusculas: ", mayusculas)
print("Minusculas:",minusculas)
print("Longitud de la palabra:", longitud)


# Ejercicio practico 3
# Crea una variable con tu nombre y apellidos y muestra su longitud
# Concatena tu nombre con una frase de presentación
# Convierte tu nombre en mayúsculas y minusculas
# Extrae los primeros 3 caracteres de tu nombre usando slicing

print("\nEJERCICIO ADICIONAL")
myname = "Alfredo Bejarano Jaramillo"
present = "Trabajo en" + " " + "el" + " " + "sector" + " " + "de la" + " " + "tecnología"
longi = len(myname)

mayus = myname.upper()
minus = myname.lower()

subcat = myname [0:3]

#Mediante varios print
print(myname)
print(longi)
print(present)
print(mayus)
print(minus)
print(subcat)

#Con un solo print
print("\nEJERCICIO CONCATENANDO TODO CON UNA FUNCION Y UN UNICO PRINT")
ejercicio_adic = (f"Nombre: {myname}, Longitud: {longi}, "
                  f"Presentación: {present}, Nombre en mayúsculas: {mayus}, Nombre en minúsculas: {minus}, Extrae las 3 primeras letras: {subcat}")

print(ejercicio_adic)












