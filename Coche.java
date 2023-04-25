package openBootcamp;

public class Coche {
    
    private int puertas;

    public void setPuertas(int n) {
        puertas = n;
    }

    public int sumarPuertas(int n) {
        return puertas + n;
    }

    public static void main(String[] args) {
        Coche carro;
        carro = new Coche();
        carro.setPuertas(4);
        carro.sumarPuertas(1);
       System.out.println(carro);
    }

}
