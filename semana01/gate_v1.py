puntaje_gate = 0.80
umbral = 0.75
calculo = umbral - puntaje_gate
if puntaje_gate >= umbral:
    print("PASS")
else:
    print("FAIL", calculo)