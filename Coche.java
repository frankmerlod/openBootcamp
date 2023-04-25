package openBootcamp;

public class Coche {
    
    private int puertas = 4;

    public void sumarPuertas(int n) {
        int resultado = puertas + n;
        puertas = resultado;
        
    }

    public static void main(String[] args) {
        Coche carro;
        carro = new Coche();
        carro.sumarPuertas(2);
        System.out.println(carro.puertas);
        Coche carro2;
        carro2 = new Coche();
        carro2.sumarPuertas(1);
        System.out.println(carro2.puertas);

    }

}
