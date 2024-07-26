###CALCULADORA DE INDICE DE MASA CORPORAL###
print("\tBienvenido humano estas ingresando a la calculeitor3000 de IMC")
#saludo al usuario
nombre= input("Ingresa tu nombre y apellido: \n")
print("Bienvenido a la calculeitor3000 de IMC "+nombre+" espero te encuentres bien")
print("\tA continuacion necesitare tu edad, altura y peso para continuar")

#recoleccion de datos
edad= int(input("Introduce tu edad en años:\n "))
altura= float(input("introduce tu estatura(en metros): \n"))
peso= float(input("introduce tu peso(en kilos): \n"))
IMC= peso/altura**2

#datos recolectados
print(f"Tienes {edad} años.")
print(f"Tu nombre y apellido es: {nombre}")
print(f"Mides {altura} metros")
print(f"Pesas {peso} kilogramos")
print(f"\tCon los datos obtenidos podemos calcucalar que tu IMC es: {IMC:.2f}")
print("Por lo tanto esto quiere decir que;\n")


if IMC >= 0 and IMC <= 18.4 :
        print ("Estas en un muy bajo peso")
elif IMC >= 18.5 and IMC <= 24.9 :
        print ("Tu peso es el ideal")
elif IMC >= 25 and IMC <= 29.9:
        print ("estas en sobrepeso, bajale un poco")
elif IMC >= 30 and IMC <= 34.9 :
        print ("Estas en obesidad tipo 1")
elif IMC >= 35.00 and IMC <= 39.9:
        print ("Estas en obesidad tipo 2")
elif IMC >= 40:
     print("Estas en obesidad tipo 3")



