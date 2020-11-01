"""pacman pygame"""

from pygame import *
import pygame.gfxdraw
import sys
from os import chdir
import random
import time

from characters.Pacman import Pacman as Pacman
from characters.ghosts.Clyde import Clyde as Clyde
from characters.ghosts.Blinky import Blinky as Blinky
from characters.ghosts.Pinky import Pinky as Pinky
from characters.ghosts.Inky import Inky as Inky
from characters.candy import Candy as Candy

from map.map import create_map as map
from map.map import create_chemin as chemin

import os
path = os.path.dirname(os.path.abspath(__file__))

def create_fonts():
    L = []
    L.append(font.Font(path+"\\Fonts\\Arial.ttf", 20))
    L.append(font.Font(path+"\\Fonts\\GROBOLD.ttf", 30))
    L.append(font.Font(path+"\\Fonts\\GROBOLD.ttf", 40))

    return L


def create_texts(fonts, couleurs):
    L={}
    L['label_lives'] = fonts[0].render("Lives :", 1, couleurs[1])
    L['label_finish'] = fonts[1].render("CONGRATULATIONS", 1, couleurs[1])
    L['label_game_over'] = fonts[2].render("GAME OVER", 1, couleurs[1])
    L['label_enter_revive'] = fonts[1].render("Press Enter to revive", 1, couleurs[2])
    L['label_enter_restart'] = fonts[1].render("Press Enter to restart", 1, couleurs[2])
    return L


def create_dico_turn_left():
    L = {}
    L['right'] = 'up'
    L['up'] = 'left'
    L['left'] = 'down'
    L['down'] = 'right'
    return L


def create_dico_turn_right():
    L = {}
    L['right'] = 'down'
    L['down'] = 'left'
    L['left'] = 'up'
    L['up'] = 'right'
    return L


def create_dico_opposite_direction():
    L = {}
    L['right'] = 'left'
    L['down'] = 'up'
    L['left'] = 'right'
    L['up'] = 'down'
    return L


def create_candys(surface, chemin, couleurs):
    L = []
    indice = 0
    for k in chemin :
        if indice%25 == 0:
            L.append(Candy(k[0], k[1], 2, couleurs[2]))
        indice += 1

    L.append(Candy(215,119,6,couleurs[2]))
    L.append(Candy(675,119,6,couleurs[2]))
    L.append(Candy(215,385,6,couleurs[2]))
    L.append(Candy(675,385,6,couleurs[2]))
    return L


def get_events(app, running, game_over, cheat_mode, nbr_vies, pacman, blinky, clyde, inky, pinky):

    cheat = cheat_mode
    over = game_over
    run = running
    vies = nbr_vies
    again = False

    for evt in event.get():
        if evt.type == QUIT:
            run = False
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE or evt.key == K_DELETE:
                run = False

            # cheat codes :
            elif evt.key == K_c:
                rect_surface = Surface((10,10))
                rect_surface.fill((255,0,0))
                rect = rect_surface.get_rect()
                rect.center = (760,0)
                app.blit(rect_surface,rect)
                display.flip()
                time.sleep(0.2)
                for evt in event.get():
                    if evt.type == KEYDOWN:
                        if evt.key == K_o:
                            rect_surface = Surface((10,10))
                            rect_surface.fill((0,255,0))
                            rect = rect_surface.get_rect()
                            rect.center = (760,0)
                            app.blit(rect_surface,rect)
                            display.flip()
                            time.sleep(0.2)
                            for evt in event.get():
                                if evt.type == KEYDOWN:
                                    if evt.key == K_e:
                                        rect_surface = Surface((10,10))
                                        rect_surface.fill((0,0,255))
                                        rect = rect_surface.get_rect()
                                        rect.center = (760,0)
                                        app.blit(rect_surface,rect)
                                        display.flip()
                                        time.sleep(0.2)
                                        for evt in event.get():
                                            if evt.type == KEYDOWN:
                                                if evt.key == K_u:
                                                    rect_surface = Surface((10,10))
                                                    rect_surface.fill((255,255,0))
                                                    rect = rect_surface.get_rect()
                                                    rect.center = (760,0)
                                                    app.blit(rect_surface,rect)
                                                    display.flip()
                                                    time.sleep(0.2)
                                                    for evt in event.get():
                                                        if evt.type == KEYDOWN:
                                                            if evt.key == K_r:
                                                                rect_surface = Surface((10,10))
                                                                rect_surface.fill((0,255,255))
                                                                rect = rect_surface.get_rect()
                                                                rect.center = (760,0)
                                                                app.blit(rect_surface,rect)
                                                                display.flip()
                                                                cheat = [True,0.0015,9]

            elif evt.key == K_RIGHT:
                pacman.direction_wanted = 'right'
            elif evt.key == K_UP:
                pacman.direction_wanted = 'up'
            elif evt.key == K_DOWN:
                pacman.direction_wanted = 'down'
            elif evt.key == K_LEFT:
                pacman.direction_wanted = 'left'

            elif evt.key == K_RETURN:
                if over == 'perdu':
                    if vies != 0:

                        pacman.direction = 'right'
                        pacman.direction_wanted = 'right'

                        clyde.x, clyde.y = 475, 295
                        blinky.x, blinky.y = 445, 260
                        inky.x, inky.y = 415, 295
                        pinky.x, pinky.y = 445, 295
                        pacman.x ,pacman.y = 445,440

                        place_object(app, pacman)
                        place_object(app, clyde)
                        place_object(app, blinky)
                        place_object(app, inky)
                        place_object(app, pinky)

                        vies -= 1
                        over = False

                    else:
                        run = False
                        again = True

                elif over == 'gagne':
                    run = False
                    again = True

    return run, cheat, over, vies, again


def place_object(app, object):
    object.rect.center = (object.x, object.y)
    app.blit(object.img, object.rect)


def test_collision(surface, player, eaten, nbr_candys, monsters, game_over):

    over = game_over

    for i in range(len(monsters)):
        coord_i_x = list(range(monsters[i].x-10, monsters[i].x+10))
        coord_player_x = list(range(player.x-10, player.x+10))
        for j in coord_i_x:
            if j in coord_player_x:
                coord_i_y = list(range(monsters[i].y-11, monsters[i].y+13))
                coord_player_y = list(range(player.y-10, player.y+10))
                for k in coord_i_y:
                    if k in coord_player_y:
                        if monsters[i].behaviour != 'scared':
                            over = 'perdu'
                        else:
                            monsters[i].die(app)

    if eaten == nbr_candys:
        over = 'gagne'

    return over


def finish(app, game_over, nbr_vies, pacman, blinky, clyde, inky, pinky, label_finish, label_game_over, label_enter_revive, label_enter_restart):

    if game_over == 'gagne':

        clyde.x, clyde.y = 475, 295
        blinky.x, blinky.y = 445, 260
        inky.x, inky.y = 415, 295
        pinky.x, pinky.y = 445, 295

        place_object(app, pacman)
        place_object(app, clyde)
        place_object(app, blinky)
        place_object(app, inky)
        place_object(app, pinky)

        app.blit(label_finish, (292, 220))
        app.blit(label_enter_restart, (292,345))

    elif game_over == 'perdu':

        place_object(app, pacman)
        place_object(app, clyde)
        place_object(app, blinky)
        place_object(app, inky)
        place_object(app, pinky)

        app.blit(label_game_over, (320,210))
        if nbr_vies != 0:
            app.blit(label_enter_revive, (298,345))
        else:
            app.blit(label_enter_restart, (292,345))


def turn_in_blue(monsters):
    global temps_blue

    temps_blue = time.time()
    for i in range(len(monsters)):
        monsters[i].img = image.load("Images/ghost_in_blue.jpg")
        monsters[i].img = monsters[i].img.convert()
        monsters[i].behaviour = 'scared'


def turn_back_in_normal(monsters):
    for i in range(len(monsters)):
        monsters[i].img = monsters[i].profile
        monsters[i].img = monsters[i].img.convert()
        monsters[i].behaviour = 'shadow'


def main():
    global app, temps, time_start


    # chdir("C:/Users/cleme/Desktop/Documents/1. DOCUMENTS CLEMENT/TRAVAIL/Post BAC/projets personnels info/MINI JEUX/Pacman/pacman_game")
    fps = 30

    clock = pygame.time.Clock()  # pour fps
    init()
    app = display.set_mode((800, 550))
    display.set_caption('PACMAN')
    couleurs = [(0, 0, 255), (255, 255, 255), (255,255,0)]  # bleu, blanc, jaune

    turn_right = create_dico_turn_right()
    turn_left = create_dico_turn_left()
    opposite_direction = create_dico_opposite_direction()

    temps = 0
    delta_ms = clock.tick(fps)
    delta_s = delta_ms / 1000

    fonts = create_fonts()
    text = create_texts(fonts, couleurs)

    time_start = time.time()

    clyde = Clyde(475, 295, time_start)
    blinky = Blinky(445, 260, time_start)
    inky = Inky(415, 295, time_start)
    pinky = Pinky(445, 295, time_start)
    pacman = Pacman(445, 440)

    pacman_vie1 = Pacman(60, 100)
    pacman_vie2 = Pacman(90, 100)
    pacman_vie3 = Pacman(120, 100)
    nbr_vies = 2

    pacman_chemin = chemin('pacman')
    blinky_chemin = chemin('ghost')
    inky_chemin = chemin('ghost')
    clyde_chemin = chemin('ghost')
    pinky_chemin = chemin('ghost')

    candys = create_candys(app, pacman_chemin, couleurs)
    nbr_candys = len(candys)

    cheat_mode = [False, 0.008, 300]
    game_over = False
    running = True
    while running == True:
        temps = time.time() - time_start
        app.fill((0, 0, 0))
        map(app, couleurs)


        ### Events : ###
        running, cheat_mode, game_over, nbr_vies, play_again = get_events(app, running, game_over, cheat_mode, nbr_vies, pacman, blinky, clyde, inky, pinky)


        eaten = 0
        candy_indice = 0
        for i in candys:
            candy_indice += 1
            if  i.x in range(pacman.x-15,pacman.x+15) and i.y in range(pacman.y-15,pacman.y+15):
                if i.power == 1 and i.status == 'alive':
                    turn_in_blue([blinky, clyde, inky, pinky])
                i.status = 'eaten'
            if i.status == 'alive':
                if candy_indice < cheat_mode[2]:
                    i.draw_candy(app)
                else:
                    i.status = 'eaten'
            else:
                eaten+=1


        game_over = test_collision(app, pacman, eaten, nbr_candys, [blinky, clyde, inky, pinky], game_over)


        if game_over != False:
            finish(app, game_over, nbr_vies, pacman, blinky, clyde, inky, pinky, text['label_finish'], text['label_game_over'], text['label_enter_revive'], text['label_enter_restart'])


        if game_over == False :
            ### game not finished ###
            pacman.test_secret_tunnel()
            pacman.pacman_move(app, pacman_chemin, turn_right,
                               turn_left, opposite_direction, temps)

            blinky.blinky_move(app, blinky_chemin, turn_right,
                               turn_left, opposite_direction, temps, pacman.x, pacman.y)
            clyde.clyde_move(app, clyde_chemin, turn_right, turn_left,
                             opposite_direction, temps)
            inky.inky_move(app, inky_chemin, turn_right, turn_left,
                           opposite_direction, temps)
            pinky.pinky_move(app, pinky_chemin, turn_right, turn_left,
                             opposite_direction, temps)


        if blinky.behaviour == 'scared' or clyde.behaviour == 'scared' or inky.behaviour == 'scared' or pinky.behaviour == 'scared':
            duree = time.time() - temps_blue
            if duree > 5:
                turn_back_in_normal([blinky, clyde, inky, pinky])


        app.blit(text['label_lives'], (50, 50))
        app.blit(pacman_vie1.img, pacman_vie1.rect)  # l'objet et son rectangle
        if nbr_vies >= 1:
            app.blit(pacman_vie2.img, pacman_vie2.rect)  # l'objet et son rectangle
            if nbr_vies >= 2:
                app.blit(pacman_vie3.img, pacman_vie3.rect)  # l'objet et son rectangle


        display.update()

        pacman.old_direction = pacman.direction
        blinky.old_direction = blinky.direction
        clyde.old_direction = clyde.direction
        inky.old_direction = inky.direction
        pinky.old_direction = pinky.direction

        time.sleep(cheat_mode[1])


    quit()

    if play_again == True:
        main()


if __name__ == '__main__':
    main()
