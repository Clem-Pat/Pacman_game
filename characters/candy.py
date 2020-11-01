"""Candy"""

from pygame import *
import pygame.gfxdraw

class Candy():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.status = 'alive'
        self.color = color

        if radius == 6:
            self.power = 1
        else:
            self.power = 0

    def draw_candy(self, surface):
        if self.status == 'alive':
            draw.circle(surface, self.color, [self.x,self.y], self.radius)
