# program.py
# Nombre: Sánchez Sánchez Jaime Iván

# Para que el programa haga algo, se debe de agregar instrucciones de código que realicen instrucciones
sum = 1 + 2 # Esto es igual a 3
product = sum * 2

# Función print() sirve para imprimir en una consola
print('\nVariables y Función print()')
print('Suma = ', sum)
print('Producto = ', product)
print('Hola consola ¿Cómo estas? :D')

# Función Type(), sirve para saber que tipo de dato contiene mi variable
distancia_a_alfa_centauri = 4.367
print('\nFunción Type()')
print('Tipo de variable', type(distancia_a_alfa_centauri))

# Operadores aritméticos.
# x + x | Operador de adición que suma dos valores juntos.
# x - x | Operador de resta que quita el valor del lado derecho del lado izquierdo.
# x / x | Operador de división que divide el lado izquierdo tantas veces como especifique el lado derecho.
# x * x | Operador de Multiplicación.

# Operadores de asignación.
# x = 2 | x ahora contiene 2.
# x += 2 | x incrementado en 2. Si antes contenía 2, ahora tiene un valor de 4.
# x -= 2 | x decrementado por 2. Si antes contenía 2, ahora tiene un valor de 0.
# x /= 2 | x dividido por 2. Si antes contenía 2, ahora tiene un valor de 1.
# x *= 2 | x multiplicado por 2. Si antes contenía 2, ahora tiene un valor de 4.

# Importar biblioteca para utilizar fechas
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print('\nMostrar fecha en la consola')
print(date.today())

# Conversión de tipos de datos
print("\nConversión de tipos de datos")
print("Today's date is: " + str(date.today()))

# Datos de tipo de entrada
print("\nBienvenido al programa de bienvenida")
name = input("Introduzca su nombre: ")
print("Saludos: " + name)

# Trabajar con números
print("\nCalculadora")
first_number = int(input("Primer número: "))
second_number = int(input("Segundo número: "))
print(first_number + second_number)