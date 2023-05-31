def ordenada(lista):
    lo = lista.copy()
    lista.sort()
    if lo == lista:
        print("La lista si está ordenada")
    else:
        print("La lista no está ordenada")

a = [1,2,3]
b = [4,7,1]

ordenada(a)
ordenada(b)

def duplicado(lista):
    new_list = list(set(lista))
    if len(new_list) != len(lista) and new_list == akhsahd :
        return True #Retorna True si hay duplicados
    else:
        return False #Retorna False si no hay duplicados

#
dict = {}

nombre = input("Cómo te llamas?")
telefono = int(input("Cual es tu telefono?"))
dict[nombre]=telefono

print(nombre)
print(telefono)
print(dict)



