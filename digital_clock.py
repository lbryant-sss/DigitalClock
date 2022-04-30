from __future__ import with_statement
from calendar import c, weekday
from platform import python_branch
import pygame
from pygame.locals import *
import datetime
from math import pi, cos, sin

Width, Height, = 800, 300





pygame.init()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Brian's Digital Clock")
clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
RED = (255, 0, 0)
GREY = (58, 56, 56)
YELLOW = (255, 255, 0)
background = GREY

def numbers(number, size, color, position):
    font = pygame.font.SysFont('DS-Digital', size, True, False)
    text = font.render(number, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return int(x + Width / 2 + 175), int(-(y - Height / 2))



def main():
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.strftime('%S')
        minute = current_time.strftime('%M')
        hour = current_time.strftime('%I')
        am_pm = current_time.strftime('%p')
        weekday = current_time.strftime('%a')
        screen.fill(background)

        numbers(f"{hour}:{minute}", 200, WHITE, (Width /2 - 100, Height / 2))
        numbers(second, 60, RED, (Width /2 + 175, Height / 2))
        numbers(am_pm, 60, WHITE, (Width /2 + 260, Height / 2 -45))
        numbers(weekday[:], 60, WHITE, (Width / 2 + 260, Height / 2 + 44))
        
        r = 45
        theta = int(second) * 360 / 60
        pygame.draw.circle(screen, WHITE, (int(Width / 2 + 175), int(Height / 2)), r, 1)
        pygame.draw.circle(screen, RED, polar_to_cartesian(r, theta), 8)

        
        pygame.display.update()

        clock.tick(FPS)
    
    pygame.quit()
main()
