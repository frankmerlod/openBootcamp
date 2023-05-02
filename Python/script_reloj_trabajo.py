import time

def horas_trabajo(hours, min):
    if hours >= 19 and min >= 1:
        return 'Es hora de ir a casa'
    elif hours >= 9 and hours < 19:
        return f'Restan {18 - hours} horas y {59 - min} de trabajo'
    else:
        return 'Es hora de ir a casa'

horas = int(time.strftime('%H'))
minutos = int(time.strftime('%M'))

print(horas_trabajo(horas, minutos))