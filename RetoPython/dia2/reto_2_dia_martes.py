"""Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer. Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.

Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.

Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.

Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.

Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.

Así mismo el número de teléfono será a 10 dígitos.

Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.
"""
def main():
    records: int = int(input("Ingrese la cantidad de usuarios que desea registrar: "))
    for i in range(records):
        print(f'Usuario {i+1}')

        name: str = input("Ingrese su nombre(s): ")
        while len(name) < 5 or len(name) > 50:
            print("El nombre ingresado no es valido")
            name = input("Ingrese su nombre(s): ")

        last_name: str = input("Ingrese sus apellidos: ")
        while len(last_name) < 5 or len(last_name) > 50:
            print("Los apellidos ingresados no son validos")
            last_name = input("Ingrese sus apellidos: ")

        number_phone: int = int(input("Ingrese su numero de telefono: "))
        while len(str(number_phone)) != 10:
            print("El numero de telefono ingresado no es valido")
            number_phone = int(input("Ingrese su numero de telefono: "))
        email: str = input("Ingrese su correo electronico: ")

        while len(email) < 5 or len(email) > 50:
            print("El correo electronico ingresado no es valido")
            email = input("Ingrese su correo electronico: ")

        messaje: str = f'Hola, {name} {last_name}, en breve recibirás un correo a {email}'

        print(messaje)

if __name__ == "__main__":
   main()
