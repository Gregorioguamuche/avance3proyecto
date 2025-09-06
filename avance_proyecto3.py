# Lista global de cursos [(nombre, nota o promedio)]
cursos = []

# Opción 1: Mostrar cursos y permitir ingresar uno nuevo
def mostrar_cursos_y_notas():
    print("\n--- Cursos y Notas ---")
    if not cursos:
        print(" No hay cursos registrados.")
    else:
        for curso, nota in cursos:
            print(f" Curso: {curso} |  Nota: {nota}")

    # Preguntar si desea ingresar uno nuevo
    opcion = input("\n¿Desea ingresar un nuevo curso? (si/no): ").strip().lower()
    if opcion == 'si':
        nombre = input("Ingrese el nombre del curso: ")
        try:
            nota = float(input("Ingrese la nota del curso (0 a 100): "))
            if 0 <= nota <= 100:
                cursos.append((nombre, nota))
                print(" Curso registrado correctamente.")
            else:
                print(" La nota debe estar entre 0 y 100.")
        except ValueError:
            print(" Ingrese un número válido.")

# Opción 2: Actualizar nota de un curso
def actualizar_curso():
    nombre = input("Ingrese el nombre del curso a actualizar: ")
    for i, (curso, nota) in enumerate(cursos):
        if curso.lower() == nombre.lower():
            try:
                nueva_nota = float(input(f"Ingrese la nueva nota para {curso}: "))
                if 0 <= nueva_nota <= 100:
                    cursos[i] = (curso, nueva_nota)
                    print(" Nota actualizada.")
                else:
                    print(" Nota fuera de rango.")
            except ValueError:
                print(" Ingrese un número válido.")
            return
    print(" Curso no encontrado.")

# Opción 3: Registrar curso con UNA nota
def registrar_curso_simple():
    print("\n--- Registrar Curso ---")
    nombre = input("Ingrese el nombre del curso: ")
    try:
        nota = float(input("Ingrese la nota del curso (0 a 100): "))
        if 0 <= nota <= 100:
            cursos.append((nombre, nota))
            print(" Curso registrado correctamente.")
        else:
            print(" La nota debe estar entre 0 y 100.")
    except ValueError:
        print(" Ingrese un número válido.")

# Opción 4: Registrar curso con varias notas y calcular promedio
def registrar_curso_promedio():
    print("\n--- Registro y Promedio de Notas ---")
    suma = 0.0
    notas = []

    while True:
        try:
            cantidad = int(input("¿Cuántas notas desea ingresar? (mayor que 0): "))
            if cantidad > 0:
                break
            else:
                print(" Debe ser mayor que 0.")
        except ValueError:
            print(" Ingrese un número entero válido.")

    for i in range(1, cantidad + 1):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i} (entre 0 y 100): "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    suma += nota
                    break
                else:
                    print(" La nota debe estar entre 0 y 100.")
            except ValueError:
                print(" Ingrese un número válido.")

    promedio = suma / cantidad
    curso_nombre = input("Ingrese el nombre del curso relacionado con estas notas: ")
    cursos.append((curso_nombre, promedio))

    print("\n=) =) =)")
    print(f"El Promedio de las notas ingresadas para {curso_nombre} es: {promedio:.2f}")
    print("Saludos, fue un gusto")
    print("=) =) =)")

# Opción 5: Contar cursos aprobados y reprobados
def mostrar_cursos_aprobados_y_reprobados():
    aprobados = sum(1 for _, nota in cursos if nota >= 60)
    reprobados = len(cursos) - aprobados
    print(f" Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

# Opción 6: Calcular promedio general de todos los cursos
def calcular_promedio():
    if not cursos:
        print(" No hay cursos registrados.")
        return
    promedio_general = sum(nota for _, nota in cursos) / len(cursos)
    print(f" Promedio general de todos los cursos: {promedio_general:.2f}")

# Opción 7: Eliminar un curso
def eliminar_curso():
    nombre = input("Ingrese el nombre del curso a eliminar: ")
    for i, (curso, _) in enumerate(cursos):
        if curso.lower() == nombre.lower():
            cursos.pop(i)
            print("Curso eliminado correctamente.")
            return
    print("Curso no encontrado.")

# Opción 8: Buscar curso por nombre (búsqueda lineal)
def buscar_curso_lineal():
    nombre = input("Ingrese el nombre del curso a buscar: ")
    encontrado = False
    for curso, nota in cursos:
        if curso.lower() == nombre.lower():
            print(f"Curso encontrado: {curso} | Nota: {nota}")
            encontrado = True
            break
    if not encontrado:
        print(" Curso no encontrado.")

# === MENÚ PRINCIPAL ===
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Mostrar cursos y notas ")
    print("2. Actualizar nota de un curso")
    print("3. Registrar curso (una sola nota)")
    print("4. Registrar curso con varias notas (promedio)")
    print("5. Mostrar cursos aprobados y reprobados")
    print("6. Calcular promedio general")
    print("7. Eliminar un curso")
    print("8. Buscar curso por nombre (búsqueda lineal)")
    print("9. Salir")

    try:
        opcion = int(input("Seleccione una opción (1-9): "))
    except ValueError:
        print(" Opción inválida. Intente nuevamente.")
        continue

    if opcion == 1:
        mostrar_cursos_y_notas()
    elif opcion == 2:
        actualizar_curso()
    elif opcion == 3:
        registrar_curso_simple()
    elif opcion == 4:
        registrar_curso_promedio()
    elif opcion == 5:
        mostrar_cursos_aprobados_y_reprobados()
    elif opcion == 6:
        calcular_promedio()
    elif opcion == 7:
        eliminar_curso()
    elif opcion == 8:
        buscar_curso_lineal()
    elif opcion == 9:
        print(" Saliendo del sistema. ¡Gracias!")
        break
    else:
        print(" Esta Opción es inválida. Intente nuevamente.")
