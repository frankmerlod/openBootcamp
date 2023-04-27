public class Persona {

    private int edad;
    private String nombre;
    private String telefono;

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getTelefono() {
        return this.telefono;
    }

    public static void main(String[] args){
        Cliente cliente1 = new Cliente();
        cliente1.setEdad(25);
        cliente1.setNombre("Alex");
        cliente1.setTelefono("+58424-444-33-22");
        cliente1.setCredito(500);
        Trabajador trabajador1 = new Trabajador();
        trabajador1.setEdad(28);
        trabajador1.setNombre("Jose");
        trabajador1.setTelefono("+58426-555-444-33");
        trabajador1.setSalario(1500);

        System.out.println("Cliente 1:");
        System.out.println(cliente1.getNombre());
        System.out.println(cliente1.getEdad());
        System.out.println(cliente1.getTelefono());
        System.out.println(cliente1.getCredito());

        System.out.println("Trabajador 1:");
        System.out.println(trabajador1.getNombre());
        System.out.println(trabajador1.getEdad());
        System.out.println(trabajador1.getTelefono());
        System.out.println(trabajador1.getSalario());
        
    }


}

class Cliente extends Persona {
    private int credito;

    public void setCredito(int credito) {
        this.credito = credito;
    }

    public int getCredito() {
        return this.credito;
    }

}

class Trabajador extends Persona {
    private int salario;

    public void setSalario(int salario) {
        this.salario = salario;
    }

    public int getSalario() {
        return this.salario;
    }
}
