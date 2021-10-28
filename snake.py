from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#declaramos lista
lista_colores = ['black', 'pink', 'blue', 'green', 'yellow', 'orange', 'gray', 'white', 'cyan']
#escoge un color random para snake
color_snake = choice(lista_colores)
#elimina el color de snake para que no se repita
lista_colores.remove(color_snake)
#escoge un color random para food
color_food = choice(lista_colores)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    #actualizar la variable aux head
    head.move(aim)

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

    clear()
    
    #dibuja la snake
    for body in snake:
        square(body.x, body.y, 9, color_snake)

    #dibuja la food
    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 200)

#crea la ventana
setup(420, 420, 370, 0)
#oculta el cursor
hideturtle()
#desactiva que se vayan dibujando los vectores
tracer(False)
#detecta los eventos del teclado
listen()
#llama a funciones especificas según la tecla
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
