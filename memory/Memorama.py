from random import *
from turtle import *

from freegames import path

contador = 0
car = path('car.gif')
tiles =  ["perro", "gato", "perico", "vaca", "pez payaso", "pez dorado", "serpiente", "mono", "araña", "lobo", "gorila", "lagarto", "leon", "oso", "elefante", "murcielago", "cebra", "panda", "sapo", "tigre", "caballo", "cerdo", "delfin", "venado", "zorro", "mapache", "koala", "hipopotamo", "pavorreal", "camello"] * 2
state = {'mark': None}
#lista indica la cantidad de cartas escondidas
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('green', 'pink')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def unrevealed(hide):
    for i in hide:
        if (i != False):
            return
    print("Todos los cuatros estan destapados")

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    
    #contador de taps como atributo de función
    tap.counter += 1
    print("Número de taps: ", tap.counter)

    #obtiene el indice sobre el cual se dio click
    spot = index(x, y)
    #obtiene el estado actual del memorama
    mark = state['mark']
    
    # verifica si son pares o no para dejar de mostrar el recuadro o no
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
    unrevealed(hide)

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    
    #ciclo que dibuja las cartas que estan ocultas
    # iniciando en la esquina inferior izquierda 
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    
        
    # mark indica si tenemos una carta visible o no
    mark = state['mark']
            

    # si fue seleccionada y no esta visible escribe el valor de la carta
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

# desordena las tiles
shuffle(tiles)
# abre la ventana del memorama
setup(420, 420, 370, 0)
# añade una imagen al canvas
addshape(car)
# oculta la tortuga
hideturtle()
# oculta el trasado del dibujo
tracer(False)
#inicializando contador
tap.counter = 0

# activar la funcion que atiende los eventos del mouse
onscreenclick(tap)
draw()
done()
