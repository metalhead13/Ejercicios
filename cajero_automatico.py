saldo = int(input("Ingrese saldo: "))

print("\t :Menu") #\t para que el menu aparezca tabulado
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Digite la opcion de menu: ")) # Le pedimos al usuario que seleccione el menu
print() # Aqui finaliza el menu, segun las opciones elegidas el programa realizara las operacionesdatetime A combination of a date and a time.
#para que tome las opciones (sintaxis para crear menu) 

if opcion == 1:
    extra = float(input("Cuanto dinero desea ingresar: "))
    saldo += extra
    print(f"Su nuevo saldo es {saldo}")
elif opcion == 2:
    retiro = float(input("Cuanto dinero desea retirar: "))
    if retiro > saldo: 
        print("Fondos insuficientes")
    else:
        saldo -= retiro # aqui le estoy restando lo que se retiro
        print(f"El nuevo saldo es {saldo}")
elif opcion == 3:
    print(f"Su saldo actual es {saldo}")

    print("gracias por utilizar los servicios")

elif opcion == 4:
    print("Gracias por utilizar nuestros servicios")

else:
    print("Error de opcion")
