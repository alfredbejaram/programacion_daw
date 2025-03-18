#Ejercicio 1: Operaciones numericas complejas
#Define cinco variables numericas distintas (int, float, complex) y
#realiza diversas operaciones matemáticas (potenciacion, division entera, módulo).
#Imprime los resultados formateados por una cadena clara y descriptiva

print("OPERACIONES NUMERICAS COMPLEJAS")

num1, num2, num3, num4, num5 = 10, 3, 2.5, 7.2, 4+2j

resultado = (f"Potencia: {num1 ** num2}, Divison entera: {num1//num2}, "
             f"Modulo: {num1%num2}, Multiplicacion: {num3*num4}, Complejo: {num5}")
print(resultado)



# Ejercicio 2: Combinacion de cadenas y números
# Define dos variables numericas (int, float) y tres cadenas diferentes.
# Genera una nueva cadena combinando texto con el resultado de operaciones aritméticas entre estas variables
# Usa conversación explicita (str()) para insertar valores numericos en la cadena final


num_int, num_float = 8, 3.5
cadena1, cadena2, cadena3 = "Resultado: ", "La suma es ", "y la division es "
resultado = cadena1 + "" + cadena2 + "" + cadena3 + "" + str(num_int/num_float)
print(resultado)


# Ejercicio 3: Manipulacion avanzada de cadenas
# Crea una cadena larga que contenga espacios en blanco al inicio, final y en medio
# Realiza varias operaciones encadenadas como eliminar
# espacios, extremos, convertir to_do a mayúsculas,
# y dividir la cadena en varias subcadenas usando un separador específico

cadena = " Esto es una cadena para manipular datos"
nueva_cadena = cadena.strip().upper().split()

print(nueva_cadena)


#Ejercicio 4: índices y subcadenas
#Define una cadena extensa








# Ejercicio 5: Formato y conversación numerica
# Define variables numéricas (entero, flotante, complejo).
# Crea una cadena con formato avanzado (f - strings) que muestre numeros
# con precisión definida (dos decimales, notificación científica, etc.)
# Evita concatenar directamente numeros y textos














largo, ancho, radio, altura = 10, 5, 3, 4
area_rectangulo


