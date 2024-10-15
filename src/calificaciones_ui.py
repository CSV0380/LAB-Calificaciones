from calificaciones import *



def solicita_notas():

    nombre = input("Introduzca su nombre: \n")

    notas_teoria = []
    for i in range(1, 5):
        nota = input(f"Introduzca la nota del examen teórico {i} (- si no se ha presentado): ")
        if nota == "-":
            notas_teoria.append(0.0)  #Si no se ha presentado tiene un 0
        else:
            notas_teoria.append(float(nota))  

    
    notas_practico = []
    for i in range(1, 3):
        nota = input(f"Introduzca la nota del examen práctico {i} (- si no se ha presentado): ")
        if nota == "-":
            notas_practico.append(0.0)
        else:
            notas_practico.append(float(nota))

    return (nombre, tuple(notas_teoria), tuple(notas_practico)) #transformamos en tupla las listas de las notas



def mostrar_notas(datos):
    nombre, notas_teoria, notas_practico = datos
    media_teoria_cuatri1 = nota_teoria(notas_teoria[0], notas_teoria[1])
    media_teoria_cuatri2 = nota_teoria(notas_teoria[2], notas_teoria[3])

    #Aquí me conviene hacerlo por mi mismo en lugar de llamarla del otro archivo
    cuatrimestre1 = 0.2 * media_teoria_cuatri1 + 0.8 * notas_practico[0]
    cuatrimestre2 = 0.2 * media_teoria_cuatri2 + 0.8 * notas_practico[1]

    nota_final = (cuatrimestre1 + cuatrimestre2) / 2

    print(f"Hola, {nombre}.")
    print(f"--- Tus notas del primer cuatrimestre son:\n-Teoría: {round(media_teoria_cuatri1, 1)}\n-Práctica: {notas_practico[0]}\n-Cuatrimestre: {round(cuatrimestre1, 1)}")
    print(f"\n--- Tus notas del segundo cuatrimestre son:\n-Teoría: {round(media_teoria_cuatri2, 1)}\n-Práctica: {notas_practico[1]}\nCuatrimestre {round(cuatrimestre2, 1)}\n")
    if nota_final >= 5:
        print(f"###/ / / Tu nota final de la asignatura es: {round(nota_final, 1)} . HAS APROBADO, ENHORABUENA!!! \ \ \###")
    else: 
        print(f"###/ / / Tu nota final de la asignatura es: {round(nota_final, 1)} . G G \ \ \###")


if __name__ == '__main__':
    datos_estudiante = solicita_notas()
    mostrar_notas(datos_estudiante)