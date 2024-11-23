import tkinter as tk
import random

# 游戏设置
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
SNAKE_COLOR = 'green'
FOOD_COLOR = 'red'
BACKGROUND_COLOR = 'black'

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("贪吃蛇游戏")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
        self.canvas.pack()
        self.snake = [(GRID_SIZE, GRID_SIZE), (GRID_SIZE * 2, GRID_SIZE)]
        self.food = None
        self.direction = 'Right'
        self.running = True
        self.place_food()
        self.draw_snake()
        self.root.bind("<KeyPress>", self.change_direction)
        self.move_snake()

    def place_food(self):
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.food = (x, y)
        self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=FOOD_COLOR)

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR, tags="snake")

    def move_snake(self):
        if not self.running:
            return

        head_x, head_y = self.snake[-1]
        if self.direction == 'Up':
            head_y -= GRID_SIZE
        elif self.direction == 'Down':
            head_y += GRID_SIZE
        elif self.direction == 'Left':
            head_x -= GRID_SIZE
        elif self.direction == 'Right':
            head_x += GRID_SIZE

        new_head = (head_x, head_y)

        if (new_head in self.snake or
                head_x < 0 or head_y < 0 or
                head_x >= WIDTH or head_y >= HEIGHT):
            self.running = False
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="游戏结束", fill="white", font=('Arial', 24))
            return

        self.snake.append(new_head)

        if new_head == self.food:
            self.place_food()
        else:
            self.snake.pop(0)

        self.draw_snake()
        self.root.after(100, self.move_snake)

    def change_direction(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.direction = event.keysym

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
