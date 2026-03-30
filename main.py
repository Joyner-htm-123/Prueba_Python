#LISTA PRINCIPAL
from numpy import rint


estudiantes = []

#FUNCIONES

def menu ():
    option = ""

    while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6":
        print("==== STUDENT SYSTEM ====")
        print("1. Register")
        print("2. Consult")
        print("3. Search")
        print("4. Updated")
        print("5. Eliminate")
        print("6. Go out")

    option = input("Select: ")

    if option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6":
        print("ENTER A VALID NUMBER; PLEASE TRY AGAIN")
        return option

def registrar():
    print("\n--- REGISTER STUDENT ---")

    id_est = input("ID: ")

    #VALIDAR EL ID UNICO
    for est in estudiantes:
        if est["ID"] == id_est:
            print("❌ THAT ALREADY EXISTS")
            return
        
    nombre = input("Name: ")
    
    try:
        edad = print(input("Age: "))
    except:
        print("❌ INVALID OPTION")
        return
    
    curso = input("course: ")
    estado = input("Estado (Activo/Inactivo)")

    estudiante = {
        "id":id_est,
        "name": nombre,
        "age": edad,
        "course": curso,
        "state": estado
    }

    estudiantes.append(estudiante)
    print("✅ REGISTERED STUDENT")

def consultar ():
    print("--- \STUDENT LIST ---")

    if len(estudiantes) == 0:
        print("THERE ARE NOT STUDENT")
        return
    
    for est in estudiantes:
        print("-------------------")
        print("ID:", est["id"])
        print("Name:", est["name"])
        print("Age:", est["age"])
        print("Course:", est["course"])
        print("State:", est["state"])

def buscar ():
    print("--- Search student ---")
    dato = input("Ingrese ID o nombre: ")

    encontrado = False

    for est in estudiantes:
        if est["id"] == dato or est["name"] == dato:
            print("✅ FOUND")
            print(est)
            encontrado = True

        if not encontrado:
            print("❌ NOT FOUND")

def actualizar ():
    print("\--- UPDATE STUDENT ---")
    id_buscar = input("Enter your ID: ")

    for est in estudiantes:
        if est["id"] == id_buscar:
            est["name"] = input("New name: ")

            try:
                est["age"] = int(input("New age"))
            except:
                print("❌ INVALID AGE")
                return
            
            est["course"] = input("New course: ")
            est["state"] = input("New state: ")

            print("✅ UPDATED")
            return
        
        print("❌ NOT FOUND")

def eliminar ():
    print("\--- REMOVE STUDENT ---")
    id_buscar = input("Enter your ID: ")

    for est in estudiantes:
        if est["id"] == id_buscar:
            estudiantes.remove(est)
            print("🗑️ Deleted")
            return
        
        print("❌ NOT FOUND")
#MENU PRINCIPAL

opcion = ""

while opcion != "6":
    print("==== STUDENT SYSTEM ====")
    print("1. Register")
    print("2. Consult")
    print("3. Search")
    print("4. Updated")
    print("5. Eliminate")
    print("6. Go out")

    opcion = input("Select: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        consultar ()
    elif opcion == "3":
        buscar ()
    elif opcion == "4":
        actualizar ()
    elif opcion == "5":
        eliminar()
    elif opcion == "6":
        print("👋 FIN DEL PROGRAMA")
    
    else:
        "❌ INVALID OPCTION, PLEASE ENTER AGAIN"