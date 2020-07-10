# esribir un programa que pida al usuario un texto y un numero entero
# mandar a imprimir en pantalla el texto repetido las veces indicado por
# el numero. nota: hacer el programa usando una funcion

#ingresa un texto:hola
#ingresa un numero:4
#salida:
#hola
#hola
#hola
#hola

#declarar la funcion
def repetir(texto,numero):
    texto += "\n"
    print(texto*numero)
#escribir el codigo para usar la funcion
t = input("ingresa un texto")
n = int(input("ingresa un numero"))

repetir(t,n)