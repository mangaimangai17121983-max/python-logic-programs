import tkinter as tk
import random

window = tk.Tk()

canvas = tk.Canvas(window, width=700, height=500, bg="darkgreen")
canvas.pack()

player = canvas.create_rectangle(320,220,380,280, fill="blue")

zombies = []

score = 0

def move(event):

    if event.keysym == "Up":
        canvas.move(player, 0, -20)

    elif event.keysym == "Down":
        canvas.move(player, 0, 20)

    elif event.keysym == "Left":
        canvas.move(player, -20, 0)

    elif event.keysym == "Right":
        canvas.move(player, 20, 0)

window.bind("<Key>", move)

while True:

    if random.randint(1, 15) == 1:

        x = random.randint(0, 650)

        zombie = canvas.create_rectangle(x,0,x+40,40, fill="red")

        zombies.append(zombie)

    for zombie in zombies:

        canvas.move(zombie, 0, 5)

        z_pos = canvas.coords(zombie)
        p_pos = canvas.coords(player)

        if (p_pos[2] > z_pos[0] and
            p_pos[0] < z_pos[2] and
            p_pos[3] > z_pos[1]):

            canvas.create_text(350,250,text="GAME OVER",fill="white",font=("Arial",40))
            window.update()
            exit()

    score += 1

    window.title(f"Survival Score: {score}")

    window.update()
    canvas.after(50)

window.mainloop()





