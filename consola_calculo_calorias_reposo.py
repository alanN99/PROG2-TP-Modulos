import calculadora_indices as ci

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en cm: "))
edad = int(input("Ingresa tu edad: "))
valor_genero = ci.obtener_valor_genero(str(input("Ingresa tu género (M/F): ").upper()))

tmb = ci.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)

print(f"{tmb:.2f} cal")