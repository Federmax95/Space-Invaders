import tkinter as tk
from PIL import ImageTk, Image
from src import enemy as en
from src.utils import resource_path

class Player:
    def __init__(self, master):
        player_image_path = resource_path("Utils/player.png")
        player_image = Image.open(player_image_path)
        player_image = player_image.resize((30, 30))
        self.canvas = tk.Canvas(master, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        background_path = resource_path("Utils/background.jpg")
        background_image = Image.open(background_path)
        bg_img = ImageTk.PhotoImage(background_image)
        self.canvas.create_image(0, 0, anchor='nw', image=bg_img)
        self.canvas.image = bg_img
        

        self.player_img = ImageTk.PhotoImage(player_image)
        self.player = self.canvas.create_image(185, 250, image=self.player_img)
        self.bullets = []
        master.bind('<KeyPress>', self.move)
        master.bind('<space>', self.shoot)
        self.restart_button = None

    def move(self, event):
        if event.char == "s":
            x,y=self.canvas.coords(self.player)
            if(y<280):
                self.canvas.move(self.player, 0, 10)
        elif event.char == "w":
            x,y=self.canvas.coords(self.player)
            if(y>20):
                self.canvas.move(self.player, 0, -10)
        elif event.char == "a":
            x,y=self.canvas.coords(self.player)
            if(x>20):
                self.canvas.move(self.player, -10, 0)
        elif event.char == "d":
            x,y=self.canvas.coords(self.player)
            if(x<380):
                self.canvas.move(self.player, 10, 0)

    def shoot(self, event):
        x, y = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(x, y - 20, x + 5, y - 25, fill='yellow')
        self.bullets.append(bullet)

    def move_bullets(self,bullet):
                self.canvas.move(bullet, 0, -10)
    def restart(self,enemy,label,master,self1):
        self.canvas.coords(self.player, 200, 250)
        self.canvas.delete(label)
        self.canvas.delete(self.restart_button)
        master.bind('<KeyPress>',self.move)
        master.bind('<space>',self.shoot)
        for bullet in self.bullets:
            self.canvas.delete(bullet)
        for bullet in enemy.bullets:
             self.canvas.delete(bullet)
        for enem in enemy.enemies:
            self.canvas.delete(enem)
        self.bullets.clear()
        enemy.bullets.clear()
        enemy.enemies.clear()
        for i in range (3,28):
            enemy.enemies.append(i)
        self1.game_is_on=True
        self1.enemy = en.Enemy(self1.player)
        self1.update_game()
        

    def loose(self,master,enemy,self1):
        label=self.canvas.create_text(200, 100, text="Game Over", font=("Arial", 30), fill="red")
        self.restart_button = self.canvas.create_window(200, 150, window=tk.Button(self.canvas, text="Restart", command=lambda: self.restart(enemy, label, master,self1)))
        master.unbind('<KeyPress>')
        master.unbind('<space>')
    def win(self,master,enemy,self1):
        label=self.canvas.create_text(200, 100, text="You Win", font=("Arial", 30), fill="green")
        self.restart_button = self.canvas.create_window(200, 150, window=tk.Button(self.canvas, text="Restart", command=lambda: self.restart(enemy, label, master,self1)))
        master.unbind('<KeyPress>')
        master.unbind('<space>')