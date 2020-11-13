"""Blinky"""

from pygame import *
import pygame.gfxdraw
import math
import random
import time


class Blinky():
    """Shadow"""
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

        self.profile = image.load(path+"\\Images\\Blinky_right.jpg")
        self.img = image.load(path+"\\Images\\Blinky_right.jpg")
        self.img = self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.img.set_colorkey((0, 0, 0))

        self.position = 'out'
        self.time_start = t
        self.time_in_box_origin = t
        self.time_in_box = time.time() - t


    def die(self,app):
        self.x, self.y = 475, 295
        self.rect.center = (self.x, self.y)
        app.blit(self.img, self.rect)
        self.position = 'box'
        self.time_in_box_origin = time.time()
        self.time_in_box = time.time() - self.time_in_box_origin


    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        pass


    def fct_behaviour(self, chemin, pacman_x, pacman_y):
        ### BEHAVIOUR : Normally SHADOW ###

        if self.position == 'box' :
            if self.status == 'statique':
                self.direction_wanted = random.choice(chemin[self.x, self.y])
            if self.behaviour != 'scared' and self.time_in_box > 5:
                self.direction_wanted = 'up'

        else:
            if self.status == 'statique' and self.behaviour != 'scared':
                self.behaviour = 'stuck'

            if self.behaviour == 'stuck':
                ## Don't follow Pacman until there is a cross road ###
                self.direction = random.choice(chemin[self.x,self.y])
                self.behaviour = 'unstucking'

            elif self.behaviour == 'unstucking':
                if len(chemin[self.x,self.y]) > 2:
                    self.behaviour = 'follow'

            elif self.behaviour == 'follow':
                # if self.distance(self.x,self.y,pacman_x,pacman_y) > 50:
                #     ### Follow Pacman ###
                if self.distance(self.x - 1, self.y, pacman_x, pacman_y) < self.distance(self.x + 1, self.y, pacman_x, pacman_y) and 'left' in chemin[self.x, self.y]:
                    self.direction_wanted = 'left'
                elif self.distance(self.x - 1, self.y, pacman_x, pacman_y) > self.distance(self.x + 1, self.y, pacman_x, pacman_y) and 'right' in chemin[self.x, self.y]:
                    self.direction_wanted = 'right'
                if self.distance(self.x, self.y - 1, pacman_x, pacman_y) < self.distance(self.x, self.y + 1, pacman_x, pacman_y) and 'up' in chemin[self.x, self.y]:
                    self.direction_wanted = 'up'
                elif self.distance(self.x, self.y + 1, pacman_x, pacman_y) < self.distance(self.x, self.y - 1, pacman_x, pacman_y) and 'down' in chemin[self.x, self.y]:
                    self.direction_wanted = 'down'




    def blinky_move(self, app, chemin, turn_right, turn_left, opposite_direction, temps, pacman_x, pacman_y):

        self.fct_behaviour(chemin, pacman_x, pacman_y)

        self.time_in_box = time.time() - self.time_in_box_origin

        ### MOVING ###
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

        if self.position == 'box' and self.time_in_box > 5:
            ### GET OUT OF BOX ###
            self.direction_wanted = 'up'

        if self.y == 260:
            self.position = 'out'

        self.rect.center = (self.x, self.y)
        app.blit(self.img, self.rect)
