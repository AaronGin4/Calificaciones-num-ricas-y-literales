def asignar_calificacion(calificacion_numerica):
    if calificacion_numerica > 9.0:
        calificacion_literal = "A Excelente"
    else:
        if calificacion_numerica > 8.0:
            calificacion_literal = "B Muy bien"
        else:
            if calificacion_numerica >= 7.5:
                calificacion_literal = "C Bien"
            else:
                calificacion_literal = "R Reprobado"
    return calificacion_literal

# Ejemplo de uso
calificacion = float(input("Ingrese la calificación numérica: "))
calificacion_literal = asignar_calificacion(calificacion)
print("Calificación literal asignada:", calificacion_literal)