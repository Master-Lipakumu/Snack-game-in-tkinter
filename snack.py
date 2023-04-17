#coding:UTF-8


#MasterLipakumu

import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jeu de serpent")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.snake_coords = [(250, 250), (240, 250), (230, 250), (220, 250)]
        self.direction = "Right"
        self.food_coord = self.set_food()
        self.score = 0
        self.game_over = False
        self.draw_board()
        self.root.bind("<Key>", self.change_direction)
        self.move_snake()
        self.root.mainloop()

    def draw_board(self):
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", anchor=tk.NW)
        self.canvas.create_rectangle(self.food_coord[0], self.food_coord[1], self.food_coord[0] + 10,
                                      self.food_coord[1] + 10, fill="red")
        for coord in self.snake_coords:
            self.canvas.create_rectangle(coord[0], coord[1], coord[0] + 10, coord[1] + 10, fill="green")

    def move_snake(self):
        head = self.snake_coords[0]
        if self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 10, head[1])

        if new_head[0] < 0 or new_head[0] > 490 or new_head[1] < 0 or new_head[1] > 490:
            self.game_over = True
        elif new_head in self.snake_coords:
            self.game_over = True
        elif new_head == self.food_coord:
            self.score += 10
            self.snake_coords.insert(0, new_head)
            self.food_coord = self.set_food()
        else:
            self.snake_coords.pop()
            self.snake_coords.insert(0, new_head)

        self.canvas.delete("all")
        self.draw_board()
        if not self.game_over:
            self.root.after(100, self.move_snake)
        else:
            self.canvas.create_text(250, 250, text="Game Over!", font=("Helvetica", 30))

    def change_direction(self, event):
        if event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"

    def set_food(self):
        while True:
            x = random.randint(0, 49) * 10
            y = random.randint(0, 49) * 10
            if (x, y) not in self.snake_coords:
                return x, y



if __name__ == '__main__':
    SnakeGame()

# merci d'avoir choisi MasterLipakumu