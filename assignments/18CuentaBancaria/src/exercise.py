def main():
 # escribe tu código abajo de esta línea
   saldomes= float(input("Dame el saldo del mes anterior: "))
   ingresos= float(input("Dame el ingreso: "))
   egresos= float(input("Dame el egreso: "))
   numcheques= int(input("Dame el numero de cheques: "))
   cheque= numcheques*13
   descuento= 9.46875
   saldofinal= (saldomes-cheque)+(ingresos-egresos)
   saldomes= saldofinal-descuento
   print("El saldo final de la cuenta es:",saldomes)

if __name__ == '__main__':
    main()
