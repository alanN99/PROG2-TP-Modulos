import calculadora_indices as ci

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))
edad = int(input("Ingresa tu edad: "))
valor_genero = ci.obtener_valor_genero(str(input("Ingresa tu género (M/F): ").upper()))

print("\nSelecciona tu nivel de actividad física:")
print("1 - Poco o ningún ejercicio")
print("2 - Ejercicio ligero (1 a 3 días por semana)")
print("3 - Ejercicio moderado (3 a 5 días por semana)")
print("4 - Deportista (6-7 días por semana)")
print("5 - Atleta (entrenamientos mañana y tarde)")

valor_actividad = ci.obtener_valor_actividad(int(input("Opción: ")))

calorias = ci.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)

print(f"{calorias:.2f} cal")