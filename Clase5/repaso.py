def votapormi(nombre):
    condicion=0
    while condicion < 3:
        if nombre == "Hayde":
            print("Vota por " + nombre)
            condicion = condicion + 1
        else:
            print("No votes por nadie")
            condicion = 3

votapormi("Hayde")
votapormi("Marce")


def sumalistaacum(lista):
    resultado = 0
    listanueva = []
    for x in lista:
        resultado = resultado + x
        listanueva.append(resultado)

    print(listanueva)

sumalistaacum([1,2,3,4])

def sumalistaacumindice(lista):
    resultado = 0
    listanueva = []
    for x in range(0,len(lista)):
        resultado = resultado + lista[x]
        listanueva.append(resultado)
    print(listanueva)

sumalistaacumindice([2,0,1,7])

def sumalista(lista):
    resultado = 0
    for x in lista:
        resultado = resultado + x

    print(resultado)

sumalista([1,2,3,4])

def sumalistaindice(lista):
    resultado = 0
    for x in range(0,len(lista)):
        resultado = resultado + lista[x]
    print(resultado)

sumalistaindice([2,0,1,7])





def sumadosnumreturn(num1, num2):
    #return(num1+num2)
    resultado = num1+num2
    return(resultado)

resultado = sumadosnumreturn(4,5)
print(resultado)

def sumadosnumprint(num1, num2):
    #return(num1+num2)
    resultado = num1+num2
    print(resultado)

sumadosnumprint(7,9)

def imprimelistaporvalor(lista):
    for cosa in lista:
        print(cosa)

imprimelistaporvalor([3,4,5])

def imprimelistaporindice(lista):
    for indice in range(0,len(lista)):
        print(lista[indice])

imprimelistaporindice(["hola","como","estas"])
imprimelistaporindice([7,6,5,4,3,2,1])

def imprimedict(dict):
    for clave in dict:
        print(clave+":"+str(dict[clave]))

imprimedict({"maria":123456, "juan":1264746, "pepito":1287874, "hayde":12878274})ç
