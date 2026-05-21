import tkinter as tk
import random

window = tk.Tk()

canvas = tk.Canvas(window, width=800, height=300, bg="white")
canvas.pack()

dino = canvas.create_rectangle(50,200,100,250, fill="green")

obstacles = []

jumping = False

def jump(event):

    global jumping

    if not jumping:

        jumping = True

        for i in range(20):
            canvas.move(dino, 0, -5)
            window.update()
            canvas.after(20)

        for i in range(20):
            canvas.move(dino, 0, 5)
            window.update()
            canvas.after(20)

        jumping = False

window.bind("<space>", jump)

while True:

    if random.randint(1, 30) == 1:
        obstacle = canvas.create_rectangle(800,220,830,250, fill="red")
        obstacles.append(obstacle)

    for obstacle in obstacles:

        canvas.move(obstacle, -10, 0)

        dino_pos = canvas.coords(dino)
        obs_pos = canvas.coords(obstacle)

        if (dino_pos[2] > obs_pos[0] and
            dino_pos[0] < obs_pos[2] and
            dino_pos[3] > obs_pos[1]):

            canvas.create_text(400,150,text="GAME OVER",font=("Arial",30))
            window.update()
            exit()

    window.update()
    canvas.after(30)

window.mainloop()

