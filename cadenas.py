# texto_variado = "palabra 123.-#"
# print(type(texto_variado))

#podemos utilizar comillas triples para que el texto se muestre como una cadena que hemos escrito
# print(""" 
# funcionamiento de \
# programa: (opciones)
#     -1 para acceder a opciones
#         -2 para salir
# """)


#subscripting e indexado

# texto = "Python"
# # print(texto[3])
# # print(texto[4])
# # print(texto[-1])
# # print(texto[-6])#vuelve a contar hacia atras las letras-

# # print(texto[6])#no se puede porque se enumeran desde el cero


# letra = texto[0]
# print(letra)

# #  texto[0 ="p"] #error no podemos modificxar una cadena

# letra = "p"
# print(letra)

# texto_compuesto = letra+texto[1]#concatenacion

# print(texto_compuesto)

################################################################



#slicing o substringing

#texto="python"
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])
#print(texto[2:2])

#########################################################
#cadenas y formatos

# texto="hola mundo! Buenas tardes"
# print(texto.lower())#metodo por punto
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print(texto.swapcase())
# texto=texto.upper()


# print(texto)


print("{} + {} = {}".format(2,3,2+3))
print("{}+{}={}".format("hola","mundo","hola mundo"))
print("{:.3f}+{:.4f}={}".format(2,3,2+3))
print("{1}+{0}={2}".format(2,3,2+3))
print("{2}+{0}={1}".format("hola","mundo","hola mundo"))
print("{:d}={:b}={:o}={:x}".format(15,15,15,15))
