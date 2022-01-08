import turtle, time , random

WIDTH, HEIGHT = 600, 600
COLORS = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow', 'black', 'brown', 'purple', 'pink']

def get_number_of_racers(): # Asks user for a number of racers
    racers = 0
    while True:
        racers = input('Enter the number of racers (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not valid... Try again')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number of racers is not between 2 and 10. Try Again.')

def race(colors):
    racers = create_racers(colors)

    while True:
        for racer in racers:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[racers.index(racer)]

def create_racers(colors):
    racers = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('triangle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        racers.append(racer)

    return racers

def init_racer():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Race Window")

participants = get_number_of_racers()
init_racer()

random.shuffle(COLORS)
colors = COLORS[:participants]

winner = race(colors)
print('The winner is the racer with color:', winner)
time.sleep(5)


