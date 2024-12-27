"""1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono 
y correo electrónico deberán almacenarse en un diccionario.

2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, 
el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, 
el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad 
que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.

Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir. 
Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.
"""


def main():
    MAX_LEN : int = 50
    MIN_LEN :int = 5

    users: dict = dict()
    ids : int = []

    print('Bienvenido a la gestión de usuarios')
    print('Que deseas realizar:')
    print('a) Registrar nuevos usuarios')
    print('b) Listar los usuarios')
    print('c) Editar los usuarios')
    print('d) Eliminar los usuarios')
    print('e) Salir')
    

    
    
    anwser :str = input()
    
    if anwser == 'a' or 'A':
 

        new_user: int = int(
                    input("Ingrese la cantidad de usuarios que desea registrar: "))

        for user in range(new_user):
            print('Ingresando Usuarios')
            id:int = user + 1
        
            print(f'Usuario {id}')

            name: str = input("Ingrese su nombre(s): ")
            while len(name) < MIN_LEN or len(name) > MAX_LEN:
                print("El nombre ingresado no es valido")
                name = input("Ingrese su nombre(s): ")

            last_name: str = input("Ingrese sus apellidos: ")
            while len(last_name) < MIN_LEN or len(last_name) > MAX_LEN:
                print("Los apellidos ingresados no son validos")
                last_name = input("Ingrese sus apellidos: ")

            number_phone: int = int(input("Ingrese su numero de telefono: "))
            while len(str(number_phone)) != 10:
                print("El numero de telefono ingresado no es valido")
                number_phone = int(input("Ingrese su numero de telefono: "))
            email: str = input("Ingrese su correo electronico: ")

            while len(email) < MIN_LEN or len(email) > MAX_LEN:
                print("El correo electronico ingresado no es valido")
                email = input("Ingrese su correo electronico: ")

            messaje: str = f'Hola, {name} {last_name}, en breve recibirás un correo a {email}'

            print(messaje)
            ids.append(id)
            users = {'ids': id, 'name': name, 'last_name': last_name, 'number_phone': number_phone, 'email': email}
            # users.append(id)
            # users.append(name)
            # users.append(last_name)
            # users.append(email)

        print("ids guardados: ", ids)
        print("Usuarios registrados ", users)

    elif anwser == 'b'or 'B':
        for i in users:
            print(users)
        modificar = input('¿Qué usuario id quieres modificar?')
        users.get(ids)
        print(f'Se modificará el registro {modificar}')




    
if __name__ == "__main__":
    main()
