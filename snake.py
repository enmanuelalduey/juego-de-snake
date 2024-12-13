import turtle
import time
import random

# Configuración inicial
display = 0.1
cuerpo_serpiente = []
score = 0
high_score = 0

# Crear ventana
ventana = turtle.Screen()
ventana.title("Juego de Snake")
ventana.bgcolor("light green")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("Green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Texto de puntaje
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: 0       High Score: 0", align="center", font=("arial", 24))

# Funciones de movimiento
def movimiento():
    if cabeza.direction == "arriba":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "abajo":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "derecha":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    if cabeza.direction == "izquierda":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

def dir_up():
    if cabeza.direction != "abajo":
        cabeza.direction = "arriba"

def dir_down():
    if cabeza.direction != "arriba":
        cabeza.direction = "abajo"

def dir_right():
    if cabeza.direction != "izquierda":
        cabeza.direction = "derecha"

def dir_left():
    if cabeza.direction != "derecha":
        cabeza.direction = "izquierda"

# Conectar teclado
ventana.listen()
ventana.onkeypress(dir_up, "w")
ventana.onkeypress(dir_down, "s")
ventana.onkeypress(dir_right, "d")
ventana.onkeypress(dir_left, "a")

# Bucle principal del juego
while True:
    ventana.update()

    # Colisiones con la ventana
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        
        for segmento in cuerpo_serpiente:
            segmento.goto(1000, 1000)

        cuerpo_serpiente.clear()

        score = 0
        text.clear()
        text.write(f"Score: {score}       High Score: {high_score}", align="center", font=("arial", 24))

    # Colisiones de la cabeza con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("yellow")
        nuevo_segmento.penup()
        cuerpo_serpiente.append(nuevo_segmento)

        score += 10
        if score > high_score:
            high_score = score

        text.clear()
        text.write(f"Score: {score}       High Score: {high_score}", align="center", font=("arial", 24))

    # Mover el cuerpo de la serpiente
    total_segmentos = len(cuerpo_serpiente)
    for i in range(total_segmentos - 1, 0, -1):
        x = cuerpo_serpiente[i - 1].xcor()
        y = cuerpo_serpiente[i - 1].ycor()
        cuerpo_serpiente[i].goto(x, y)

    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo_serpiente[0].goto(x, y)

    movimiento()

    # Colisiones con su propio cuerpo
    for segmento in cuerpo_serpiente:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for segmento in cuerpo_serpiente:
                segmento.goto(1000, 1000)

            cuerpo_serpiente.clear()
            score = 0
            text.clear()
            text.write(f"Score: {score}       High Score: {high_score}", align="center", font=("arial", 24))

    time.sleep(display)

# Para que no se cierre la ventana
turtle.done()
