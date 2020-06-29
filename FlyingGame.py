import pygame
import os
import random
import math

pygame.init()

width=600
height=600
screen=pygame.display.set_mode((width, height))

def write(text, size):
    fo=pygame.font.SysFont("Arial", size)
    rend=fo.render(text, 0, (255,100,100))
    x=(width-rend.get_rect().width)/2
    y=(height-rend.get_rect().height)/2
    screen.blit(rend, (x,y))

def writexy(text, x, y, size):
    fo=pygame.font.SysFont("Arial", size)
    rend=fo.render(text, 0, (255,100,100))
    screen.blit(rend, (x,y))

now="menu"

class Obstacle():
    def __init__(self, x, width):
        self.x=x
        self.width=width
        self.y_up=0
        self.height_up=random.randint(150,250)
        self.space=200
        self.y_down=self.height_up+self.space
        self.height_down=height-self.y_down
        self.color=(160,140,190)
        self.shape_up=pygame.Rect(self.x, self.y_up, self.width, self.height_up)
        self.shape_down=pygame.Rect(self.x, self.y_down, self.width, self.height_down)
    def draw_obstacle(self):
        pygame.draw.rect(screen, self.color, self.shape_up, 0)
        pygame.draw.rect(screen, self.color, self.shape_down, 0)
    def move(self, v):
        self.x=self.x-v
        self.shape_up=pygame.Rect(self.x, self.y_up, self.width, self.height_up)
        self.shape_down=pygame.Rect(self.x, self.y_down, self.width, self.height_down)
    def collision(self, player):
        if self.shape_up.colliderect(player) or self.shape_down.colliderect(player):
            return True
        else:
            return False

class Flyer():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.height=30
        self.width=30
        self.shape=pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphic=pygame.image.load(os.path.join("image.jpg"))
    def draw_flyer(self):
        screen.blit(self.graphic, (self.x, self.y))
    def move(self, v):
        self.y=self.y+v
        self.shape=pygame.Rect(self.x, self.y, self.width, self.height)
        
obstacles = []
for i in range(21):
    obstacles.append(Obstacle(i*width/20, width/20))

player=Flyer(250, 275)
dy=0

pygame.mixer.init() 
pygame.mixer.music.load("song.mp3") 
pygame.mixer.music.set_volume(0.7) 
pygame.mixer.music.play(-1) 

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                dy=-0.25
            if event.key==pygame.K_DOWN:
                dy=0.25
            if event.key==pygame.K_SPACE:
                if now!="flight":
                    player=Flyer(250, 275)
                    dy=0
                    now="flight"
                    points=0
    screen.fill((0,0,0))
    if now=="menu":
        write("Press a space to begin.", 20)
        graphic=pygame.image.load(os.path.join("Cacodemon.png"))
        screen.blit(graphic, (155, 0))
    elif now=="flight":
        for j in obstacles:
            j.move(0.25)
            j.draw_obstacle()
            if j.collision(player.shape):
                now="GameOver"
        for j in obstacles:
            if j.x <= -j.width:
                obstacles.remove(j)
                obstacles.append((Obstacle(width, width/20)))
                points=points+math.fabs(dy)
        player.draw_flyer()
        player.move(dy)
        writexy(str(points), 50, 50, 20)
    elif now=="GameOver":
        write("GAME OVER", 20)
        writexy("Score: "+str(points), 255, 320, 20)
        graphic=pygame.image.load(os.path.join("Cacodemon.png"))
        screen.blit(graphic, (155, 0))        
    pygame.display.update()
