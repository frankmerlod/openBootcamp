class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def informacion(self):
        if self.nota >= 6:
            aprobado = True
        else:
            aprobado = False
            
        return f'Alumno: {self.nombre} \nNota: {self.nota} \nAprobado: {aprobado}'
    
alumno1 = Alumno('Frank Merlo', 6)
print(alumno1.informacion())
        
        