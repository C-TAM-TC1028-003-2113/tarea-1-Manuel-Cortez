def main():
    # escribe tu código abajo de esta línea
    pass
msj=int(input("Dame el número de mensajes: "))
m=float(input("Dame el número de megas: "))
minutos=int(input("Dame el número de minutos: "))
mensajes=0.80*msj
megas=0.80*m
minu=0.80*minutos
costomensual=mensajes+megas+minu
print("El costo mensual es: ",costomensual)

if __name__ == '__main__':
    main()
