
names = ['Jose','Luis','Luis-']
message = "Jugando con arreglos "+names[0]+"."
print (names[1].lower())
print (message)

names[2]='Jaime'
print(names)

names.append('Dana')
print(names)

newlist = []
newlist.append('1')
newlist.append('2')
newlist.append('3')
newlist.append('4')
newlist.append('5')

print(newlist)

newlist.insert(0,'0.5')
newlist.insert(2,'1.5')

print(newlist)

del newlist[0]
del newlist[1]

print(newlist)
#pop en python borra y devuelve el valor
#tambien se puede poner una posicion de la lista
popped_newlist = newlist.pop()
print(newlist)
print(popped_newlist)

popped_newlist2 = newlist.pop(0)
print(newlist)
print(popped_newlist2)

#El método remove () elimina solo la primera 
# aparición del valor que especifique. Si hay
#es posible que el valor aparezca más de una vez 
#en la lista, deberá usar un bucle para
#determinar si se han eliminado todas las 
#apariciones del valor. 

var = newlist[0]
popped_newlist_3 = newlist.remove(var)
print(newlist)
print("nos quedan los numeros :" , (newlist))


#sort para ordenar la lista

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=1)
print(cars)

#sorted()
#ordena la lista temporalmente solo en esa ejecucion
list_num = ['5','9','7','2']
print(list_num)
print(sorted(list_num))
print(list_num)
#sin necesidad de un valor bool reverse lo hace instantaneamente
list_num.reverse()
print(list_num)

#lenght: para el tamaño de una lista se usa "len"
tam=len(list_num)
print(tam)