def Anio_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return f'{anio} ES Bisiesto'
            else:
                return f'{anio} No es Bisiesto'
        else:
            return f'{anio} ES Bisiesto'
    else:
        return f'{anio} NO es Bisiesto'
    
for i in range(1900,2500):
    print(Anio_bisiesto(i))
