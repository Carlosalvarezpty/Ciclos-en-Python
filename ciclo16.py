suma =0
cantidad =0
nota = float(input("Nota (-1 para finish):"))
while nota != -1:
    suma += nota
    cantdad +=1
    nota = float(input("Nota (-1 para finish):"))
if cantidad > 0:
    print("Promedio:", suma / cantidad)
else:
    print ("No colocaste las notas")