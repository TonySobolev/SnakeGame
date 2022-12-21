from tkinter import *

import random


GAME_WIDTH = 700      #adding const for our standart setting
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = 'green'
FOOD_COLOR = 'red'
BACK_GROUND = 'black'

class Snake:


        def __init__(self):     #creating  basic elements of snake
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0,0])    #snake appear at top


            for x, y in self.coordinates:          #thats how each body element of snake will appear on board
                square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = 'snake')
                self.squares.append(square)






class Food:
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE      #our board is 700 units, and single elemtn is 50 units, so the possible places for our elements is 700 div 50 eq 14
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x,y,x+SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")    #adding food elemnt by type oval, and filling it with color


def next_turn(snake, food):

    x, y = snake.coordinates[0]    #head of snake
    if direction == 'up':
        y  -= SPACE_SIZE

    elif direction == 'down':
        y += SPACE_SIZE

    elif direction == 'left':
        x -= SPACE_SIZE

    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))    #updates coordinates of snake


    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)     #new graphic for snake head

    snake.squares.insert(0, square)    #update snake list of square, actually its length




    if x == food.coordinates[0] and y == food.coordinates[1]:     #checking if head of our snake actually hits the space of food
        global score
        score +=1
        label.config(text = 'Score:{}'.format(score))

        canvas.delete("food")          #deleting eaten food object
        food = Food()         #creating new food


    else:  #only delete if we dont eat

        del snake.coordinates[-1]   #deleting last element of snake, so its doent grow unlimitly

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:

            window.after(SPEED, next_turn, snake, food)

    #window.after(SPEED, next_turn, snake, food)  # calling nextturn funcion after time of our game(speed)


def change_direction(new_direction):


    global direction

    if new_direction =='left':              #changing direction, checking if new giving direction is not opposite to now direction
        if direction != 'right':
            direction = new_direction

    elif new_direction =='right':
        if direction != 'left':
            direction = new_direction

    elif new_direction =='up':
        if direction != 'down':
            direction = new_direction

    elif new_direction =='down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
        print('game over')

    if y < 0 or y >= GAME_HEIGHT:
        return True
        print('game over')

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print('Game Over')
            return True

    return False

def restart_game():
    global score
    global direction

    score = 0  # starting score ofc eq to 0
    direction = 'down'  # stating direction of moving
    canvas.delete(ALL)
    canvas.update()
    snake = Snake()
    food = Food()
    canvas.update()
    next_turn(snake, food)





def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 -35, font = ('Stolzl', 70), text = 'GAME OVER', fill = 'red', tag = 'gameover')
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2 +35, font=('Stolzl', 50), text='Score: {}'.format(score),
                       fill='red', tag='gameover')



window = Tk()
window.config(bg ='grey')
window.title('Snake game')  #naming of window
window.resizable(False,False)   #setting lock for window size

score = 0                 #starting score ofc eq to 0
direction = 'down'          #stating direction of moving

label = Label(window, text = 'Score:{}'.format(score), font = ('Stolzl, 40'), bg = 'grey') #adding score space to the top of window
label.pack()
button_restart =Button(window, text = 'Restart',command = restart_game)
button_restart.pack()

canvas = Canvas(window, bg = BACK_GROUND, height = GAME_HEIGHT, width = GAME_WIDTH)      #creating game zone with standart zone
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')    #by this we setting the size of window and at the same time center it in the middle of our screen

window.bind('<Left>', lambda event: change_direction('left'))         #binding to arrows key the functions of changing directions
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

window.bind('a', lambda event: change_direction('left'))         #binding to WASD key the functions of changing directions
window.bind('d', lambda event: change_direction('right'))
window.bind('w', lambda event: change_direction('up'))
window.bind('s', lambda event: change_direction('down'))

snake = Snake()

food = Food()

next_turn(snake,food)       #starting our elements

window.mainloop()