import tkinter as tk
from src import player
from src import enemy
import random
class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Space Invaders")
        self.root.minsize(400, 300)
        self.root.resizable(False, False)

        
        

        self.player = player.Player(self.root)
        self.enemy = enemy.Enemy(self.player)

        self.start_button = self.player.canvas.create_window(200, 150, window=tk.Button(self.player.canvas, text="start", command=self.start_game))


        self.game_is_on = None
        self.update_game()

    def update_game(self):
        
        if self.game_is_on:
            self.root.update()
            if len(self.enemy.enemies) == 0:
                self.player.win(self.root,self.enemy,self)
                self.game_is_on = False
            else:
                for enem in self.enemy.enemies:
                    if random.randint(0, 220) == 10:
                        self.enemy.shoot(self.player,enem)

            for bullet in self.enemy.bullets:
                self.enemy.move_bullets(bullet, self.player)
                x1, y1, x2, y2 = self.player.canvas.coords(bullet)
                x3, y3 = self.player.canvas.coords(self.player.player)
                if (x3 - x1 >= -20 and x3 - x1 <= 20) and (y3 - y1 >= 0 and y3 - y1 <= 5):
                    self.player.loose(self.root,self.enemy,self)
                    self.game_is_on = False
                    break

            self.enemy.move_all_enemies(self.player)
                    

            for bullet in self.player.bullets:
                self.player.move_bullets(bullet)
                x1, y1, x2, y2 = self.player.canvas.coords(bullet)
                for enem in self.enemy.enemies:
                    x3, y3 = self.player.canvas.coords(enem)
                    if (x3 - x1 >= -15 and x3 - x1 <= 20) and y3 - y2 == 0:
                        self.player.bullets.remove(bullet)
                        self.player.canvas.delete(bullet)
                        
                        self.enemy.enemies.remove(enem)
                        self.player.canvas.delete(enem)
                        break

                if y1 < 0 or y2 > self.player.canvas.winfo_height():
                    self.player.canvas.delete(bullet)
                    self.player.bullets.remove(bullet)
        else:
            return
        self.root.after(50, self.update_game)
    def start_game(self):
        self.player.canvas.delete(self.start_button)
        self.game_is_on = True
        self.update_game()