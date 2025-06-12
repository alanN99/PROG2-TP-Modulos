class Persona:
    def __init__(self, peso:float,altura:float, edad:int = None, valor_genero:str = None):
        self.peso = peso
        self.altura = altura        
        self.edad = edad
        self.valor_genero = valor_genero.upper()
        
        if self.valor_genero == "M":
            self.valor_genero = 10.8
        elif self.valor_genero == "F":
            self.valor_genero = 0
        else:
            raise ValueError("Género inválido. Ingrese M o F según corresponda.")

def obtener_valor_genero(genero: str):
    if genero == "M":
        valor_genero = 10.8
    elif genero == "F":
        valor_genero = 0
    else:
        raise ValueError("Género inválido. Ingrese M o F según corresponda.")
    return valor_genero

def obtener_valor_actividad(nivel: int):
    if nivel == 1:
        valor_actividad = 1.2
    elif nivel == 2:
        valor_actividad = 1.375
    elif nivel == 3:
        valor_actividad = 1.55
    elif nivel == 4:
        valor_actividad = 1.72
    elif nivel == 5:
        valor_actividad = 1.9
    else:
        raise ValueError("Valor inválido. Ingrese alguno de los valores enumerados.")
    return valor_actividad

def calcular_IMC(peso: float, altura: float):
    return peso / (altura**2)

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float):
    imc = calcular_IMC(peso, altura)
    gc = (1.2 * imc) + (0.23 * edad) - 5.4 - valor_genero
    return gc
    
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: float):
    return (10*peso) + (6.25*altura) - (5*edad) + valor_genero
        
def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)    
    return tmb * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float):
    tmb_actividad = calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    rango_inferior = tmb_actividad * 0.80
    rango_superior = tmb_actividad * 0.85
    return rango_inferior, rango_superior
    
    