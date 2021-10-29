# Eugenio Castro Páez & Alexia Elizabeth Naredo

- Links a videos 

[Alexia Naredo](https://drive.google.com/file/d/17P2v-iUNqiCbSF7-OHdnFO4vaPnKnZXw/view?usp=sharing "Liga Drive")


---

```python
from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
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


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
```
# Alexia Naredo
Recorre cada elemento de la lista hide buscando que estén false, es decir destapados
```python
def unrevealed(hide):
    for i in hide:

        if (i != False):

            return

    print("Todos los cuatros estan destapados")
```

En tap, usamos un contador para cada vez que haya uno nuevo y llamamos a la función unrevealed

```python
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
```
# Eugenio
cambiamos la lista para hacerla mas entretenida para los niños, agregando animales
```python
tiles =  ["perro", "gato", "perico", "vaca", "pez payaso", "pez dorado", "serpiente", "mono", "araña", "lobo", "gorila", "lagarto", "leon", "oso", "elefante", "murcielago", "cebra", "panda", "sapo", "tigre", "caballo", "cerdo", "delfin", "venado", "zorro", "mapache", "koala", "hipopotamo", "pavorreal", "camello"] * 2
```
