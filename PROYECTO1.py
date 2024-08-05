###CALCULADORA DE INDICE DE MASA CORPORAL###
print("\tBienvenido humano estas ingresando a la calculeitor3000 de IMC")
#saludo al usuario
nombre= input("Ingresa tu nombre y apellido: \n")
print("Bienvenido a la calculeitor3000 de IMC "+nombre+" espero te encuentres bien")
print("\tA continuacion necesitare tu edad, altura y peso para continuar")

#recoleccion de datos
edad_valida = False
while not edad_valida:
    try:
        edad = int(input("Introduce tu edad en años:\n "))
        if 1 <= edad <= 99:
            edad_valida = True
        else:
            print("Edad incorrecta, ingrese su edad en años de nuevo:")
    except ValueError:
        print("Por favor, ingrese solo números.")
altura_valida = False
while not altura_valida:
    try:
        altura = float(input("Introduce tu estatura (en metros): \n"))
        if 0.5 <= altura <= 2.2:
            altura_valida = True
        else:
            print("Altura no valida. Por favor, ingrese una altura entre 0.5 y 2.2metros.")
    except ValueError:
        print("Por favor, ingrese solo números.")
peso_valido = False
while not peso_valido:
    try:
        peso = float(input("Introduce tu peso (en kilogramos): \n"))
        if 20 <= peso <= 250:
            peso_valido = True
        else:
            print("Peso no valido. Por favor, ingrese un peso entre 20 y 250 kilogramos.")
    except ValueError:
        print("Por favor, ingrese solo números.")
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



