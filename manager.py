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
    student_name = input("Ingresa el nombre del nuevo estudiante")
    first_grade = int(input("Ingresa su primer calificacion: "))
    second_grade = int(input("Ingresa su segunda calificacion: "))
    third_grade = int(input("Ingresa su tercer calificacion: "))
    student_grades = [first_grade, second_grade, third_grade]
    students_manager[student_name] = student_grades
    print(f"\n ¡Perfecto el nuevo estudiante {student_name} se agrego al sistema!\n")
  elif option == 2 : 
    print("Seleccionaste la opcion 2")
    print(students_manager)
  elif option == 3 : 
    print("Seleccionaste la opcion 3")
  elif option == 4 :  
    print("Seleccionaste la opcion 4")
  elif option == 5 :
    print("Seleccionaste la opcion 5") 
    