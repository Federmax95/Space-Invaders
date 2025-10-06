from PIL import Image, ImageTk
from src.utils import resource_path

class Enemy:
    def __init__(self, player):
        enemy_image = resource_path("Utils/enemy.png")
        enemy_image = Image.open(enemy_image)
        enemy_image = enemy_image.resize((30, 30))
        self.enemies=[]
        self.bullets=[]
        self.direction = 'right'
        self.horizontal_move=3
        self.enemy_image = ImageTk.PhotoImage(enemy_image)
        x=107
        y=20
        for _ in range (5):
            for _ in range(5):
                self.enemies.append(player.canvas.create_image(x, y, image=self.enemy_image))
                x+=40
            x=107
            y+=30
        
    def shoot(self, player,enemy):
        x, y = player.canvas.coords(enemy)
        bullet = player.canvas.create_rectangle(x, y - 20, x + 5, y - 25, fill='red')
        self.bullets.append(bullet)

    def move_bullets(self,bullet,player):
            player.canvas.move(bullet, 0, +7)
            
    def move_enemy(self, player, enemy):
        player.canvas.move(enemy,self.horizontal_move, 0)

        x, _ = player.canvas.coords(enemy)
        if x >= 370:
            self.horizontal_move = -3
            
        elif x <= 30:
            self.horizontal_move = 3
    def move_all_enemies(self, player):
        for enemy in self.enemies:
            self.move_enemy(player, enemy)