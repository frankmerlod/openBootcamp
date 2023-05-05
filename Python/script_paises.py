def main():
    inp = input('Ingresa algunos paises sin repetirlos y separados por una coma: ').split(',')
    paises = sorted(set([i.lower() for i in inp]))
    resultado = ''
    count = 0
    for pais in paises:
        resultado += f'{pais.strip().capitalize()}'
        count += 1
        if count < len(paises):
            resultado += ', '
        else:
            resultado += '.'
        
    print(resultado)
    
if __name__ == '__main__':
    main()