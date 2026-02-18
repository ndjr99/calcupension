def calcular_tasa_reemplazo(tipo, ibl, semanas, genero, edad, pcl):
    smmlv = 1_750_905

    if ibl <= 0:
        return "Error: el IBL debe ser mayor a 0"
    
    if tipo == "Vejez" and semanas < 1300:
        return "Error: las semanas cotizadas deeben ser mayores o iguales a 1300"

    if tipo == "Vejez" and genero == "Hombre" and edad < 62:
        return "Error: debe tener al menos 62 años para pensionarse"

    if tipo == "Vejez" and genero == "Mujer" and edad < 57:
        return "Error: debe tener al menos 57 años para pensionarse"

    if tipo == "Vejez":
        if (genero == "Hombre" and edad >= 62) or (genero == "Mujer" and edad >= 57):
            
            r = 65.50 - (ibl / smmlv) * 0.50
            if semanas > 1300:
                incremento = (semanas - 1300) / 50 * 1.5
            else:
                incremento = 0
            tasa_total = r + incremento
            if tasa_total > 80:
                tasa_total = 80
            elif tasa_total < 55:
                tasa_total = 55

            return tasa_total
    
    elif tipo == "Sobreviviente":
        r = 45
        if semanas > 500:
            incremento = (semanas - 500) / 50 * 2
        else:
            incremento = 0
        tasa_total = r + incremento
        if tasa_total > 75:
            tasa_total = 75

        return tasa_total
    
    elif tipo == "Invalidez":
        if pcl > 50 and pcl <= 66:
            r = 45
            if semanas > 500:
                incremento = (semanas - 500) / 50 * 1.5
            else:
                incremento = 0

        elif pcl > 66:
            r = 54
            if semanas > 500:
                incremento = (semanas - 500) / 50 * 2
            else:
                incremento = 0
        tasa_total = r + incremento
        if tasa_total > 75:
            tasa_total = 75
        elif tasa_total < 45:
            tasa_total = 45

        return tasa_total

def calcular_pension(tasa_total, ibl, tipo):
    smmlv = 1_750_905
    mesada = (tasa_total / 100) * ibl
    if tipo == "Vejez" and mesada < smmlv:
        mesada = smmlv
    return mesada