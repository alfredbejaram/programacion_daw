package clase5;

// Ejercicio 1: Uso de if para verificar números positivos y negativo
// 📌 // Objetivo: Pedir un número al usuario y determinar si es positivo, negativo o cero.
// 1. Copia este código en EstructurasControl.java
// 2. Explicación paso a paso en los comentarios.

import java.util.Scanner;

public class Main_5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos un objeto scanner, solo 1 scanner por clase y función

        System.out.println("Introduce un numero: ");
        int numero = scanner.nextInt(); // Leemos el numero ingresado

        // Estructura de selección if-else para verificar el número
        if (numero > 0) {
            System.out.println("El numero es positivo"); //Si el numero es mayor que 0
        } else if (numero < 0) {
            System.out.println("El numero es negativo");
        } else {
            System.out.println("El numero es cero");
        }

        scanner.close(); //Cerramos el scanner
    }

    // 🔹 Ejercicio 2: Uso de switch para menú de opciones
//📌 Objetivo: Crear un menú interactivo donde el usuario elija una opción y se muestre un mensaje diferente según su selección.
// 1️⃣ Copia este código en EstructurasControl.java
// 2️⃣ Explicación en los comentarios.

    public static void switchCase(String[] args) {

        System.out.println("\n\nUSO DE SWITCH PARA MENU DE OPCIONES");

        //Mostramos el menu de opciones del usuario

        System.out.println("Menú de Opciones");
        System.out.println("1. Saludar");
        System.out.println("2. Mostrar fecha");
        System.out.println("3. Salir");

        Scanner scanner = new Scanner(System.in);
        System.out.println("Selecciona una opción: ");
        int opcion = scanner.nextInt(); //Leamos la opción del usuario

        //Evaluamos la opción con switch
        switch (opcion) {
            case 1:
                System.out.println("¡Hola, bienvenido!"); //Opción 1
                break;
            case 2:
                System.out.println("Hoy es un gran día para programar en Java");
                break;
            case 3:
                System.out.println("Saliendo del programa ...");
                break;
            default:
                System.out.println("Opción no válida. Intentalo de nuevo ..."); //Sí elige una opción incorrecta

                scanner.close(); //Cerramos el scanner

        }

    }

    //🔹 Ejercicio 3: Uso de for para mostrar los primeros 10 números
// 📌 Objetivo: Imprimir los números del 1 al 10 usando un bucle for.


    // Usamos un bucle for para contar del 1 al 10
    public static void bucleFor(String[] args) {
        System.out.println("Cuenta del 1 al 10");
        for (int i = 1; i <= 10; i++)
            System.out.println("Numero: " + i); // Mostramos el número en cada iteración

    }


// 🔹 Ejercicio 4: Uso de while para contar hasta que el usuario ingrese 0
//   📌 Objetivo: Pedir números al usuario hasta que ingrese 0.


    public static void bucleWhile(String[] args) {
        //Pedimos el primer número
        System.out.println("\n\nIntroduce el numero (0 para salir): ");
        Scanner scanner = new Scanner(System.in);
        int numero;
        numero = scanner.nextInt();

        //Mientras el número no sea distinto a 0 (!=), sigue pidiendo números. El igual es (==)
        while (numero != 0) {
            System.out.println("Has introducido: " + numero);
            System.out.println("Introduce otro numero (0 para salir): ");
            numero = scanner.nextInt();
        }

        System.out.println("Programa finalizado");
        scanner.close();


    }


    // 🔹 Ejercicio 5: Uso de do-while para pedir contraseña
// 📌 Objetivo: Pedir una contraseña y no permitir el acceso hasta que el usuario ingrese java123.

// CREO UNA NUEVA FUNCIÓN FUERA DEL MAIN

    public static void password(String[] args) {

        Scanner scanner = new Scanner(System.in);  //Scanner sirve para solicitar datos al usuario
        String contra;

        //bucle Do-While
        do {
            System.out.println("Introduce la contraseña: ");
            contra = scanner.nextLine();
        } while (!contra.equals("Java123"));

        System.out.println("Acceso concedido");
        scanner.close();

    }


}



