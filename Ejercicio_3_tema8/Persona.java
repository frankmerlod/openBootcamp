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
        Persona persona = new Persona();
        persona.setEdad(33);
        persona.setNombre("Frank");
        persona.setTelefono("+58424-444-33-22");

        System.out.println(persona.getNombre());
        System.out.println(persona.getEdad());
        System.out.println(persona.getTelefono());
        
    }
}
