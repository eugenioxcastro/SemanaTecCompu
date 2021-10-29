from turtle import *

from freegames import vector

def info_alumnos():
    # agarra el lapiz
    up()
    # se va a esta posicion
    goto(0, 190)
    # escoje el color y lo escribe para cada almuno
    color('blue')
    write('Eugenio Castro A00830392', align='left', font=('Arial', 10, 'normal'))
    # nueva posicion para nuevo nombre
    goto(0, 170)
    color('pink')
    write('Elizabeth Naredo Betancourt A00830440', align='left', font=('Arial', 10, 'normal'))

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    # sube el lapiz
    up()
    # mueve a al posicion x, y
    goto(start.x, start.y)
    #baja el lapiz
    down()
    # empieza el llenado
    begin_fill()
    # se hacen los lados (4 lados)
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    # se acaba el llenado
    end_fill()


def circle2(start, end):
    "Draw circle from start to end."
    # sube el lapiz
    up()
    # mueve a al posicion x, y
    goto(start.x, start.y)
    d = end.x - start.x
    # baja el lapiz
    down()
    # empiza el llenado
    begin_fill()
    # se hace el circulo
    circle(d/2)
    end_fill()


def rectangle(start, end):
    "Draw rectangle from start to end."
    #levantamos el lápiz
    up()
    #vamos a primera coordenada (esquina superior izquierda) 
    goto(start.x, start.y)
    #indicamos que nos dirigimos a la izquierda
    setheading(0)
    #bajamos el lapiz para empezar a dibujar
    down()
    begin_fill()
    #vamos a la esquina superior derecha
    goto(end.x, start.y)
    #giramos 90 grados
    right(90)
    #vamos a la esquina inferior derecha
    goto(end.x, end.y)
    #giramos 90 grados
    right(90)
    #vamos a la esquina inferior izquierda
    goto(start.x, end.y)
    #giramos 90 grados
    right(90)
    #regresamos a la primera coordenada (esquina superior izquierda) 
    goto(start.x, start.y)
    #terminamos de dibujar
    end_fill()


def triangle(start, end):
    "Draw triangle from start to end."
    #levantamos lápiz
    up()
    #vamos a primera coordenada
    goto(start.x, start.y)
    #bajamos el lápiz para dibujar
    down()
    begin_fill()

    #por cada lado del triangulo 
    for count in range(3):
        #nos movemos la distancia entre la primera y segunda coordenada en x
        forward(end.x - start.x)
        #en un angulo de 120° hacia la izquierda, para terminar tener un triangulo con 3 ángulos de 60°
        left(120)

    #terminamos de dibujar
    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value

# indica cual figura (shape) - lo que va a dibujar - la función que se ejecuta
# start - vector del primer click o None
state = {'start': None, 'shape': line}
print(type(state))
# sets window to 420x420 pixels, in upper left screen.
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
writer = Turtle(visible=False)
info_alumnos()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
# color rosa, P para pink
# color nuevo usando funcion lambda
onkey(lambda: color('#f633ff'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
