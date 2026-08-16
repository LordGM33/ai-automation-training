puntaje = 0.50
umbral = 0.75
diferencia = umbral - puntaje
if puntaje >= umbral:
    print("PASS")
elif diferencia < 0.05:
    print("FAIL — cerca del umbral, reintentar")
else:
    print("FAIL")