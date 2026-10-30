palabra = input("Escribe una word:")
vowels= 0
for letra in palabra.lower():
    if letra in "aeiou":
        vowels+=1
print("Tiene", vowels, "vowels")