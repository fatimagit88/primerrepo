
print("operaciones")

print("S.suma")
print("R.resta")
print("M.multiplicacion")
print("D.division")
print("A.salir")

opcion = ""
menu = True  
while menu == True: 
        opcion= input("Elige una opcion: ").upper()

        if opcion == "A": 
                print("fin del programa...") 
                menu = False
 
  
        if opcion == "S": 
                num1 = int(input("Dime el primer numero: ")) 
                num2 = int(input("Dime el segundo numero: ")) 
                print(f"La suma de los numeros es: {num1 + num2}") 

 
        if opcion == "R": 
                num1 = int(input("Dime el primer numero: ")) 
                num2 = int(input("Dime el segundo numero: ")) 
                print(f"La resta de los numeros es: {num1 - num2}") 

 
        if opcion == "M": 
                num1 = int(input("Dime el primer numero: ")) 
                num2 = int(input("Dime el segundo numero: ")) 
                print(f"La multiplicacion de los numeros es: {num1 * num2}") 
      
        if opcion == "D": 
                num1 = int(input("Dime el primer numero: ")) 
                num2 = int(input("Dime el segundo numero: ")) 
                print(f"La division de los numeros es: {num1 / num2}") 
 
       
 


 

