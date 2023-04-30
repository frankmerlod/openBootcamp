class Vehiculo:
    color = 'Rojo'
    puertas = 5
    ruedas = 4
     
class Coche(Vehiculo):
   velocidad = 120
   cilindrada = 4
    
coche = Coche()
print('Color:', coche.color)
print('Ruedas:', coche.ruedas)
print('Puertas:', coche.puertas)
print('Velocidad:', coche.velocidad)
print('Cilindrada:', coche.cilindrada)