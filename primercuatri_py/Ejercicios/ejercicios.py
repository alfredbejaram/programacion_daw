# Crea una funcion que determine si un numero es par, impar o neutro

def function(n):
    if n%2 == 0:   #Si n entre 2 tiene residuo 0
        if n == 0:
           print("0")
        else:
           print("par")
    else:
            print("impar")

function(10)


# Imprime por pantalla lo que indica en cada print si el usuario ingresa ciertos números
def fizzBuzz(n):
    if n == 15:
        print("fizzBuzz")
    elif n in [3, 6, 9, 12]:  # Si n = 3,6,9,12 ¿?
        print("Fizz")
    elif n == 5 or n == 10:
        print("Buzz")
    else:
        print(n)


fizzBuzz(15)