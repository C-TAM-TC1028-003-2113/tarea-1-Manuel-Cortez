def main():
 # escribe tu código abajo de esta línea

 n=int(input("Dame la cantidad de juegos nuevos: "))
 u=int(input("Dame la cantidad de juegos usados: "))
 juegosusados= u*350
 juegosnuevos= n*1000
 totaldecompra=juegosnuevos+juegosusados
 print("El total de la compra es:",totaldecompra)

if __name__ == '__main__':
    main()
