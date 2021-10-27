# SemanaTecCompu
Repositorio para mi clase de herramientas computacionales.

# Codigo hecho por Eugenio Castro

- nombres de los alumnos
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
    write('NOMBRE', align='left', font=('Arial', 10, 'normal'))
    
- circulo
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
    
- nuevo color
# color rosa, P para pink
# color nuevo usando funcion lambda
onkey(lambda: color('#f633ff'), 'P')

- Este codigo es bastante sencillo pero el proposito de la actividad es practicar a usar github y trabajar en equipo
