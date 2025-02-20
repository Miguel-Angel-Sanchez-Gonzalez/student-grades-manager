def calculate_average(notes):
    return round(sum(notes) / len(notes), 1) 

def show_student(nombre):
    if nombre in students_manager:
        notes = students_manager[nombre]
        final_average = calculate_average(notes)
        print(f"Nombre del estudiante: {nombre}")
        print("Calificaciones:", notes)
        print(f"Promedio: {final_average}\n")
    else:
        print(f"\nEl estudiante {nombre} no se encuentra registrado\n")

students_manager = {}
option = 0
while option != 6: 
    try :
        print("1️⃣  Agregar un estudiante")
        print("2️⃣  Mostrar la lista de estudiantes")
        print("3️⃣  Buscar un estudiante")
        print("4️⃣  Actualizar las calificaciones")
        print("5️⃣  Eliminar un estudiante ")
        print("6️⃣  Salir del programa")
        option = int(input("\nIngrese un numero del 1 al 6 para seleccionar una opcion: "))
        if option < 1 or option > 6 :
            print("El numero ingresado no corresponde a ninguna opcion, intentalo de nuevo\n")
    except ValueError:
        print("Lo siento pero no ingresaste un valor numerico, intentalo de nuevo ")
        continue
    
    if option == 1 :
        print("\nSeleccionaste la opcion 1 - Agregar un estudiante \n")
        student_name = input("Ingresa el nombre del nuevo estudiante: ")
        try :
            first_grade = int(input("Ingresa su primer calificacion: "))
            second_grade = int(input("Ingresa su segunda calificacion: "))
            third_grade = int(input("Ingresa su tercer calificacion: "))
        except ValueError :
            print("\nNo capturaste correctamente las calificaciones, vuelve a comenzar\n")
            continue
        
        student_grades = [first_grade, second_grade, third_grade]
        students_manager[student_name] = student_grades
        print(f"\n ¡Perfecto el nuevo estudiante {student_name} se agrego al sistema!\n")
    elif option == 2 : 
        print("\nSeleccionaste la opcion 2 - Mostrar la lista de estudiantes\n")
        if not students_manager : 
            print("Parece que todavia no tienes ningun estudiante registrado.\n")   
        else :
            for i, (key, value) in enumerate(students_manager.items(), start=1) :
                print(f"Estudiante numero {i}")
                show_student(key)
    elif option == 3 : 
        print("\nSeleccionaste la opcion 3 - Buscar un estudiante\n")
        find_student = input("Ingresa el nombre del alumno que deseas buscar: ")
        if find_student in students_manager : 
            show_student(find_student)
        else : 
            print(f"El estudiante {find_student} no se encuentra registrado\n")  
    elif option == 4 :  
        print("\nSeleccionaste la opcion 4 - Actualizar las calificaciones")
        find_student = input("Ingresa el nombre del alumno para actualizar sus calificaciones: ")
        if find_student in students_manager : 
            print(f"Nombre del estudiante: {find_student}")
            try : 
                update_first_grade = int(input("Ingresa la primer calificacion: "))
                update_second_grade = int(input("Ingresa la segunda calificacion: "))
                update_third_grade = int(input("Ingresa la tercer calificacion: "))
            
            except ValueError :
                print("\nNo capturaste correctamente las calificaciones, vuelve a comenzar\n")
                continue
                
            update_grades = [update_first_grade,update_second_grade,update_third_grade]
            students_manager[find_student] = update_grades
            print(f"\n¡Perfecto se actualizaron las calificaciones de: {find_student}!\n")
        else : 
            print(f"\nEl estudiante {find_student} no se encuentra registrado\n") 
        
    elif option == 5 :
        print("\nSeleccionaste la opcion 5 - Eliminar un estudiante")
        delete_student = input("Ingresa el nombre del alumno que deseas dar de baja: ")
        if delete_student in students_manager : 
            del students_manager[delete_student]
            print(f"\n¡El estudiante {delete_student} se ha dado de baja exitosamente!\n")
        else : 
            print(f"El estudiante {delete_student} no se encuentra registrado\n")     