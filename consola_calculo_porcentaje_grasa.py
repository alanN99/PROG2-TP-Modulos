import calculadora_indices as ci

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))
edad = int(input("Ingresa tu edad: "))
valor_genero = ci.obtener_valor_genero(str(input("Ingresa tu género (M/F): ").upper()))
grasa = ci.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

print(f"{grasa:.2f}%")