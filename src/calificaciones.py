


def nota_teoria(nota1, nota2):

    #si es None
    if nota1 is None:
        nota1 = 0
    if nota2 is None:
        nota2 = 0

    #si no responde nada
    try:
        nota1 = float(nota1) #si es float se queda float
    except ValueError: #si no es float nota1 = 0
        nota1 = 0

    try:
        nota2 = float(nota2)
    except ValueError:
        nota2 = 0

    nota_media = (nota1 + nota2)/2

    if nota1 == 0 and nota2 == 0: #las condiciones se tratan por separado aunque esten en el mismo if
        return 0.0
    else: 
        return nota_media
    






def nota_cuatrimestre(teoricas, nota_practico):

    if len(teoricas) != 2:
        raise ValueError("La tupla de notas teóricas debe tener exactamente 2 valores.")
    
    nota1, nota2 = teoricas
    nota_teoria_media = nota_teoria(nota1, nota2)

    if nota_teoria_media < 4:
        return 0.0
    
    if nota_practico is None:
        nota_practico = 0
    try:
        nota_practico = float(nota_practico)
    except ValueError:
        nota_practico = 0

    nota_final = (0.2 * nota_teoria_media) + (0.8 * nota_practico)
    return nota_final






def nota_continua(notas_teoria, notas_practico):

    nota_cuatri1 = nota_cuatrimestre(notas_teoria[:2], notas_practico[0]) #notas_teoria[:2] primeras dos teoricas y primer práctico
    nota_cuatri2 = nota_cuatrimestre(notas_teoria[2:], notas_practico[1])

    #Si en alguno de los dos cuatrimestres la nota es inferior a 4, 
    #entonces la nota es el mínimo entre 4 y la nota media de los cuatris
    if nota_cuatri1 < 4 or nota_cuatri2 < 4:
        media_cuatris = (nota_cuatri1 + nota_cuatri2) / 2
        return min(4, media_cuatris)
    else:
        return (nota_cuatri1 + nota_cuatri2) / 2
    




