Performance Test Documentation – Module 1 PYHTON

OBJECTIVE:

The goal of this project is to develop a simple system for managing student information using basic Python concepts.

The system allows users to register, query, search, update, and delete students.

TOOLS USED:

Lists: to store multiple students.
Dictionaries: to represent each student.
Functions: to better organize the code.
Conditional statements: to make decisions and avoid common errors.
Loops: to repeat the process as needed.

DATA STRUCTURE:

LIST: All students are stored on a list:

estudiantes = []

DISCTIONARY: Each student is represented by a dictionary

estudiante = {
        "id":id_est,
        "name": nombre,
        "age": edad,
        "course": curso,
        "state": estado
    }

SYSTEM FUNCTIONS:

REGISTER STUDENT: def registrar():
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

CONSULT STUDENTS: def consultar ():
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

FIND STUDENTS: def buscar ():
    print("--- Search student ---")
    dato = input("ENTER YOUR ID OR NAME: ")

    encontrado = False

    for est in estudiantes:
        if est["id"] == dato or est["name"] == dato:
            print("✅ FOUND")
            print(est)
            encontrado = True

        if not encontrado:
            print("❌ NOT FOUND")

UPDATE STUDENTS: def actualizar ():
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

DELETE STUDENT: def eliminar ():
    print("\--- REMOVE STUDENT ---")
    id_buscar = input("Enter your ID: ")

    for est in estudiantes:
        if est["id"] == id_buscar:
            estudiantes.remove(est)
            print("🗑️ Deleted")
            return
        
        print("❌ NOT FOUND")

VALIDATIONS:

The system includes basic validations such as:
- Preventing duplicate IDs.

- Verifying that the age is numeric.

- Displaying messages when a student cannot be found.

CONCLUSION:

This project demonstrates how basic programming concepts can be used to build a functional system.
It allows you to understand how to organize information using lists and dictionaries, as well as how to control program flow with loops and conditionals.
