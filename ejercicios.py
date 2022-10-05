#para que me ayudes en algunas cosas como el seleccionar, como lo harias?, son ejercicios aletorios que estoy haciendo para ir aprendiendo
# que tal te gusta?

def string(a:str):
     print(a)

def suma(a,b):
     return a+b

def resta(a,b):
     return a-b

def multiplicacion(a,b):
     return a*b

def division(a,b):
     # if b != 0:
     #      print("El resultado de la división es: ",str(division(a,b)))
     # else:
     #      print("ERROR")
     return a/b

def potencia(a):
     return a*a

def potenciaCubo(a):
     return a**a

from decimal import Decimal
def raizCuadrada(a):
     return a

string("¿Qué opción deseas elegir? ** ESCOGE CON EL NÚMERO **")
i = 0

# print("suma: 1")
# print("resta: 2")
# print("multiplicación: 3")
# print("división: 4")
# print("potencia cuadrada: 5")
# print("potencia cubica: 6 \n")

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6

print("1( suma )")
print("2( resta )")
print("3( multiplicacion )")
print("4( division )")
print("5( potencia )")
print("6( potencia cubica )")


numero = (input("Elige tu opción: "))

if numero == a or "suma":
     string("** SUMA **")
     i = 0
     while True:
          try:
               a = int(input("Escribe un número: "))
               b = int(input("Escribe un número: "))
               print("La suma de {} y {} es: {}".format(a,b,suma(a,b)))
          except:
               print("Por favor escribe un número entero")
          i += 1

elif numero == b or "resta":
     string("** RESTA **")
     i = 0
     while True:
          try:
               a = int(input("Escribe un número: "))
               b = int(input("Escribe un número: "))
               print("La resta de {} y {} es: {}".format(a,b,resta(a,b)))
          except:
               print("Por favor escribe un número entero")
          i += 1
     
elif numero == 3:
     string("** MULTIPLICACIÓN **")
     i = 0
     while True:
          try:
               a = int(input("Escribe un número: "))
               b = int(input("Escribe un número: "))
               print("La multiplicación de {} y {} es: {}".format(a,b,multiplicacion(a,b)))
          except:
               print("Por favor escribe un número entero")
          i += 1

elif numero == 4:
     string("** DIVISIÓN **")
     i = 0
     while True:
          try:
               a = int(input("Escribe un número: "))
               b = int(input("Escribe un número: "))
               print("La división de {} y {} es: {}".format(a,b,division(a,b)))
          except:
               print("Por favor escribe un número entero")
          i += 1

elif numero == 5:
     string("** POTENCIA CUADRADA **")
     i = 0
     while True:
          try:
               a = int(input("Escribe un número: "))
               print("La potencia cuadrada de {} es: {}".format(a,potencia(a)))
          except:
               print("Por favor escribe un número entero")
          i += 1
     
elif numero == 6:
     string("** POTENCIA CUBICA **")
     i = 0
     while True:
          try:
               a = int(input("Escribe un número: "))
               print("La potencia cubica de {} es: {}".format(a,potenciaCubo(a)))
          except:
               print("Por favor escribe un número entero")
          i += 1

    
# string("** SUMA **")
# i = 0
# end = 100
# while True: # como hacer para que sea un bucle indefinido
#      try:
#           a = int(input("Escribe un número: "))
#           b = int(input("Escribe un número: "))
#           print("La suma de {} y {} es: {}".format(a,b,suma(a,b)))
#      except:
#           print("Por favor escribe un número valido")
#      i += 1
#      break

# string("** RESTA **")
# i = 0
# while True:
#      try:
#          a = int(input("Escribe un número: "))
#          b = int(input("Escribe un número: "))
#          print("La resta de {} y {} es: {}".format(a,b,resta(a,b))) 
#      except:
#           print("Por favor ingresa un entero.")
#      i += 1
#      break     

# string("** MULTIPLICACIÓN **")
# i = 0
# while True:
#      try:
#           a = int(input("Escribe un número: "))
#           b = int(input("Escribe un número: "))
#           print("La multi´plicación de {} y {} es: {}".format(a,b,multiplicacion(a,b)))
#      except:
#           print("Por favor escribe un entero.")
#      i += 1
#      break

# string("** DIVISIÓN **")
# i = 0
# while True:
#      try:
#           a = int(input("Escribe un número: "))
#           b = int(input("Escribe un número: "))
#           a/b
#           print("La división de {} y {} es: {}".format(a,b,division(a,b)))
#      except ZeroDivisionError as e:
#           print("ERROR, ingresa un numero valido diferente de 0",e)
#      i += 1
#      break
# # if b != 0:
# #      print("El resultado de la división es: ",str(division(a,b)))
# # else:
# #      print("ERROR")
# # try:
# #      a = a/b
# #      print("El resultado de la división es: ",str(division(a,b)))
# # except ZeroDivisionError as e:
# #      print("ERROR",e)


# string("** POTENCIA CUADRADA **")
# i = 0
# while True:
#      try:
#           a = int(input("Escribe un número: "))
#           print("La potencia cuadrada de {} es: {}".format(a,potencia(a)))
#      except:
#           print("Por favor ingresa un número valido.")
#      i += 1
#      break

# string("** POTENCIA CUBICA **")
# i = 0
# while True:
#      try:
#           a = int(input("Escribe un número: "))
#           print("El resultado de la potencia cubica de {} es: {}".format(a,potenciaCubo(a)))
#      except:
#           print("Please type a number.")
#      i = i + 1
#      break


string("** RAÍZ CUADRADA **")
n = int(input("Escribe un número: "))
a = Decimal(n)
a = a.sqrt()
print("El resultado de la raíz cuadrada de {} es: {}".format(n,raizCuadrada(a)))
