from flask import Flask, request, jsonify
from flask_cors import CORS
from experta import *

class Producto(Fact):
    """Información del usuario"""
    pass

class MotorRecomendador(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.resultado = "Sin recomendación disponible"

    @Rule(Producto(interes='tecnología', presupuesto='alto'))
    def recomendar_laptop(self):
        self.resultado = "Laptop de gama alta"

    @Rule(Producto(interes='tecnología', presupuesto='medio'))
    def recomendar_celular(self):
        self.resultado = "Celular calidad-precio"

    @Rule(Producto(interes='tecnología', presupuesto='bajo'))
    def recomendar_otro(self):
        self.resultado = "Camara basica"

    @Rule(Producto(interes='hogar', presupuesto='alto'))
    def recomendar_smart(self):
        self.resultado = "Equipo inteligente de limpieza"

    @Rule(Producto(interes='hogar', presupuesto='medio'))
    def recomendar_aspiradora(self):
        self.resultado = "Aspiradora robot"

    @Rule(Producto(interes='hogar', presupuesto='bajo'))
    def recomendar_limpieza(self):
        self.resultado = "Juego de limpieza básico"

    @Rule(Producto(interes='deporte', presupuesto='alto'))
    def recomendar_maquinas(self):
        self.resultado = "Juego de maquinas de gimnasio"

    @Rule(Producto(interes='deporte', presupuesto='medio'))
    def recomendar_corredor(self):
        self.resultado = "Corredora de calidad"

    @Rule(Producto(interes='deporte', presupuesto='bajo'))
    def recomendar_juego(self):
        self.resultado = "Juego de pesas básicas"

app = Flask(__name__)
CORS(app)  # <-- permite peticiones desde el frontend

@app.route('/recomendar', methods=['POST'])
def recomendar():
    datos = request.json
    motor = MotorRecomendador()
    motor.reset()
    motor.declare(Producto(interes=datos['interes'], presupuesto=datos['presupuesto']))
    motor.run()
    return jsonify({'recomendacion': motor.resultado})

if __name__ == '__main__':
    app.run(debug=True)



