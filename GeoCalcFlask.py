from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

# Funciones de cálculo con estructura uniforme (diccionarios)
def calcular_cuadrado(lado):
    return {'area': lado**2, 'perimetro': 4*lado, 'valido': True}

def calcular_circulo(radio):
    return {'area': math.pi * radio**2, 'perimetro': 2 * math.pi * radio, 'valido': True}

def calcular_rectangulo(lado_corto, lado_largo):
    return {'area': lado_corto * lado_largo, 'perimetro': 2 * (lado_corto + lado_largo), 'valido': True}

def calcular_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor * diagonal_menor) / 2
    lado = math.sqrt((diagonal_mayor/2)**2 + (diagonal_menor/2)**2)
    return {'area': area, 'perimetro': 4 * lado, 'valido': True}

def calcular_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return {'area': area, 'perimetro': a + b + c, 'valido': True}
    else:
        return {'valido': False}

def calcular_trapecio(b1, b2, lado):
    if abs(b2 - b1) / 2 < lado:
        altura = math.sqrt(lado**2 - ((b2 - b1)/2)**2)
        area = ((b1 + b2) / 2) * altura
        perimetro = b1 + b2 + 2 * lado
        return {'area': area, 'perimetro': perimetro, 'valido': True}
    else:
        return {'valido': False}

def procesar_terna(a, b, c):
    resultados = {}
    if a == b and b == c:
        resultados['cuadrado'] = calcular_cuadrado(a)
        resultados['circulo'] = calcular_circulo(a)
    elif a == b or a == c or b == c:
        if a == b:
            igual, diferente = a, c
        elif a == c:
            igual, diferente = a, b
        else:
            igual, diferente = b, a
        resultados['rectangulo'] = calcular_rectangulo(igual, diferente)
        resultados['rombo'] = calcular_rombo(igual, diferente)
    else:
        resultados['triangulo'] = calcular_triangulo(a, b, c)
        resultados['trapecio'] = calcular_trapecio(a, b, c)
    return resultados

# Plantilla HTML con estilo y validaciones
html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Procesamiento Geométrico</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 30px;
            background-color: #f4f4f4;
        }
        h1, h2 {
            color: #333;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        input[type="text"], input[type="submit"] {
            padding: 10px;
            margin-top: 10px;
            font-size: 16px;
        }
        ul {
            list-style: none;
            padding-left: 0;
        }
        li {
            background: white;
            padding: 10px;
            margin-bottom: 8px;
            border-radius: 5px;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
        }
        .invalido {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Procesamiento de Ternas de Números</h1>
    <form action="/procesar" method="post">
        <label for="terna">Ingrese tres números separados por comas (ej: 3,4,5):</label><br>
        <input type="text" id="terna" name="terna" placeholder="3,4,5" required>
        <br><br>
        <input type="submit" value="Procesar">
    </form>
    {% if resultados %}
        <h2>Resultados:</h2>
        <ul>
        {% for figura, datos in resultados.items() %}
            {% if not datos.valido %}
                <li class="invalido"><strong>{{ figura.capitalize() }}:</strong> Los valores no permiten formar una figura válida.</li>
            {% else %}
                <li><strong>{{ figura.capitalize() }}:</strong> Área = {{ datos.area|round(2) }}, Perímetro = {{ datos.perimetro|round(2) }}</li>
            {% endif %}
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def inicio():
    return render_template_string(html_template)

@app.route('/procesar', methods=['POST'])
def procesar():
    terna_str = request.form.get("terna")
    try:
        numeros = [float(x.strip()) for x in terna_str.split(',')]
        if len(numeros) != 3:
            raise ValueError("Se requieren tres números.")
    except Exception as e:
        return f"Error en la entrada: {e}"

    a, b, c = numeros
    resultados = procesar_terna(a, b, c)
    return render_template_string(html_template, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
