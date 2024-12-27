"""Estas funcionalidades son las siguientes

.1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario. 
Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir 
el formato o tipo que tú desees.
2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando
 todos los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza que 
 las operaciones, en efecto, se realizaron de forma exitosa.

Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.
"""


def main():
    users: str = []
    ids : int = []

    new_user: int = int(
                input("Ingrese la cantidad de usuarios que desea registrar: "))

    for user in range(new_user):
        print('Ingresando Usuarios')
        id:int = user + 1
       
        print(f'Usuario {id}')

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
        ids.append(id)
        users.append(id)
        users.append(name)
        users.append(last_name)
        users.append(email)

    print("ids guardados: ", ids)
    print("Usuarios registrados ", users)

        
           

if __name__ == "__main__":
    main()
