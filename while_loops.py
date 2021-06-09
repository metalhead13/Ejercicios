valor_actual = int(input("Valor: "))

while valor_actual >= 100:
        valor_actual = (int(input("Ingrese un numero menor a 100: ")))
        if  valor_actual == 100:
                print("El valor debe ser menor a 100!")
print(f" el valor actual es: {valor_actual}")