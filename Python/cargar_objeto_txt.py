from pickle import *

class Vehiculo:
    def __init__(self, modelo = '', color = '', puertas = 5, motor = 'diesel', cilindrada = 4):
        self.color = color
        self.modelo = modelo
        self.puertas = puertas
        self.motor = motor
        self.cilindrada = cilindrada
        
    def __str__(self):
        return f'Modelo: {self.modelo}, Color: {self.color}, Puertas: {self.puertas}, Motor: {self.motor}, Cilindrada: {self.cilindrada}'
    
auto = Vehiculo('Mustang', 'Rojo', puertas= 3, cilindrada= 8)
print(auto)

f = open('auto_class', 'w+b')
dump(auto, f)
f.close()

d = open('auto_class', 'r+b')
d.seek(0)
f_auto = load(d)
print(f_auto)
d.close()
