# Estructuras de control

# Valores de tipo Bool
# True / False
# Operadores de comparacion (==, !=, >, <, >=, <=)
# Operadores logicos (and, or, not)

import random
number1 : int = 10
number2 : int = 20

result : bool = number1 < number2 and 10 == 10 and 5 != 5


# if, matched, else, elif, for, while, break, continue, pass (switch),

age : int = int(input("Ingrese su edad: "))

if age >=0 and age <= 110:
    print("Es menor de edad")
    if age >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
    
else:
    print("La edad no es valida, intenta de nuevo (min:0, max:110).")

# Semaforo elif
color : str = "red"

if color == "green":
    print("Puede continuar")
elif color == "yellow":
    print("Alto parcial")
elif color == "red":
    print("Alto total")
else:
    print("Invalid color")

match color:
    case "green":
        print("Puede continuar")
    case "yellow":
        print("Alto parcial")
    case "red":
        print("Alto total")
    case _:
        print("Invalid color")

# foreach -> Cuando sepamos cuantas interacciones vamos a tener en un ciclo
# while -> Cuando no sabemos cuantas iteraciones tendremos en un ciclo

ramdon : int = 5
number : int = 0
max_attends : int = 5
attends : int = 0
while number != random and attends < max_attends:
    number = int(input("Ingrese un numero: "))
    attends += 1
else:
    if number == random:
        print("Ganaste")
    else:
        print("Perdiste")