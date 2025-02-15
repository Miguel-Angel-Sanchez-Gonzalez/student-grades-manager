students_manager = {}
option = 0
while option != 6: 
  try :
    print("1️⃣  Agregar un estudiante")
    print("2️⃣  Mostrar la lista de estudiantes")
    print("3️⃣  Buscar un estudiante ")
    print("4️⃣  Actualizar las calificaciones")
    print("5️⃣  Eliminar un estudiante ")
    print("6️⃣  Salir del programa")
    option = int(input("\nIngrese un numero del 1 al 6 para seleccionar una opcion: "))
    if option < 1 or option > 6 :
      print("Parece que el numero ingresado no corresponde a ninguna de las opciones, intentalo de nuevo\n")
  except ValueError:
    print("Lo siento pero no ingresaste un valor numerico, intentalo de nuevo ")
    continue
  
  if option == 1 :
    print("\nSeleccionaste la opcion 1 - Agregar un estudiante \n")
    student_name = input("Ingresa el nombre del nuevo estudiante: ")
    first_grade = int(input("Ingresa su primer calificacion: "))
    second_grade = int(input("Ingresa su segunda calificacion: "))
    third_grade = int(input("Ingresa su tercer calificacion: "))
    student_grades = [first_grade, second_grade, third_grade]
    students_manager[student_name] = student_grades
    print(f"\n ¡Perfecto el nuevo estudiante {student_name} se agrego al sistema!\n")
  elif option == 2 : 
    print("\nSeleccionaste la opcion 2")
    if not students_manager : 
      print("Parece que todavia no tienes ningun estudiante registrado.\n")   
    else :
      for i, (key, value) in enumerate(students_manager.items(), start=1) :
        print(f"Estudiante numero {i}, nombre: {key}")
        average = (value[0] + value[1] + value[2]) / 3
        print(f"Calificacion 1️⃣ :  {value[0]}")
        print(f"Calificacion 2️⃣ :  {value[1]}")
        print(f"Calificacion 3️⃣ :  {value[2]}")
        print(f"El promedio del alumno es de {average}\n")
  elif option == 3 : 
    print("\nSeleccionaste la opcion 3")
  elif option == 4 :  
    print("\nSeleccionaste la opcion 4")
  elif option == 5 :
    print("\nSeleccionaste la opcion 5") 
    