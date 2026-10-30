secret=7
intento= int (input("Adivina el numero(1 al 10):"))
while intento != secret:
    if intento <secret:
        print("Muy bajo")
    intento= int(input("Intenta de nuevo:"))
print("Siuuuu")