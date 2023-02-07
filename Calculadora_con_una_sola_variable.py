#Calculadora con una sola variable
#Ejercicio de Operadores de Asignacion

print("Calculadora\n")
print("********************")
print("* Menu de opciones *")
print("********************")

print("\n1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto")
numero = int(input("\n Introduce una opcion: ")) 

if numero == 1:
    print("Eligio la Suma")
    numero = int(input("Ingrese el primer numero: "))
    numero += int(input("Ingrese el primer numero: "))
    print("El Resultado es: ",numero)
    
elif numero == 2:
    print("Eligio la Resta")
    numero = int(input("Ingrese el primer numero: "))
    numero -= int(input("Ingrese el primer numero: "))
    print("El Resultado es: ",numero)
    
elif numero == 3:
    print("Eligio la Multiplicacion")
    numero = int(input("Ingrese el primer numero: "))
    numero *= int(input("Ingrese el primer numero: "))
    print("El Resultado es: ",numero)
    
elif numero == 4:
    print("Eligio la Divición")
    numero = int(input("Ingrese el primer numero: "))
    numero /= int(input("Ingrese el primer numero: "))
    print("El Resultado es: ",round(numero,3))

elif numero == 5:
    print("Eligio la Divición entera")
    numero = int(input("Ingrese el primer numero: "))
    numero //= int(input("Ingrese el primer numero: "))
    print("El Resultado es: ",numero)

elif numero == 6:
    print("Eligio la Exponente")
    numero = int(input("Ingrese el primer numero: "))
    numero **= int(input("Ingrese el primer numero: "))
    print("El Resultado es: ",numero)

elif numero == 7:
    print("Eligio la Modulo o resto")
    numero = int(input("Ingrese el primer numero: "))
    numero %= int(input("Ingrese el primer numero: "))
    print("El Resultado es: ",numero)
else:
    print("** El numero que marco no es una opcion **")
print("FIN.")
