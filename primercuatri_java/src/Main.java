public class Main {
    //Metodo principal, punto de partida del programa
    public static void main (String[] args) {

        queEsUnPrograma();
        estructuraBasica();
        declaracionVariables();
        alfredobejaram();
        /*usoVariables();
        alcanceVariables();
        buenasPracticas();
        erroresComunes();*/
    }


    public static void queEsUnPrograma() {

        System.out.println("Un programa tarara rara...");
        System.out.println("Java, Python, Node.js");
        System.out.println("Aprendiendo a programar");
    }


    public static void estructuraBasica() {
        System.out.println("\nEstructura basica:");
        int numero = 42;
        String mensaje = "Hola, mundo";
        boolean esActivo = true;

//Imprime cada valor
        System.out.println("Numero: " + numero);
        System.out.println("Mensajito: " + mensaje);
        System.out.println("Resultado: " + esActivo);

    }

    public static void declaracionVariables() {
        System.out.println("\nDeclaración de variables en Java");


        int edad = 26;
        String nombre = "Alfredo Bejarano Jaramillo";
        double altura = 1.78;
        char sexo = 'M';
        boolean mayoredad = true;

    //Imprime la info

        System.out.println("Edad: " + edad + "\nNombre: " + nombre + "\nAltura: " + altura + "\nSexo: " + sexo + "\n" +
                "" +
                "Mayor de Edad: " + mayoredad);

    }


//Tarea: Presentarse mostrando nombre, edad, altura, ciudad y empleo

    public static void alfredobejaram () {
        System.out.println("\nDatos personales: ");

        String nombre = "Alfredo Bejarano Jaramillo";
        int edad = 26;
        double altura = 1.85;
        String ciudad = "Madrid";
        String empleo = "Tecnico IT Soporte";

        System.out.println("Nombre: " + nombre + "\nEdad: " + edad + "\nAltura: " + altura + "\nCiudad: " + ciudad + "\nEmpleo: " + empleo);

    }




}




