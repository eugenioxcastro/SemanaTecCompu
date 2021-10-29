from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
movements = 0

#declaramos lista
lista_colores = ['black', 'pink', 'blue', 'green', 'yellow', 'orange', 'gray', 'white', 'cyan']
#escoge un color random para snake
color_snake = choice(lista_colores)
#elimina el color de snake para que no se repita
lista_colores.remove(color_snake)
#escoge un color random para food
color_food = choice(lista_colores)

def info_alumnos():
    # agarra el lapiz
    writer.up()
    # se va a esta posicion
    writer.goto(0, 150)
    # escoje el color y lo escribe para cada almuno
    writer.color('blue')
    writer.write('Eugenio Castro A00830392', align='left', font=('Arial', 10, 'normal'))
    # nueva posicion para nuevo nombre
    writer.goto(0, 130)
    writer.color('pink')
    writer.write('Elizabeth Naredo Betancourt A00830440', align='left', font=('Arial', 10, 'normal'))

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global movements
    "Move snake forward one segment."
    head = snake[-1].copy()
    #actualizar la variable aux head
    head.move(aim)
    movements = movements + 1
    #revisa que no esté dentro de los límites o si choca consigo misma
    if not inside(head) or head in snake:
        #dibuja el cuadrado rojo
        square(head.x, head.y, 9, 'red')
        #actualiza al dibujo
        update()
        #termina el juego 
        return

    #agrega la cabeza
    snake.append(head)
    
    #si head y food están en la misma posición (snake va a comer)
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    #lista de direcciones
    directions = [(30, 0), (-30, 0), (0, 30), (0, -30)]
    if movements % 5 == 0:
        #escoge una dirección random
        new_direction = choice(directions)
        #se suma a la posición actual
        food.x = food.x + new_direction[0]
        food.y = food.y + new_direction[1]
        # validacion para que la comida no quede dentro de la serpiente.
        while food in snake:
            new_direction = choice(directions)
            #se suma a la posición actual
            food.x = food.x + new_direction[0]
            food.y = food.y + new_direction[1]

    
    #verifica que no se salga de la ventana
    if not inside(food):
        food.x = 0
        food.y = 0


    clear()
    
    #dibuja la snake
    for body in snake:
        square(body.x, body.y, 9, color_snake)

    #dibuja la food
    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 200)

#crea la ventana
writer = Turtle(visible=False)
setup(420, 420, 370, 0)
#oculta el cursor
hideturtle()
#desactiva que se vayan dibujando los vectores
tracer(False)
#detecta los eventos del teclado
listen()
#llama a funciones especificas según la tecla
info_alumnos()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
