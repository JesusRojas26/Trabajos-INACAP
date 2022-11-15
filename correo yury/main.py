import getpass as gp
import time
import SQLconnector
import os
import json

user = ""
cursor = SQLconnector.db.cursor()
program = True

# Clase create_dict usada para mostrar los datos obtenidos de la base de datos

class create_dict(dict):
    def __init__(self):
        super().__init__()
        dict()

    def add(self, key, value):
        self[key] = value

mydict = create_dict()

# Función para desbloquear usuarios

def desbloquearUsuario():
    print("-------Desbloquear un usuario------")
    while True:
        rut = input("Rut -> ")
        if rut[-2] == "-":
            break
        else:
            print("Formato incorrecto, debe ingresar un rut válido")
            continue
    sql = "update EMPLEADO set ID_ESTADO = 1 where RUT=(%s)"
    cursor.execute(sql, [rut, ])
    SQLconnector.db.commit()
    print("Usuario desbloqueado con éxito")

# Función para eliminar usuarios

def eliminarEmpleado():
    print("-------Eliminar un usuario------")
    while True:
        rut = input("Rut -> ")
        if rut[-2] == "-":
            break
        else:
            print("Formato incorrecto, debe ingresar un rut válido")
            continue
    sql = "delete from EMPLEADO where RUT=(%s)"
    cursor.execute(sql, [rut, ])
    SQLconnector.db.commit()
    print("Usuario eliminado con éxito")

# Función para el inicio de sesión.

def logIn():
    while True:
        try:

            # Contador de intentos para definir el bloqueo de la cuenta después de 3 intentos fallidos.

            intentos = 0

            while True:

                os.system("cls")

                print(" --- Inicio de sesión Correo de Yury --- \n")

                # Inicio de sesión

                userName = input("Nombre de usuario: ")
                passwd = gp.getpass("Contraseña: ")

                if intentos < 2:

                    os.system("cls")

                    # Creación de la consulta sql para buscar el nombre de usuario ingresado
                    # previamente dentro de la base de datos, y almacenandolo en una variable.

                    sql = "select NOMBRE_USUARIO from EMPLEADO where NOMBRE_USUARIO = (%s)"

                    cursor.execute(sql, [userName, ])
                    sUN = cursor.fetchone()

                    # Checkeo de que el nombre de usuario se haya encontrado  .

                    if sUN[0] == "":
                        os.system("cls")
                        print("Nombre de usuario no encontrado, reintente")
                        time.sleep(1)
                        continue
                    else:

                        # Si el usuario fue encontrado, se extrae la contraseña almacenada
                        # en ese usuario para usarla en el inicio de sesión.

                        sql = "select CONTRASENIA from EMPLEADO where NOMBRE_USUARIO = (%s)"
                        cursor.execute(sql, [userName, ])
                        sPW = cursor.fetchone()

                        # Se checkea que se haya encontrado algo en la búsqueda.

                        if sPW[0] != "":
                            if sPW[0] == passwd:

                                # Si la contraseña encontrada coincide con la ingresada, entonces el usuario
                                # puede iniciar sesión.

                                os.system("cls")
                                print("Verificando estado...")

                                # Verificando si el estado del empleado es activo, de lo contrario
                                # no puede ingresar al programa.

                                sql = "select ID_ESTADO from EMPLEADO where NOMBRE_USUARIO = (%s)"
                                cursor.execute(sql, [userName, ])
                                est = cursor.fetchone()
                                time.sleep(1.5)

                                if est[0] == 1:
                                    os.system("cls")
                                    print("¡Usuario activo!")
                                    time.sleep(1)

                                    x = 0

                                    while x < 5:
                                        os.system("cls")
                                        print("Iniciando sesión.")
                                        time.sleep(0.1)
                                        os.system("cls")
                                        print("Iniciando sesión..")
                                        time.sleep(0.1)
                                        os.system("cls")
                                        print("Iniciando sesión...")
                                        time.sleep(0.1)
                                        x += 1

                                    os.system("cls")
                                    print("Sesión iniciada con éxito!")

                                    # Se crea una variable global en donde se almacena el usuario activo
                                    globals()['user'] = userName

                                    return userName
                                else:

                                    # En caso de que el usuario esté inactivo, no se le da acceso al programa
                                    # y se expulsa al usuario del programa.

                                    print(
                                        "\nSu cuenta está desactivada, contacte al Jefe de RRHH")
                                    a = input(
                                        "Presione enter para continuar...")
                                    exit()
                            else:

                                # Si el usuario ingresa la contraseña de manera incorrecta, se suma un intento.

                                print("\nContraseña incorrecta")
                                time.sleep(1)
                                intentos += 1
                                continue
                        else:

                            # Si la contraseña no se encontró no se le suma un intento al usuario, ya que
                            # puede deberse a una falla de la base de datos.
                            # Se le pide al usuario intentarlo nuevamente.

                            os.system("cls")
                            print("Por favor, escriba su contraseña")
                            a = input("Presione enter para continuar...")
                            continue

                else:

                    # Si el usuario erra su contraseña tres veces, el programa se lo informa y
                    # la cuenta del usuario es cambiada a inactiva.

                    os.system("cls")
                    print(
                        "Cantidad máxima de intentos excedida. Su cuenta será bloqueada.")
                    time.sleep(5)

                    # Actualización de la tabla empleado para dejar la cuenta inactiva en la base de datos.

                    sql = "update EMPLEADO set ID_ESTADO = 2 where NOMBRE_USUARIO = (%s)"
                    cursor.execute(sql, (userName,))

                    SQLconnector.db.commit()

                    exit()

        except KeyboardInterrupt:
            os.system("cls")
            print("Por favor no interrumpa el programa.")
            time.sleep(1)
            print("Reiniciando...")
            time.sleep(0.5)
            os.system("cls")
            continue
        except:
            print("\nHa ocurrido un error, se reiniciará el programa")
            a = input("Presione enter para continuar...")
            continue

# Función para el jefe de RRHH, en donde puede ver la lista de trabajadores especificada en los requerimientos.

def verListaTrabajadores():
    try:

        # Selección de la vista que contiene los filtros solicitados en los requerimientos

        sql = "select * from lista_trabajadores"

        cursor.execute(sql)
        result = cursor.fetchall()

        # Contador para asignarle un número a los trabajadores al mostrarlos

        c = 0

        for x in list(result):

            c += 1

            # Validaciónes de los datos para entregar la información de forma más clara.

            # Sexo

            if x[0] == 1:
                sexo = "Masculino"
            else:
                sexo = "Femenino"

            # Cargo

            if x[1] == 1:
                cargo = "Administrador"
            elif x[1] == 2:
                cargo = "Jefe RRHH"
            elif x[2] == 3:
                cargo = "Trabajador RRHH"
            else:
                cargo = "Trabajador"

            # Departamento

            if x[2] == 1:
                depto = "Departamento Administracion"
            elif x[2] == 2:
                depto = "Departamento RRHH"
            elif x[2] == 3:
                depto = "Departamento Produccion"
            elif x[2] == 4:
                depto = "Departamento Compras"
            elif x[2] == 5:
                depto = "Departamento Financiero"
            elif x[2] == 6:
                depto = "Departamento Contabilidad"
            elif x[2] == 7:
                depto = "Departamento Tesorería"
            elif x[2] == 8:
                depto = "Departamento Marketing"
            elif x[2] == 9:
                depto = "Departamento Comercial"
            else:
                depto = "Departamento Ventas"

            # Area

            if x[3] == 1:
                area = "Administracion"
            elif x[3] == 2:
                area = "Producción"
            elif x[3] == 3:
                area = "Finanzas"
            else:
                area = "Comercial"

            mydict.add(("#" + str(c)), ({
                "Sexo": sexo,
                "Cargo": cargo,
                "Departamento": depto,
                "Area": area
            }))

        print(json.dumps(mydict, indent=1))

    except:
        pass

# Ingresar nuevo usuario con sus datos personales.

def ingresoTrabajadores():

    while True:

        try:
            os.system("cls")
            print(" --- Ingreso de nuevo trabajador --- \n")

            nombre_completo = input("Nombre y apellido -> ")

            # Checkeo que el rut cumpla el formato "00.000.000-0"

            while True:
                rut = input("Rut -> ")
                if rut[-2] == "-":
                    break
                else:
                    print("Formato incorrecto, debe ingresar un rut válido")
                    continue

            sexo = int(input("Genero (1: Masculino, 2: Femenino) -> "))
            direccion = input("Dirección -> ")

            # Checkeo que el número telefónico tenga 8 números

            while True:
                tel = input("Teléfono (Sin +56 9) -> ")
                if len(tel) == 8 and tel.isnumeric():
                    break
                else:
                    print("Número inválido")
                    continue

            while True:
                passwd = input("Establezca una contraseña -> ")
                passwd2 = input("Repita la contraseña -> ")

                if passwd == passwd2:
                    break
                else:
                    print("\nLas contraseñas no coinciden")
                    continue

            tel = "+56 9 " + tel

            # Valores por defecto de los usuarios nuevos

            comuna = 1
            estado = 1

            # Separación del nombre completo en solo nombre y solo apellido.

            lstNombre = nombre_completo.split()
            nombre = lstNombre[0].title()
            apellido = lstNombre[1].title()

            # Creación automática del nombre de usuario con formato nombre.apellido

            userName = nombre.lower() + "." + apellido.lower()

            sql = "insert into EMPLEADO(RUT, NOMBRE, APELLIDO, ID_GENERO, TELEFONO, DIRECCION, ID_COMUNA, NOMBRE_USUARIO, CONTRASENIA,ID_ESTADO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,1)"
            val = (rut, nombre, apellido, sexo, tel,
                   direccion, comuna, userName, passwd, estado)

            cursor.execute(sql, val)
            SQLconnector.db.commit()

            time.sleep(1.5)
            os.system("cls")

            print("¡Trabajador ingresado con éxito!")
            opt = input("\n¿Desea continuar agregando trabajadores? (s/n) -> ")
            if opt.lower() == "s":
                continue
            else:
                print("Saliendo al menú...")
                time.sleep(1.5)
                break

        except ValueError:
            print(
                "\nIngresó un valor incorrecto, por favor ingrese valores numéricos si así se le pide.")
            a = input("Presione enter para continuar...")
            continue
        except:
            print("Ocurrió un error, se reiniciará el programa")
            a = input("Presione enter para continuar...")
            continue

# Ingresar datos laborales del trabajador

def ingresoDatosLaborales():
    while True:
        try:

            os.system("cls")
            print(" --- Ingreso datos laborales --- \n")

            # Se predefine un arreglo con los cargos y deptos para verificar que se ingrese información correcta

            cargos = ["jefe rrhh", "trabajador rrhh", "trabajador"]
            deptos = ["administración", "recursos humanos", "producción", "compras",
                      "financiero", "contabilidad", "tesorería", "marketing", "comercial", "ventas"]
            jefes = []

            # El rut se pide para hacer la actualización en la base de datos al trabajador correcto

            rut = input(
                "Introduzca el rut del trabajador al cuál añadir datos laborales -> ")

            # Se valida que el cargo, departamento y jefes sean correctos y forman parte de la base de datos

            while True:
                print("Cargos disponibles: " + str(cargos[:]).title())
                cargo = input("Cargo -> ")
                if cargo.lower() in cargos:
                    break
                else:
                    print("Cargo inválido")
                    continue

            while True:
                print("Departamentos disponibles: " + str(deptos[:]).title())
                depto = input("Departamento -> ")
                if depto.lower() in deptos:
                    break
                else:
                    print("Departamento inválido")
                    continue

            # Tomando todos los jefes de la base de datos para mostrarlos

            sql = "select RUT, NOMBRE, APELLIDO from EMPLEADO where ID_CARGO = 2"
            cursor.execute(sql)
            results = cursor.fetchall()
            c = 0

            for x in results:
                c += 1
                jefes.append(x[0])
                mydict.add(("#" + str(c)), ({
                    "Rut": x[0],
                    "Nombre": x[1],
                    "Apellido": x[2]
                }))

            print("Jefes disponibles: ")
            print(json.dumps(mydict, indent=1))

            while True:
                jefe = input("Rut del jefe -> ")
                if jefe in jefes:
                    break
                else:
                    print("Jefe inválido")
                    continue

            # Se hace el cambio a números de las variables, ya que, en la base de datos se manejan de esta forma
            # pero se ingresaron de forma string para hacerlo más amigable con el usuario

            # Cargo

            if cargo.lower() == cargos[0]:
                cargo = 2
            elif cargo.lower() == cargos[1]:
                cargo = 3
            else:
                cargo = 4

            # Departamento

            if depto.lower() == deptos[0]:
                depto = 1
            elif depto.lower() == deptos[1]:
                depto = 2
            elif depto.lower() == deptos[2]:
                depto = 3
            elif depto.lower() == deptos[3]:
                depto = 4
            elif depto.lower() == deptos[4]:
                depto = 5
            elif depto.lower() == deptos[5]:
                depto = 6
            elif depto.lower() == deptos[6]:
                depto = 7
            elif depto.lower() == deptos[7]:
                depto = 8
            elif depto.lower() == deptos[8]:
                depto = 9
            else:
                depto = 10

            # Actualización del empleado en la base de datos

            sql = "update EMPLEADO set ID_CARGO = (%s), ID_DEPARTAMENTO = (%s), ID_JEFE = (%s) where RUT = (%s)"
            val = (cargo, depto, jefe, rut)

            time.sleep(1)

            cursor.execute(sql, val)
            print("¡Trabajador actualizado con éxito!")
            SQLconnector.db.commit()

            cont = input("¿Desea actualizar otro trabajador? (s/n) -> ")
            if cont.lower() == "n":
                print("Cerrando...")
                time.sleep(1)
                break
            else:
                print("Reiniciando...")
                time.sleep(1)
                continue

        except:
            print("Ha habido un problema, se reiniciará")
            a = input("Presione enter para continuar...")
            continue

# Ingreso contacto de emergencia de un trabajador

def ingresoContactoEmergencia():
    while True:
        try:
            os.system("cls")
            print(" --- Ingreso de contactos de emergencia --- \n")

            # Pidiendo rut para asociar al trabajador con el contacto

            rutE = input("Ingrese rut del empleado -> ")

            sql = "select RUT from EMPLEADO where RUT = (%s)"
            cursor.execute(sql, [rutE, ])
            result = cursor.fetchone()

            if result[0] == "":
                print("Trabajador no encontrado o inexistente")
                time.sleep(1.5)
                continue

            # Se piden los datos del contacto

            while True:
                rut = input("Ingrese rut de la carga familiar -> ")
                if rut[-2] == "-":
                    break
                else:
                    print("Formato incorrecto, debe ingresar un rut válido")
                    continue

            # Se pide nombre y apellido, y se separan para ingresarlos en la base de datos

            nombre_completo = input("Nombre y apellido -> ")
            lstNombre = nombre_completo.split()
            nombre = lstNombre[0].title()
            apellido = lstNombre[1].title()

            # Se pide el telefono y se checkea el formato

            while True:
                tel = input("Teléfono (Sin +56 9) -> ")
                if len(tel) == 8 and tel.isnumeric():
                    break
                else:
                    print("Número inválido")
                    continue

            tel = "+56 9 " + tel

            rel = input("Relación -> ")

            sql = "insert into CONTACT_EMERG values(%s,%s,%s,%s,%s,%s)"
            val = (rut, nombre, apellido, tel, rel, rutE)

            cursor.execute(sql, val)
            SQLconnector.db.commit()

            time.sleep(1)
            os.system("cls")
            print("¡Contacto de emergencia ingresado con éxito!")

            # Finalmente se pregunta si se desea continuar

            cont = input(
                "¿Desea agregar otro contacto de emergencia? (s/n) -> ")
            if cont.lower() == "s":
                print("Reiniciando...")
                time.sleep(1)
                continue
            else:
                print("Cerrando...")
                time.sleep(1)
                break

        except:
            pass

# Ingreso carga familiar de un trabajador

def ingresoCargaFamiliar():
    while True:
        try:
            os.system("cls")
            print(" --- Ingreso de cargas familiares --- \n")

            # Pidiendo el rut del trabajador para asociar la carga familiar a este

            rutE = input("Ingrese rut del empleado -> ")

            sql = "select RUT from EMPLEADO where RUT = (%s)"
            cursor.execute(sql, [rutE, ])
            result = cursor.fetchone()

            if result[0] == "":
                print("Trabajador no encontrado o inexistente")
                time.sleep(1.5)
                continue

            # Se pide el rut de la carga, y se valida que tenga formato correcto

            while True:
                rut = input("Ingrese rut de la carga familiar -> ")
                if rut[-2] == "-":
                    break
                else:
                    print("Formato incorrecto, debe ingresar un rut válido")
                    continue

            # Se pide el nombre de la carga, y luego se divide en dos variables separadas

            nombre_completo = input("Nombre y apellido -> ")
            lstNombre = nombre_completo.split()
            nombre = lstNombre[0].title()
            apellido = lstNombre[1].title()

            parentesco = input("Parentesco entre la carga y el empleado -> ")
            sexo = int(input("Genero (1: Masculino, 2: Femenino) -> "))

            # Se ingresa la carga a la base de datos

            sql = "insert into CARGA_FAMILIAR values(%s,%s,%s,%s,%s,%s)"
            val = (rut, nombre, apellido, parentesco, sexo, rutE)

            cursor.execute(sql, val)
            SQLconnector.db.commit()

            time.sleep(1)
            os.system("cls")
            print("¡Carga familiar ingresada con éxito!")

            # Finalmente se pregunta si se desea continuar

            cont = input("¿Desea agregar otra carga familiar? (s/n) -> ")
            if cont.lower() == "s":
                print("Reiniciando...")
                time.sleep(1)
                continue
            else:
                print("Cerrando...")
                time.sleep(1)
                break

        except ValueError:
            print(
                "Error, ingresó un valor incorrecto. Por favor ingrese números cuando así se le pida")
            a = input("Presione enter para continuar...")
            continue
        except:
            print("Hubo un problema, reiniciando...")
            a = input("Presione enter para continuar...")
            continue

# Actualizar datos personales, laborales, cargas y contactos de emergencia de trabajadores

def actualizarDatos():
    while True:
        try:
            os.system("cls")
            print(" --- Actualizar datos --- \n")

            print(" 1- Datos personales")
            print(" 2- Datos laborales")
            print(" 3- Cargas familiares")
            print(" 4- Contactos de emergencia")
            print(" 5- Salir\n")

            while True:
                sel = input("Seleccione qué actualizar -> ")
                if int(sel) in range(1, 6):
                    print("Cargando...")
                    time.sleep(1)
                    os.system("cls")
                    break
                else:
                    print("Opción incorrecta, por favor ingrese solo números")
                    time.sleep(2)
                    continue

            # ! Datos personales

            if sel == "1":
                while True:
                    os.system("cls")
                    print(" --- Datos personales --- \n")                
                                
                    while True:

                        rut = input("Ingrese rut del trabajador a actualizar -> ")

                        sql = "select RUT from EMPLEADO where RUT = (%s)"
                        cursor.execute(sql,[rut,])
                        result = cursor.fetchone()
                        if result[0] == "":
                            print("Rut no encontrado, reinentelo por favor")
                            time.sleep(2)
                            os.system("cls")
                        else:
                            continue                   
                                        
                        sexo = int(input("Genero (1: Masculino, 2: Femenino) -> "))
                        direccion = input("Dirección -> ")

                        # Checkeo que el número telefónico tenga 8 números
                                
                        while True:
                            tel = input("Teléfono (Sin +56 9) -> ")
                            if len(tel) == 8 and tel.isnumeric():
                                break
                            else:
                                print("Número inválido")
                                continue
                                
                        tel = "+56 9 " + tel

                        time.sleep(1)
                        os.system("cls")
                        print("Actualizando...")

                        # Actualizando en la base de datos al empleado seleccionado

                        sql = "update EMPLEADO set ID_GENERO = (%s), DIRECCION = (%s), TELEFONO = (%s) where RUT = (%s)"
                        val = (sexo, direccion, tel, rut)

                        cursor.execute(sql,val)
                        SQLconnector.db.commit()

                        print("Datos actualizados con éxito!")
                        cont = input("¿Desea actualizar más trabajadores? (s/n) -> ")
                        if cont.lower() == "s":
                            print("Reiniciando...")
                            time.sleep(1)
                            os.system("cls")
                            continue
                        else:
                            print("Cerrando...")
                            time.sleep(1)
                            os.system("cls")
                            break

            # ! Datos laborales

            elif sel == "2":
                while True:
                    os.system("cls")
                    print(" --- Datos laborales --- \n")

                    # Se predefine un arreglo con los cargos y deptos para verificar que se ingrese información correcta

                    cargos = ["jefe rrhh","trabajador rrhh","trabajador"]
                    deptos = ["administración","recursos humanos","producción","compras","financiero","contabilidad","tesorería","marketing","comercial","ventas"]
                    jefes = []

                    rut = input("Ingrese rut del trabajador a actualizar -> ")

                    # Se valida que el cargo, departamento y jefes sean correctos y forman parte de la base de datos

                    while True:
                        print("Cargos disponibles: " + str(cargos[:]).title())
                        cargo = input("Cargo -> ")
                        if cargo.lower() in cargos:
                            break
                        else:
                            print("Cargo inválido")
                            continue
                                
                    while True:
                        print("Departamentos disponibles: " + str(deptos[:]).title())
                        depto = input("Departamento -> ")
                        if depto.lower() in deptos:
                            break
                        else:
                            print("Departamento inválido")
                            continue

                    # Tomando todos los jefes de la base de datos para mostrarlos
                                
                    sql = "select RUT, NOMBRE, APELLIDO from EMPLEADO where ID_CARGO = 2"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    c = 0

                    for x in results:
                        c += 1
                        jefes.append(x[0])
                        mydict.add(("#" + str(c)),({
                        "Rut":x[0],
                        "Nombre":x[1],
                        "Apellido":x[2]
                    }))

                    print("Jefes disponibles: ")
                    print(json.dumps(mydict, indent = 1))

                    while True:                
                        jefe = input("Rut del jefe -> ")
                        if jefe in jefes:
                            break
                        else:
                            print("Jefe inválido")
                            continue

                    # Se hace el cambio a números de las variables, ya que, en la base de datos se manejan de esta forma
                    # pero se ingresaron de forma string para hacerlo más amigable con el usuario

                    # Cargo

                    if cargo.lower() == cargos[0]:
                        cargo = 2
                    elif cargo.lower() == cargos[1]:
                        cargo = 3
                    else:
                        cargo = 4

                    # Departamento

                    if depto.lower() == deptos[0]:
                        depto = 1
                    elif depto.lower() == deptos[1]:
                        depto = 2
                    elif depto.lower() == deptos[2]:
                        depto = 3
                    elif depto.lower() == deptos[3]:
                        depto = 4
                    elif depto.lower() == deptos[4]:
                        depto = 5
                    elif depto.lower() == deptos[5]:
                        depto = 6
                    elif depto.lower() == deptos[6]:
                        depto = 7
                    elif depto.lower() == deptos[7]:
                        depto = 8
                    elif depto.lower() == deptos[8]:
                        depto = 9
                    else:
                        depto = 10

                    # Actualización del empleado en la base de datos

                    sql = "update EMPLEADO set ID_CARGO = (%s), ID_DEPARTAMENTO = (%s), ID_JEFE = (%s) where RUT = (%s)"
                    val = (cargo, depto, jefe, rut)

                    time.sleep(1)    

                    cursor.execute(sql, val)
                    print("Datos actualizados con éxito!")
                    SQLconnector.db.commit()

                    cont = input("¿Desea actualizar más datos? (s/n) -> ")
                    if cont.lower() == "n":
                        print("Cerrando...")
                        time.sleep(1)
                        break
                    else:
                        print("Reiniciando...")
                        time.sleep(1)
                        continue

            # ! Carga familiar

            elif sel == "3":
                while True:
                    os.system("cls")
                    print(" --- Cargas familiares --- \n")

                    # Pidiendo el rut del trabajador para asociar la carga familiar a este

                    rutE = input("Introduzca el rut del empleado a asociar -> ")

                    sql = "select RUT from EMPLEADO where RUT = (%s)"
                    cursor.execute(sql, [rutE,])
                    result = cursor.fetchone()

                    if result[0] == "":
                        print("Trabajador no encontrado o inexistente")
                        time.sleep(1.5)
                        continue
                                
                    # Se pide el rut de la carga, y se valida que tenga formato correcto
                                
                    rut = input("Ingrese rut de la carga familiar -> ")

                    # Se pide el nombre de la carga, y luego se divide en dos variables separadas

                    nombre_completo = input("Nombre y apellido -> ")
                    lstNombre = nombre_completo.split()
                    nombre = lstNombre[0].title()
                    apellido = lstNombre[1].title()

                    parentesco = input("Parentesco entre la carga y el empleado -> ")
                    sexo = int(input("Genero (1: Masculino, 2: Femenino) -> "))     

                    # Checkeando que la carga ingresada esté relacionada con el trabajador ingresado

                    sql = "select RUT from CARGA_FAMILIAR where ID_EMPLEADO = (%s)"
                    cursor.execute(sql, [rutE,])
                    result = cursor.fetchone()

                    if result[0] == rut:
                        pass
                    else:
                        print("Error, la carga familiar ingresada no coincide con el empleado, o el empleado no\ntiene ninguna carga asociada.")
                        print("Se reiniciará para que reintente el ingreso de los datos.")
                        a = input("Presione enter para continuar...")
                        os.system("cls")
                        continue

                    # Se actualiza la carga a la base de datos

                    sql = "update CARGA_FAMILIAR set NOMBRE = (%s), APELLIDO = (%s), PARENTESCO = (%s), ID_GENERO = (%s) where RUT = (%s)"
                    val = (nombre,apellido,parentesco,sexo,rut)

                    cursor.execute(sql,val)
                    SQLconnector.db.commit()
                                
                    time.sleep(1)
                    os.system("cls")
                    print("¡Carga familiar actualizada con éxito!")

                    # Finalmente se pregunta si se desea continuar

                    cont = input("¿Desea actualizar otra carga familiar? (s/n) -> ")
                    if cont.lower() == "s":
                        print("Reiniciando...")
                        time.sleep(1)
                        continue
                    else:
                        print("Cerrando...")
                        time.sleep(1)
                        break

            # ! Contacto de emergencia

            elif sel == "4":
                while True:
                    print(" --- Contactos de emergencia --- \n")

                    # Pidiendo rut para asociar al trabajador con el contacto

                    rutE = input("Introduzca el rut del trabajador a asociar -> ")

                    # Verificando que el trabajador exista en la base de datos

                    sql = "select RUT from EMPLEADO where RUT = (%s)"
                    cursor.execute(sql, [rutE,])
                    result = cursor.fetchone()

                    if result[0] == "":
                        print("Trabajador no encontrado o inexistente")
                        time.sleep(1.5)
                        continue
                                
                    rut = input("Ingrese rut del contacto de emergencia -> ")

                    # Se pide nombre y apellido, y se separan para ingresarlos en la base de datos

                    nombre_completo = input("Nombre y apellido -> ")
                    lstNombre = nombre_completo.split()
                    nombre = lstNombre[0].title()
                    apellido = lstNombre[1].title()

                    # Se pide el telefono y se checkea el formato

                    while True:
                        tel = input("Teléfono (Sin +56 9) -> ")
                        if len(tel) == 8 and tel.isnumeric():
                            break
                        else:
                            print("Número inválido")
                            continue

                    tel = "+56 9 " + tel

                    rel = input("Relación -> ")

                    # Checkeando que el empleado y el contacto esten relacionados

                    sql = "select RUT from CONTACT_EMERG where ID_EMPLEADO = (%s)"
                    cursor.execute(sql, [rutE,])
                    result = cursor.fetchone()

                    if result[0] == rut:
                        pass
                    else:
                        print("Error, el contacto ingresado no coincide con el empleado, o el empleado no\ntiene ningun contacto asociado.")
                        print("Se reiniciará para que reintente el ingreso de los datos.")
                        a = input("Presione enter para continuar...")
                        os.system("cls")
                        continue

                    sql = "update CONTACT_EMERG set NOMBRE = (%s), APELLIDO = (%s), TELEFONO = (%s), RELACION = (%s) where ID_EMPLEADO = (%s)"
                    val = (nombre,apellido,tel,rel,rutE)

                    cursor.execute(sql,val)
                    SQLconnector.db.commit()
                                
                    time.sleep(1)
                    os.system("cls")
                    print("¡Contacto de emergencia actualizado con éxito!")

                    # Finalmente se pregunta si se desea continuar

                    cont = input("¿Desea actualizar otro contacto de emergencia? (s/n) -> ")
                    if cont.lower() == "s":
                        print("Reiniciando...")
                        time.sleep(1)
                        continue
                    else:
                        print("Cerrando...")
                        time.sleep(1)
                        break

            # ! Menú

            else:
                print("Saliendo al menú...")
                time.sleep(1)
                break

        except:
            print("Error, se reiniciará el programa")
            a = input("Presione enter para continuar...")
            continue

def actualizarPersonales(trabajador):
    while True:
        print(" --- Datos personales --- \n")                
                    
        while True:

            rut = trabajador

            sql = "select RUT from EMPLEADO where RUT = (%s)"
            cursor.execute(sql,[rut,])
            result = cursor.fetchone()
            if result[0] == "":
                print("Rut no encontrado, reinentelo por favor")
                time.sleep(2)
                os.system("cls")
            else:
                continue                   
                            
            sexo = int(input("Genero (1: Masculino, 2: Femenino) -> "))
            direccion = input("Dirección -> ")

            # Checkeo que el número telefónico tenga 8 números
                    
            while True:
                tel = input("Teléfono (Sin +56 9) -> ")
                if len(tel) == 8 and tel.isnumeric():
                    break
                else:
                    print("Número inválido")
                    continue
                    
            tel = "+56 9 " + tel

            time.sleep(1)
            os.system("cls")
            print("Actualizando...")

            # Actualizando en la base de datos al empleado seleccionado

            sql = "update EMPLEADO set ID_GENERO = (%s), DIRECCION = (%s), TELEFONO = (%s) where RUT = (%s)"
            val = (sexo, direccion, tel, rut)

            cursor.execute(sql,val)
            SQLconnector.db.commit()

            print("Datos actualizados con éxito!")
            cont = input("¿Desea actualizar más datos? (s/n) -> ")
            if cont.lower() == "s":
                print("Reiniciando...")
                time.sleep(1)
                os.system("cls")
                continue
            else:
                print("Cerrando...")
                time.sleep(1)
                os.system("cls")
                break

def actualizarLaborales(trabajador):
    while True:
        print(" --- Datos laborales --- \n")

        # Se predefine un arreglo con los cargos y deptos para verificar que se ingrese información correcta

        cargos = ["jefe rrhh","trabajador rrhh","trabajador"]
        deptos = ["administración","recursos humanos","producción","compras","financiero","contabilidad","tesorería","marketing","comercial","ventas"]
        jefes = []

        rut = trabajador

        # Se valida que el cargo, departamento y jefes sean correctos y forman parte de la base de datos

        while True:
            print("Cargos disponibles: " + str(cargos[:]).title())
            cargo = input("Cargo -> ")
            if cargo.lower() in cargos:
                break
            else:
                print("Cargo inválido")
                continue
                    
        while True:
            print("Departamentos disponibles: " + str(deptos[:]).title())
            depto = input("Departamento -> ")
            if depto.lower() in deptos:
                break
            else:
                print("Departamento inválido")
                continue

        # Tomando todos los jefes de la base de datos para mostrarlos
                    
        sql = "select RUT, NOMBRE, APELLIDO from EMPLEADO where ID_CARGO = 2"
        cursor.execute(sql)
        results = cursor.fetchall()
        c = 0

        for x in results:
            c += 1
            jefes.append(x[0])
            mydict.add(("#" + str(c)),({
            "Rut":x[0],
            "Nombre":x[1],
            "Apellido":x[2]
        }))

        print("Jefes disponibles: ")
        print(json.dumps(mydict, indent = 1))

        while True:                
            jefe = input("Rut del jefe -> ")
            if jefe in jefes:
                break
            else:
                print("Jefe inválido")
                continue

        # Se hace el cambio a números de las variables, ya que, en la base de datos se manejan de esta forma
        # pero se ingresaron de forma string para hacerlo más amigable con el usuario

        # Cargo

        if cargo.lower() == cargos[0]:
            cargo = 2
        elif cargo.lower() == cargos[1]:
            cargo = 3
        else:
            cargo = 4

        # Departamento

        if depto.lower() == deptos[0]:
            depto = 1
        elif depto.lower() == deptos[1]:
            depto = 2
        elif depto.lower() == deptos[2]:
            depto = 3
        elif depto.lower() == deptos[3]:
            depto = 4
        elif depto.lower() == deptos[4]:
            depto = 5
        elif depto.lower() == deptos[5]:
            depto = 6
        elif depto.lower() == deptos[6]:
            depto = 7
        elif depto.lower() == deptos[7]:
            depto = 8
        elif depto.lower() == deptos[8]:
            depto = 9
        else:
            depto = 10

        # Actualización del empleado en la base de datos

        sql = "update EMPLEADO set ID_CARGO = (%s), ID_DEPARTAMENTO = (%s), ID_JEFE = (%s) where RUT = (%s)"
        val = (cargo, depto, jefe, rut)

        time.sleep(1)    

        cursor.execute(sql, val)
        print("Datos actualizados con éxito!")
        SQLconnector.db.commit()

        cont = input("¿Desea actualizar más datos? (s/n) -> ")
        if cont.lower() == "n":
            print("Cerrando...")
            time.sleep(1)
            break
        else:
            print("Reiniciando...")
            time.sleep(1)
            continue

def actualizarCargaFamiliar(trabajador):
    while True:
        print(" --- Cargas familiares --- \n")

        # Pidiendo el rut del trabajador para asociar la carga familiar a este

        rutE = trabajador

        sql = "select RUT from EMPLEADO where RUT = (%s)"
        cursor.execute(sql, [rutE,])
        result = cursor.fetchone()

        if result[0] == "":
            print("Trabajador no encontrado o inexistente")
            time.sleep(1.5)
            continue
                    
        # Se pide el rut de la carga, y se valida que tenga formato correcto
                    
        rut = input("Ingrese rut de la carga familiar -> ")

        # Se pide el nombre de la carga, y luego se divide en dos variables separadas

        nombre_completo = input("Nombre y apellido -> ")
        lstNombre = nombre_completo.split()
        nombre = lstNombre[0].title()
        apellido = lstNombre[1].title()

        parentesco = input("Parentesco entre la carga y el empleado -> ")
        sexo = int(input("Genero (1: Masculino, 2: Femenino) -> "))     

        # Checkeando que la carga ingresada esté relacionada con el trabajador ingresado

        sql = "select RUT from CARGA_FAMILIAR where ID_EMPLEADO = (%s)"
        cursor.execute(sql, [rutE,])
        result = cursor.fetchone()

        if result[0] == rut:
            pass
        else:
            print("Error, la carga familiar ingresada no coincide con el empleado, o el empleado no\ntiene ninguna carga asociada.")
            print("Se reiniciará para que reintente el ingreso de los datos.")
            a = input("Presione enter para continuar...")
            os.system("cls")
            continue

        # Se actualiza la carga a la base de datos

        sql = "update CARGA_FAMILIAR set NOMBRE = (%s), APELLIDO = (%s), PARENTESCO = (%s), ID_GENERO = (%s) where RUT = (%s)"
        val = (nombre,apellido,parentesco,sexo,rut)

        cursor.execute(sql,val)
        SQLconnector.db.commit()
                    
        time.sleep(1)
        os.system("cls")
        print("¡Carga familiar actualizada con éxito!")

        # Finalmente se pregunta si se desea continuar

        cont = input("¿Desea actualizar otra carga familiar? (s/n) -> ")
        if cont.lower() == "s":
            print("Reiniciando...")
            time.sleep(1)
            continue
        else:
            print("Cerrando...")
            time.sleep(1)
            break

def actualizarContactoEmergencia(trabajador):
    while True:
        print(" --- Contactos de emergencia --- \n")

        # Pidiendo rut para asociar al trabajador con el contacto

        rutE = trabajador

        # Verificando que el trabajador exista en la base de datos

        sql = "select RUT from EMPLEADO where RUT = (%s)"
        cursor.execute(sql, [rutE,])
        result = cursor.fetchone()

        if result[0] == "":
            print("Trabajador no encontrado o inexistente")
            time.sleep(1.5)
            continue
                    
        rut = input("Ingrese rut del contacto de emergencia -> ")

        # Se pide nombre y apellido, y se separan para ingresarlos en la base de datos

        nombre_completo = input("Nombre y apellido -> ")
        lstNombre = nombre_completo.split()
        nombre = lstNombre[0].title()
        apellido = lstNombre[1].title()

        # Se pide el telefono y se checkea el formato

        while True:
            tel = input("Teléfono (Sin +56 9) -> ")
            if len(tel) == 8 and tel.isnumeric():
                break
            else:
                print("Número inválido")
                continue

        tel = "+56 9 " + tel

        rel = input("Relación -> ")

        # Checkeando que el empleado y el contacto esten relacionados

        sql = "select RUT from CONTACT_EMERG where ID_EMPLEADO = (%s)"
        cursor.execute(sql, [rutE,])
        result = cursor.fetchone()

        if result[0] == rut:
            pass
        else:
            print("Error, el contacto ingresado no coincide con el empleado, o el empleado no\ntiene ningun contacto asociado.")
            print("Se reiniciará para que reintente el ingreso de los datos.")
            a = input("Presione enter para continuar...")
            os.system("cls")
            continue

        sql = "update CONTACT_EMERG set NOMBRE = (%s), APELLIDO = (%s), TELEFONO = (%s), RELACION = (%s) where ID_EMPLEADO = (%s)"
        val = (nombre,apellido,tel,rel,rutE)

        cursor.execute(sql,val)
        SQLconnector.db.commit()
                    
        time.sleep(1)
        os.system("cls")
        print("¡Contacto de emergencia actualizado con éxito!")

        # Finalmente se pregunta si se desea continuar

        cont = input("¿Desea actualizar otro contacto de emergencia? (s/n) -> ")
        if cont.lower() == "s":
            print("Reiniciando...")
            time.sleep(1)
            continue
        else:
            print("Cerrando...")
            time.sleep(1)
            break

f = 2

def menuTipo():

    os.system("cls")

    # Checkeando el tipo de usuario

    sql = "SELECT ID_CARGO FROM empleado WHERE NOMBRE_USUARIO=(%s)"
    cursor.execute(sql, [user, ])
    result = cursor.fetchone()

    match(result[0]):
        case 1:
            print("administrador")
        case 2:
            menuJefeRRHH()
        case 3:
            menuTrabajadorRRHH()
        case 4:
            menuTrabajador()

# funciones menu para cada tipo de usuario

def menuTrabajadorRRHH():
    os.system("cls")
    print("<-------------Bienvenido al menú Trabajador de recursos humanos------>\n")
    print("(1)  Ingresar datos personales de nuevo usuario")
    print("(2)  Ingresar datos laborales")
    print("(3)  Ingresar contacto de emergencia")
    print("(4)  Ingresar carga familiar")
    print("(5)  Actualizar datos")
    print("(6)  Cerrar sesión\n")
    while True:
        sel = int(input("Seleccione su opción-> "))
        if(sel) in range(1, 7):
            print("Cargando...")
            time.sleep(1)
            os.system("cls")
            match(sel):
                case 1:
                    ingresoTrabajadores()
                case 2:
                    ingresoDatosLaborales()
                case 3:
                    ingresoContactoEmergencia()
                case 4:
                    ingresoCargaFamiliar()
                case 5:
                    actualizarDatos()
                case 6:
                    print("Cerrando sesión...")
                    time.sleep(1.5)
                    os.system("cls")
                    break

            break
        else:
            print("Opción incorrecta, por favor ingrese solo números")
            time.sleep(2)
            continue

def menuJefeRRHH():
    os.system("cls")
    print("<-------------Bienvenido al menú Jefe de recursos humanos------>\n")
    print("(1)  Ingresar nuevo trabajador")
    print("(2)  Actualizar datos")
    print("(3)  Eliminar trabajador")
    print("(4)  Desbloquear trabajador")
    print("(5)  Listar trabajadores")
    print("(6)  Cerrar sesión\n")
    while True:
        sel = int(input("Seleccione su opción-> "))
        if(sel) in range(1, 7):
            print("Cargando...")
            time.sleep(1)
            os.system("cls")
            match(sel):
                case 1:
                    ingresoTrabajadores()
                case 2:
                    actualizarDatos()
                case 3:
                    eliminarEmpleado()
                case 4:
                    desbloquearUsuario()
                case 5:
                    verListaTrabajadores()
                case 6:
                    print("Cerrando sesión...")
                    time.sleep(1.5)
                    os.system("cls")
                    break

            break
        else:
            print("Opción incorrecta, por favor ingrese solo números")
            time.sleep(2)
            continue

def menuTrabajador():
    os.system("cls")
    sql = "SELECT RUT FROM empleado WHERE NOMBRE_USUARIO=(%s)"
    cursor.execute(sql, [user, ])
    result = cursor.fetchone()
    print("<-------------Bienvenido al menú Trabajador------>\n")
    print("Hola", result[0])
    print("\n(1)Modificar cargas familiares")
    print("(2)Cambiar contacto de emergencia")
    print("(3)Modificar datos personales")
    print("(4)Ver cargas familiares")
    print("(5)Ver contactos de emergencia")
    print("(6)Cerrar sesión\n")
    while True:
        sel = int(input("Seleccione su opción -> "))
        if(sel) in range(1, 7):
            print("Cargando...")
            time.sleep(1)
            os.system("cls")
            match(sel):
                case 1:
                    actualizarCargaFamiliar(result[0])
                case 2:                    
                    actualizarContactoEmergencia(result[0])
                case 3:
                    actualizarDatos(result[0])
                case 4:
                    # Ver cargas
                    rut = result[0]
                    sql = "select * from CARGA_FAMILIAR where ID_EMPLEADO = (%s)"
                    cursor.execute(sql,[rut,])
                    datos_carga = cursor.fetchall()
                    c = 0
                    for x in datos_carga:
                        c += 1
                        mydict.add(("#" + str(c)), ({
                            "Rut": x[0],
                            "Nombre": x[1],
                            "Apellido": x[2],
                            "Parentesco": x[3],
                            "Género": x[4]
                        }))
                    print("Cargas familiares: ")
                    print(json.dumps(mydict, indent=1))
                    a = input("Presione enter para volver al menú...")
                    menuTrabajador()
                case 5:
                    # Ver contacto
                    rut = result[0]
                    sql = "select * from CONTACT_EMERG where ID_EMPLEADO = (%s)"
                    cursor.execute(sql,[rut,])
                    datos_carga = cursor.fetchall()
                    c = 0
                    for x in datos_carga:
                        c += 1
                        mydict.add(("#" + str(c)), ({
                            "Rut": x[0],
                            "Nombre": x[1],
                            "Apellido": x[2],
                            "Teléfono": x[3],
                            "Relación": x[4]
                        }))
                    print("Contactos de emergencia: ")
                    print(json.dumps(mydict, indent=1))
                    a = input("Presione enter para volver al menú...")
                    menuTrabajador()
                case 6:
                    print("Cerrando sesión...")
                    time.sleep(1.5)
                    os.system("cls")
                    break
            break
        else:
            print("Opción incorrecta, por favor ingrese solo números")
            time.sleep(2)
            continue

logIn()
menuTipo()
asd = input(" - Fin del programa -")