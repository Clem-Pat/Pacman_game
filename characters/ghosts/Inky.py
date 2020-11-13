"""Inky"""

from pygame import *
import pygame.gfxdraw
import random
import time

class Inky():
    def __init__(self, path, x, y, t):
        self.x_debut = x
        self.y_debut = y
        self.x = x
        self.y = y
        self.status = 'mobile'
        self.behaviour = 'shadow'

        self.direction = 'left'
        self.direction_wanted = 'left'
        self.old_direction = 'right'
        self.path = path

        self.profile = image.load(self.path+"\\Images\\Inky_right.jpg")
        self.img = image.load(self.path + "\\Images\\Inky_right.jpg")
        self.img = self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.img.set_colorkey((0, 0, 0))

        self.position = 'box'
        self.time_start = t
        self.time_in_box_origin = t
        self.time_in_box = time.time() - t


    def die(self,app):
        self.x, self.y = self.x_debut, self.y_debut
        self.rect.center = (self.x, self.y)
        app.blit(self.img, self.rect)
        self.position = 'box'
        self.time_in_box_origin = time.time()
        self.time_in_box = time.time() - self.time_in_box_origin


    def inky_move(self, app, chemin, turn_right, turn_left, opposite_direction, temps):
        self.time_in_box = time.time() - self.time_in_box_origin


        if self.direction_wanted in chemin[self.x, self.y]:
            self.direction = self.direction_wanted

        if self.direction == 'up' and self.direction in chemin[self.x, self.y]:
            self.y -= 1
            self.status = 'mobile'

        elif self.direction == 'right'and self.direction in chemin[self.x, self.y]:
            self.x += 1
            self.status = 'mobile'

        elif self.direction == 'down'and self.direction in chemin[self.x, self.y]:
            self.y += 1
            self.status = 'mobile'

        elif self.direction == 'left'and self.direction in chemin[self.x, self.y]:
            self.x -= 1
            self.status = 'mobile'

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


        if self.position == 'box' and self.time_in_box > 15:
            ### GET OUT OF BOX ###
            self.direction_wanted = 'up'

        if self.y == 260:
            self.position = 'out'

        if self.status == 'statique':
            self.direction_wanted = random.choice(chemin[self.x, self.y])

        self.rect.center = (self.x, self.y)
        app.blit(self.img, self.rect)
