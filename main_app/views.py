from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'autos' : autos})

class Auto:
    def __init__(self, nombre, precio, modelo, color):
        self.nombre = nombre
        self.precio = precio
        self.modelo = modelo
        self.color = color

autos = [ 
    Auto('VW Jetta', "$145,000.00" , 2018, "Rojo"),
    Auto('Batplane', "$9,999,999.00" , 2020, "Negro oscuro"),
    Auto("Batimovil", "$876,400.00" , 1960, "Negro con acabados rojos"),
    Auto("Submarino amarillo", "$890,000.00", 1967, "Amarillo"),
    Auto("Rayo McQueen", "Auto de colección" , 2006, "Rojo"),
    Auto("Carro Mario Kart", "$700,000.00" , 2017, "Rojo")
]
