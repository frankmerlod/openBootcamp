package openBootcamp.Ejercicio_2_estructuras_control;

public class Ejercicio_5 {

    public static void main(String[] args){

        String estacion = "hola";

        switch (estacion){
            case "Verano":
                System.out.println("Es verano...");
                break;
            case "Primavera":
                System.out.println("Es Primavera...");
                break;
            case "Otr;o":
                System.out.println("Es Otro;o...");
                break;
            case "Invierno":
                System.out.println("Es invierno...");
                break;
            default:
                System.out.println("No es una estacion...");
                break;
        }
    }
    
}
