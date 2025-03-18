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