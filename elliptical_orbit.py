import pygame
import sys
import math


pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
BLACK = (0,0,0)
RED = (225,0,0)
WHITE = (255,255,255,)
GREEN = (0,225,0)
BLUE = (0,0,225)
fps = 5
centerx = SCREEN_WIDTH //2
centery = SCREEN_HEIGHT // 2
sunRadius= 30
ballRadius = 20

def draw_sun():
    pygame.draw.circle(screen, RED, (centerx, centery), sunRadius)

def draw_orbit1():
    pygame.draw.ellipse(screen, WHITE, [50, 100, 700, 400], 1)

def draw_orbit2():
    pygame.draw.ellipse(screen, WHITE, [125, 220, 550, 180], 1)

def draw_balls(degree,orbitxRadius,orbityRadius,color):
    x = int(math.cos(degree * math.pi /180) * orbitxRadius) + centerx
    y = int(math.sin(degree * math.pi /180) *orbityRadius) + centery
    pygame.draw.circle(screen, color, (x, y), ballRadius)
   


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Elliptical-Orbit")
clock = pygame.time.Clock()

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    for degree in range(0, 360 ,10):
        screen.fill(BLACK)
        draw_sun()
        draw_orbit1()
        draw_orbit2()
        draw_balls(degree*2,275,90,GREEN)
        draw_balls(degree,350,200,BLUE)
        pygame.display.update()
        clock.tick(fps)
    
        