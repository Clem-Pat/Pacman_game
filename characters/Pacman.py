"""Pacman"""

from pygame import *
import pygame.gfxdraw
import random
import time

class Pacman():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 'mobile'
        self.direction = 'right'
        self.direction_wanted = 'right'
        self.old_direction = 'right'
        self.img = image.load("Images/pacman.jpg")
        self.img = self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.img.set_colorkey((0, 0, 0))

    def rotate(self, angle):
        self.img = pygame.transform.rotate(self.img, angle)

    def test_secret_tunnel(self):
        if self.x >= 679:
            self.x = 210
        elif self.x <= 210:
            self.x = 679

    def pacman_move(self, app, chemin, turn_right, turn_left, opposite_direction, temps):

        temps = time.time()

        if self.direction_wanted in chemin[self.x, self.y]:
            self.direction = self.direction_wanted

        if self.direction == 'up' and self.direction in chemin[self.x, self.y]:
            self.y -= 1
            self.status = 'mobile'

            if self.direction == turn_right[self.old_direction]:
                self.rotate(-90)
            if self.direction == turn_left[self.old_direction]:
                self.rotate(90)
            if self.direction == opposite_direction[self.old_direction]:
                self.rotate(180)

        elif self.direction == 'right'and self.direction in chemin[self.x, self.y]:
            self.x += 1
            self.status = 'mobile'

            if self.direction == turn_right[self.old_direction]:
                self.rotate(-90)
            if self.direction == turn_left[self.old_direction]:
                self.rotate(90)
            if self.direction == opposite_direction[self.old_direction]:
                self.rotate(180)

        elif self.direction == 'down'and self.direction in chemin[self.x, self.y]:
            self.y += 1
            self.status = 'mobile'

            if self.direction == turn_right[self.old_direction]:
                self.rotate(-90)
            if self.direction == turn_left[self.old_direction]:
                self.rotate(90)
            if self.direction == opposite_direction[self.old_direction]:
                self.rotate(180)

        elif self.direction == 'left'and self.direction in chemin[self.x, self.y]:
            self.x -= 1
            self.status = 'mobile'

            if self.direction == turn_right[self.old_direction]:
                self.rotate(-90)
            if self.direction == turn_left[self.old_direction]:
                self.rotate(90)
            if self.direction == opposite_direction[self.old_direction]:
                self.rotate(180)

        else:
            if self.old_direction == 'up'and self.old_direction in chemin[self.x, self.y]:
                self.y -= 1
                self.status = 'mobile'
            elif self.old_direction == 'right'and self.old_direction in chemin[self.x, self.y]:
                self.x += 1
                self.status = 'mobile'
            elif self.old_direction == 'down'and self.old_direction in chemin[self.x, self.y]:
                self.y += 1
                self.status = 'mobile'
            elif self.old_direction == 'left'and self.old_direction in chemin[self.x, self.y]:
                self.x -= 1
                self.status = 'mobile'
            else:
                self.status = 'statique'

        self.rect.center = (self.x, self.y)
        app.blit(self.img, self.rect)
