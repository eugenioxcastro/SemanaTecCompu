# SemanaTecCompu
Repositorio para mi clase de herramientas computacionales.

- Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí,
pero al azar ()

```python
#declaramos lista
lista_colores = ['black', 'pink', 'blue', 'green', 'yellow', 'orange', 'gray', 'white', 'cyan']
#escoge un color random para snake
color_snake = choice(lista_colores)
#elimina el color de snake para que no se repita
lista_colores.remove(color_snake)
#escoge un color random para food
color_food = choice(lista_colores)
```

En función move()

```python
#dibuja la snake
    for body in snake:
        square(body.x, body.y, 9, color_snake)

#dibuja la food
square(food.x, food.y, 9, color_food)
```
