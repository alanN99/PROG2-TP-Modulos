import calculadora_indices as ci

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))

imc = ci.calcular_IMC(peso, altura)

print(f"{imc:.2f}")