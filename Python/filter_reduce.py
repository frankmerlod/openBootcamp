from functools import reduce

def num_par(lista):
    res = filter((lambda x: x % 2 == 0), lista)
    return list(res)

def sumador(lista):
    res = reduce((lambda a,b : a + b), lista)
    return res

def main():
    lista = [5,6,7,8,9,10]
    resultado = sumador(num_par(lista))
    print(resultado)

if __name__ == '__main__':
    main()