f = open('mi_file.txt', 'w')
f.write('Hola, Mundo!')
f.close()

d = open('mi_file.txt', 'r')
datos = d.read()
d.close()
print(datos)




