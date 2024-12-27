#Variables
#Tipo de datos

#Nombres de variable = valor

#String
first_name : str = 'Juan'
last_name : str = 'García Perez'
full_name : str = first_name + ' ' + last_name

# int, float, bool

age : int = 23
score : float = 9.5
active : bool = True

# Función type para ver el tipo de dato de una variable
result : str = type(first_name)


# Función input() para pedir datos al usuario 
name : str = input('Ingresa tu nombre: ')
age : int = int(input('Ingresa tu edad: '))
score : float = float(input('Ingresa tu nota: '))
active : bool = bool(input('El usuario se encuentra activo: '))

print(type(name))
print(type(age))
print(type(score))
print(type(active))
