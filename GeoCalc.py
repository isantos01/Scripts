import math

# ========================
# Funciones de Cálculo
# ========================

# Cuadrado: área = lado^2, perímetro = 4 * lado
def calcular_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

# Círculo: área = π * radio^2, perímetro = 2 * π * radio
def calcular_circulo(radio):
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

# Rectángulo: se asume que los números son (l = valor_igual, L = valor_diferente)
# Área = l * L, perímetro = 2*(l+L)
def calcular_rectangulo(lado_corto, lado_largo):
    area = lado_corto * lado_largo
    perimetro = 2 * (lado_corto + lado_largo)
    return area, perimetro

# Rombo: supondremos que se da el valor de la diagonal mayor y menor
# Para fines de ejemplo, se usará: Área = (d1 * d2) / 2
# Aquí se puede asumir que uno de los números es la diagonal mayor y el otro es la menor.
def calcular_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor * diagonal_menor) / 2
    # Perímetro: si se conoce un lado; aproximamos asumiendo: lado = sqrt((d1/2)^2+(d2/2)^2)
    lado = math.sqrt((diagonal_mayor/2)**2 + (diagonal_menor/2)**2)
    perimetro = 4 * lado
    return area, perimetro

# Triángulo Escaleno: se usan los tres lados y la fórmula de Herón
def calcular_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimetro = a + b + c
    return area, perimetro

# Trapecio: para simplificar, se consideran los tres números como:
# bases b1 y b2, y lado oblicuo (se pediría en realidad la altura para área, 
# pero para fines de ejemplo asumiremos una fórmula simplificada)
def calcular_trapecio(b1, b2, lado):
    # Suponiendo que la altura se puede aproximar
    altura = math.sqrt(lado**2 - ((b2-b1)/2)**2) if abs(b2-b1)/2 < lado else 0
    area = ((b1 + b2)/2) * altura
    perimetro = b1 + b2 + 2 * lado
    return area, perimetro

# ========================
# Algoritmos de Ordenamiento
# ========================

def bubble_sort(lista, ascendente=True):
    n = len(lista)
    # Se hace una copia para no modificar la lista original
    arr = lista.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascendente and arr[j] > arr[j+1]) or (not ascendente and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ========================
# Algoritmo de Búsqueda (Búsqueda Secuencial)
# ========================
def busqueda_secuencial(lista, valor):
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
    return -1

# ========================
# Función Iterativa y Recursiva (Ejemplo: suma de lista)
# ========================
def suma_iterativa(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

def suma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + suma_recursiva(lista[1:])

# ========================
# Procesamiento de una terna de números
# ========================
def procesar_terna(a, b, c):
    resultados = {}
    if a == b and b == c:
        # Caso: tres números iguales
        resultados['cuadrado'] = calcular_cuadrado(a)
        resultados['circulo'] = calcular_circulo(a)
    elif a == b or a == c or b == c:
        # Caso: dos números iguales
        # Identificar cuál es el número igual y cuál es el diferente
        if a == b:
            igual, diferente = a, c
        elif a == c:
            igual, diferente = a, b
        else:
            igual, diferente = b, a
        resultados['rectangulo'] = calcular_rectangulo(igual, diferente)
        results_rombo = calcular_rombo(igual, diferente)
        resultados['rombo'] = results_rombo
    else:
        # Caso: tres números diferentes
        resultados['triangulo'] = calcular_triangulo(a, b, c)
        resultados['trapecio'] = calcular_trapecio(a, b, c)
    return resultados

# ========================
# Función Principal de Ejecución
# ========================
def main():
    # Listas para almacenar áreas y perímetros de cada figura (para efectos de estadísticas)
    lista_areas = []
    lista_perimetros = []
    
    # Contadores para ternas especiales
    contador_tres_iguales = 0
    contador_dos_iguales = 0
    
    # Ejemplo de datos de prueba (lista de ternas)
    ternas = [
        (5, 5, 5),     # tres iguales -> cuadrado y círculo
        (4, 4, 7),     # dos iguales -> rectángulo y rombo
        (3, 4, 5),     # tres diferentes -> triángulo y trapecio
    ]
    
    for terna in ternas:
        a, b, c = terna
        print(f"\nProcesando terna: {terna}")
        resultados = procesar_terna(a, b, c)
        
        # Mostrar resultados y acumular áreas y perímetros
        for figura, (area, perimetro) in resultados.items():
            print(f"Figura: {figura.capitalize()} | Área: {area:.2f} | Perímetro: {perimetro:.2f}")
            lista_areas.append(area)
            lista_perimetros.append(perimetro)
        
        # Actualización de contadores
        if a == b and b == c:
            contador_tres_iguales += 1
        elif a == b or a == c or b == c:
            contador_dos_iguales += 1
    
    # Operaciones adicionales:
    print("\n--- Estadísticas ---")
    print(f"Total de ternas con tres números iguales: {contador_tres_iguales}")
    print(f"Total de ternas con dos números iguales: {contador_dos_iguales}")
    
    # Ordenar áreas (ascendente) y perímetros (descendente)
    areas_ordenadas = bubble_sort(lista_areas, ascendente=True)
    perimetros_ordenados = bubble_sort(lista_perimetros, ascendente=False)
    print(f"Áreas ordenadas (ascendente): {areas_ordenadas}")
    print(f"Perímetros ordenados (descendente): {perimetros_ordenados}")
    
    # Promedio de áreas
    promedio_areas = suma_iterativa(lista_areas) / len(lista_areas) if lista_areas else 0
    print(f"Promedio de áreas: {promedio_areas:.2f}")
    
    # Mediana de perímetros: se ordena la lista y se extrae la mediana
    n = len(perimetros_ordenados)
    if n % 2 == 1:
        mediana = perimetros_ordenados[n//2]
    else:
        mediana = (perimetros_ordenados[n//2 - 1] + perimetros_ordenados[n//2]) / 2
    print(f"Mediana de perímetros: {mediana:.2f}")
    
    # Ejemplo de algoritmo de búsqueda:
    buscar_valor = areas_ordenadas[1]  # ejemplo: buscar el segundo valor del arreglo de áreas ordenadas
    posicion = busqueda_secuencial(areas_ordenadas, buscar_valor)
    print(f"\nBúsqueda: El área {buscar_valor:.2f} se encuentra en la posición {posicion} de la lista de áreas ordenadas.")
    
    # Ejemplo del uso de función recursiva:
    suma_total = suma_recursiva(lista_areas)
    print(f"Suma total de las áreas (usando función recursiva): {suma_total:.2f}")

if __name__ == "__main__":
    main()
