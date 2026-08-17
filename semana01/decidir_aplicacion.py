tarifa = 45
pago_verificado = True
gasto_total_cliente = 1500
horas_semanales = 30
if not pago_verificado or gasto_total_cliente < 1000:
    print("NO APLICAR — cliente no confiable")
else:
    if tarifa < 20:                 #20 pasa al rango siguiente
        print("tarifa baja")
    elif tarifa <= 40:              #el rango de tarifa aceptable es de 20 a 40
        print("tarifa aceptable")
    else:
        print("tarifa buena")
    if  horas_semanales >= 30:
        print("dedicación alta")
    else:
        print("dedicación parcial")
    if tarifa > 40 and horas_semanales >= 30:
        print("APLICAR — prioridad máxima")
    elif tarifa >= 20:
        print("APLICAR — prioridad normal")
    else:
        print("NO APLICAR — no vale los connects")