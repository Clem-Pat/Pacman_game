"""map"""

from pygame import *
import pygame.gfxdraw


def create_map(app, couleurs):

    pygame.gfxdraw.hline(app, 196, 694, 70, couleurs[0])  # 0
    pygame.gfxdraw.hline(app, 200, 430, 74, couleurs[0])  # 1
    pygame.gfxdraw.hline(app, 460, 690, 74, couleurs[0])  # 2
    pygame.gfxdraw.vline(app, 430, 74, 134, couleurs[0])  # 3
    pygame.gfxdraw.vline(app, 460, 74, 134, couleurs[0])  # 4
    pygame.gfxdraw.hline(app, 430, 460, 134, couleurs[0])  # 5

    pygame.gfxdraw.vline(app, 196, 70, 224, couleurs[0])  # 6
    pygame.gfxdraw.vline(app, 200, 74, 220, couleurs[0])  # 7
    pygame.gfxdraw.hline(app, 196, 286, 224, couleurs[0])  # 8
    pygame.gfxdraw.hline(app, 200, 290, 220, couleurs[0])  # 9
    pygame.gfxdraw.vline(app, 290, 220, 280, couleurs[0])  # 10
    pygame.gfxdraw.vline(app, 286, 224, 276, couleurs[0])  # 11
    pygame.gfxdraw.hline(app, 286, 196, 276, couleurs[0])  # 12
    pygame.gfxdraw.hline(app, 290, 196, 280, couleurs[0])  # 13

    pygame.gfxdraw.hline(app, 290, 196, 310, couleurs[0])  # 14
    pygame.gfxdraw.hline(app, 286, 196, 314, couleurs[0])  # 15
    pygame.gfxdraw.vline(app, 290, 310, 370, couleurs[0])  # 16
    pygame.gfxdraw.vline(app, 286, 314, 366, couleurs[0])  # 17
    pygame.gfxdraw.hline(app, 196, 286, 366, couleurs[0])  # 18
    pygame.gfxdraw.hline(app, 200, 290, 370, couleurs[0])  # 19
    pygame.gfxdraw.vline(app, 196, 366, 520, couleurs[0])  # 20
    pygame.gfxdraw.vline(app, 200, 370, 456, couleurs[0])  # 21
    pygame.gfxdraw.hline(app, 200, 230, 456, couleurs[0])  # 22
    pygame.gfxdraw.vline(app, 230, 456, 486, couleurs[0])  # 23
    pygame.gfxdraw.hline(app, 200, 230, 486, couleurs[0])  # 24
    pygame.gfxdraw.vline(app, 200, 486, 516, couleurs[0])  # 25

    pygame.gfxdraw.hline(app, 196, 694, 520, couleurs[0])  # 26
    pygame.gfxdraw.hline(app, 200, 690, 516, couleurs[0])  # 27

    pygame.gfxdraw.vline(app, 690, 486, 516, couleurs[0])  # 28
    pygame.gfxdraw.vline(app, 694, 366, 520, couleurs[0])  # 29
    pygame.gfxdraw.hline(app, 690, 660, 486, couleurs[0])  # 30
    pygame.gfxdraw.vline(app, 660, 456, 486, couleurs[0])  # 31
    pygame.gfxdraw.hline(app, 660, 690, 456, couleurs[0])  # 32
    pygame.gfxdraw.vline(app, 690, 370, 456, couleurs[0])  # 33
    pygame.gfxdraw.hline(app, 690, 600, 370, couleurs[0])  # 34
    pygame.gfxdraw.hline(app, 694, 604, 366, couleurs[0])  # 35
    pygame.gfxdraw.vline(app, 600, 310, 370, couleurs[0])  # 36
    pygame.gfxdraw.vline(app, 604, 314, 366, couleurs[0])  # 37
    pygame.gfxdraw.hline(app, 600, 694, 310, couleurs[0])  # 38
    pygame.gfxdraw.hline(app, 604, 694, 314, couleurs[0])  # 39

    pygame.gfxdraw.hline(app, 600, 694, 280, couleurs[0])  # 40
    pygame.gfxdraw.hline(app, 604, 694, 276, couleurs[0])  # 41
    pygame.gfxdraw.vline(app, 600, 220, 280, couleurs[0])  # 42
    pygame.gfxdraw.vline(app, 604, 224, 276, couleurs[0])  # 43
    pygame.gfxdraw.hline(app, 600, 690, 220, couleurs[0])  # 44
    pygame.gfxdraw.hline(app, 604, 694, 224, couleurs[0])  # 45
    pygame.gfxdraw.vline(app, 690, 74, 220, couleurs[0])  # 46
    pygame.gfxdraw.vline(app, 694, 70, 224, couleurs[0])  # 47

    pygame.gfxdraw.vline(app, 230, 104, 134, couleurs[0])  # A1
    pygame.gfxdraw.hline(app, 230, 290, 104, couleurs[0])  # A2
    pygame.gfxdraw.vline(app, 290, 104, 134, couleurs[0])  # A3
    pygame.gfxdraw.hline(app, 230, 290, 134, couleurs[0])  # A4

    pygame.gfxdraw.vline(app, 320, 104, 134, couleurs[0])  # A5
    pygame.gfxdraw.hline(app, 320, 400, 104, couleurs[0])  # A6
    pygame.gfxdraw.vline(app, 400, 104, 134, couleurs[0])  # A7
    pygame.gfxdraw.hline(app, 320, 400, 134, couleurs[0])  # A8

    pygame.gfxdraw.hline(app, 230, 290, 164, couleurs[0])  # A9
    pygame.gfxdraw.vline(app, 290, 164, 190, couleurs[0])  # A10
    pygame.gfxdraw.hline(app, 230, 290, 190, couleurs[0])  # A11
    pygame.gfxdraw.vline(app, 230, 164, 190, couleurs[0])  # A12

    pygame.gfxdraw.hline(app, 320, 345, 164, couleurs[0])  # A13
    pygame.gfxdraw.vline(app, 345, 164, 220, couleurs[0])  # A14
    pygame.gfxdraw.vline(app, 320, 164, 280, couleurs[0])  # A15
    pygame.gfxdraw.hline(app, 345, 400, 220, couleurs[0])  # A16
    pygame.gfxdraw.vline(app, 400, 220, 245, couleurs[0])  # A17
    pygame.gfxdraw.hline(app, 345, 400, 245, couleurs[0])  # A18
    pygame.gfxdraw.vline(app, 345, 245, 280, couleurs[0])  # A19
    pygame.gfxdraw.hline(app, 320, 345, 280, couleurs[0])  # A20

    pygame.gfxdraw.hline(app, 375, 515, 164, couleurs[0])  # A'1
    pygame.gfxdraw.vline(app, 375, 164, 190, couleurs[0])  # A'2
    pygame.gfxdraw.vline(app, 515, 164, 190, couleurs[0])  # A'3
    pygame.gfxdraw.hline(app, 375, 430, 190, couleurs[0])  # A'4
    pygame.gfxdraw.hline(app, 460, 515, 190, couleurs[0])  # A'5
    pygame.gfxdraw.vline(app, 430, 190, 245, couleurs[0])  # A'6
    pygame.gfxdraw.vline(app, 460, 190, 245, couleurs[0])  # A'7
    pygame.gfxdraw.hline(app, 430, 460, 245, couleurs[0])  # A'8

    pygame.gfxdraw.vline(app, 490, 104, 134, couleurs[0])  # B1
    pygame.gfxdraw.hline(app, 490, 570, 104, couleurs[0])  # B2
    pygame.gfxdraw.vline(app, 570, 104, 134, couleurs[0])  # B3
    pygame.gfxdraw.hline(app, 490, 570, 134, couleurs[0])  # B4

    pygame.gfxdraw.vline(app, 600, 104, 134, couleurs[0])  # B5
    pygame.gfxdraw.hline(app, 600, 660, 104, couleurs[0])  # B6
    pygame.gfxdraw.vline(app, 660, 104, 134, couleurs[0])  # B7
    pygame.gfxdraw.hline(app, 600, 660, 134, couleurs[0])  # B8

    pygame.gfxdraw.hline(app, 600, 660, 164, couleurs[0])  # B9
    pygame.gfxdraw.vline(app, 660, 164, 190, couleurs[0])  # B10
    pygame.gfxdraw.hline(app, 600, 660, 190, couleurs[0])  # B11
    pygame.gfxdraw.vline(app, 600, 164, 190, couleurs[0])  # B12

    pygame.gfxdraw.hline(app, 545, 570, 164, couleurs[0])  # B13
    pygame.gfxdraw.vline(app, 545, 164, 220, couleurs[0])  # B14
    pygame.gfxdraw.vline(app, 570, 164, 280, couleurs[0])  # B15
    pygame.gfxdraw.hline(app, 490, 545, 220, couleurs[0])  # B16
    pygame.gfxdraw.vline(app, 490, 220, 245, couleurs[0])  # B17
    pygame.gfxdraw.hline(app, 490, 545, 245, couleurs[0])  # B18
    pygame.gfxdraw.vline(app, 545, 245, 280, couleurs[0])  # B19
    pygame.gfxdraw.hline(app, 545, 570, 280, couleurs[0])  # B20

    pygame.gfxdraw.hline(app, 320, 400, 400, couleurs[0])  # C1
    pygame.gfxdraw.vline(app, 400, 400, 425, couleurs[0])  # C2
    pygame.gfxdraw.hline(app, 320, 400, 425, couleurs[0])  # C3
    pygame.gfxdraw.vline(app, 320, 400, 425, couleurs[0])  # C4

    pygame.gfxdraw.hline(app, 320, 400, 455, couleurs[0])  # C5
    pygame.gfxdraw.vline(app, 400, 455, 485, couleurs[0])  # C6
    pygame.gfxdraw.hline(app, 320, 400, 485, couleurs[0])  # C7
    pygame.gfxdraw.vline(app, 320, 455, 485, couleurs[0])  # C8

    pygame.gfxdraw.hline(app, 230, 290, 400, couleurs[0])  # C9
    pygame.gfxdraw.vline(app, 290, 400, 485, couleurs[0])  # C10
    pygame.gfxdraw.hline(app, 260, 290, 485, couleurs[0])  # C11
    pygame.gfxdraw.vline(app, 260, 425, 485, couleurs[0])  # C12
    pygame.gfxdraw.hline(app, 230, 260, 425, couleurs[0])  # C13
    pygame.gfxdraw.vline(app, 230, 400, 425, couleurs[0])  # C14

    pygame.gfxdraw.hline(app, 430, 460, 277, couleurs[1])  # D1
    pygame.gfxdraw.vline(app, 430, 275, 280, couleurs[0])  # D1'
    pygame.gfxdraw.vline(app, 460, 275, 280, couleurs[0])  # D1''
    pygame.gfxdraw.hline(app, 460, 515, 275, couleurs[0])  # D2
    pygame.gfxdraw.hline(app, 460, 510, 280, couleurs[0])  # D2'
    pygame.gfxdraw.vline(app, 515, 275, 315, couleurs[0])  # D3
    pygame.gfxdraw.vline(app, 510, 280, 310, couleurs[0])  # D3'
    pygame.gfxdraw.hline(app, 375, 515, 315, couleurs[0])  # D4
    pygame.gfxdraw.hline(app, 380, 510, 310, couleurs[0])  # D4'
    pygame.gfxdraw.vline(app, 375, 275, 315, couleurs[0])  # D5
    pygame.gfxdraw.vline(app, 380, 280, 310, couleurs[0])  # D5'
    pygame.gfxdraw.hline(app, 375, 430, 275, couleurs[0])  # D6
    pygame.gfxdraw.hline(app, 380, 430, 280, couleurs[0])  # D6'

    pygame.gfxdraw.hline(app, 320, 345, 310, couleurs[0])  # D7
    pygame.gfxdraw.vline(app, 345, 310, 370, couleurs[0])  # D8
    pygame.gfxdraw.vline(app, 320, 310, 370, couleurs[0])  # D9
    pygame.gfxdraw.hline(app, 320, 345, 370, couleurs[0])  # D10

    pygame.gfxdraw.hline(app, 545, 570, 310, couleurs[0])  # D11
    pygame.gfxdraw.vline(app, 545, 310, 370, couleurs[0])  # D12
    pygame.gfxdraw.vline(app, 570, 310, 370, couleurs[0])  # D13
    pygame.gfxdraw.hline(app, 545, 570, 370, couleurs[0])  # D14

    pygame.gfxdraw.hline(app, 490, 570, 400, couleurs[0])  # E1
    pygame.gfxdraw.vline(app, 570, 400, 425, couleurs[0])  # E2
    pygame.gfxdraw.hline(app, 490, 570, 425, couleurs[0])  # E3
    pygame.gfxdraw.vline(app, 490, 400, 425, couleurs[0])  # E4

    pygame.gfxdraw.hline(app, 490, 570, 455, couleurs[0])  # E5
    pygame.gfxdraw.vline(app, 570, 455, 485, couleurs[0])  # E6
    pygame.gfxdraw.hline(app, 490, 570, 485, couleurs[0])  # E7
    pygame.gfxdraw.vline(app, 490, 455, 485, couleurs[0])  # E8

    pygame.gfxdraw.hline(app, 600, 660, 400, couleurs[0])  # E9
    pygame.gfxdraw.vline(app, 600, 400, 485, couleurs[0])  # E10
    pygame.gfxdraw.hline(app, 600, 630, 485, couleurs[0])  # E11
    pygame.gfxdraw.vline(app, 630, 425, 485, couleurs[0])  # E12
    pygame.gfxdraw.hline(app, 630, 660, 425, couleurs[0])  # E13
    pygame.gfxdraw.vline(app, 660, 400, 425, couleurs[0])  # E14

    pygame.gfxdraw.hline(app, 375, 515, 345, couleurs[0])  # F1
    pygame.gfxdraw.vline(app, 515, 345, 370, couleurs[0])  # F2
    pygame.gfxdraw.hline(app, 460, 515, 370, couleurs[0])  # F3
    pygame.gfxdraw.vline(app, 460, 370, 425, couleurs[0])  # F4
    pygame.gfxdraw.hline(app, 430, 460, 425, couleurs[0])  # F5
    pygame.gfxdraw.vline(app, 430, 370, 425, couleurs[0])  # F6
    pygame.gfxdraw.hline(app, 375, 430, 370, couleurs[0])  # F7
    pygame.gfxdraw.vline(app, 375, 345, 370, couleurs[0])  # F8

    pygame.gfxdraw.hline(app, 430, 460, 455, couleurs[0])  # F9
    pygame.gfxdraw.vline(app, 460, 455, 485, couleurs[0])  # F10
    pygame.gfxdraw.hline(app, 430, 460, 485, couleurs[0])  # F11
    pygame.gfxdraw.vline(app, 430, 455, 485, couleurs[0])  # F12

    pass


def create_chemin(object):
    L = {}

    # Suivant les x
    for i in range(215, 415):
        L[(i, 89)] = ['right', 'left']
    for i in range(475, 675):
        L[(i, 89)] = ['right', 'left']

    for i in range(215, 675):
        L[(i, 149)] = ['right', 'left']

    for i in range(215, 305):
        L[(i, 205)] = ['right', 'left']
    for i in range(360, 415):
        L[(i, 205)] = ['right', 'left']
    for i in range(475, 530):
        L[(i, 205)] = ['right', 'left']
    for i in range(585, 675):
        L[(i, 205)] = ['right', 'left']

    for i in range(360, 530):
        L[(i, 260)] = ['right', 'left']

    for i in range(210, 360):
        L[(i, 295)] = ['right', 'left']
    for i in range(530, 680):
        L[(i, 295)] = ['right', 'left']

    for i in range(360, 530):
        L[(i, 330)] = ['right', 'left']

    for i in range(215, 415):
        L[(i, 385)] = ['right', 'left']
    for i in range(475, 675):
        L[(i, 385)] = ['right', 'left']

    for i in range(215, 245):
        L[(i, 440)] = ['right', 'left']
    for i in range(305, 585):
        L[(i, 440)] = ['right', 'left']
    for i in range(645, 675):
        L[(i, 440)] = ['right', 'left']

    for i in range(215, 675):
        L[(i, 500)] = ['right', 'left']

    # Suivant les y
    for j in range(89, 205):
        L[(215, j)] = ['up', 'down']
    for j in range(385, 440):
        L[(215, j)] = ['up', 'down']

    for j in range(440, 500):
        L[(245, j)] = ['up', 'down']

    for j in range(89, 500):
        L[(305, j)] = ['up', 'down']

    for j in range(149, 205):
        L[(360, j)] = ['up', 'down']
    for j in range(260, 385):
        L[(360, j)] = ['up', 'down']

    for j in range(89, 149):
        L[(415, j)] = ['up', 'down']
    for j in range(205, 260):
        L[(415, j)] = ['up', 'down']
    for j in range(385, 500):
        L[(415, j)] = ['up', 'down']

    for j in range(89, 149):
        L[(475, j)] = ['up', 'down']
    for j in range(205, 260):
        L[(475, j)] = ['up', 'down']
    for j in range(385, 500):
        L[(475, j)] = ['up', 'down']

    for j in range(149, 205):
        L[(530, j)] = ['up', 'down']
    for j in range(260, 385):
        L[(530, j)] = ['up', 'down']

    for j in range(89, 500):
        L[(585, j)] = ['up', 'down']

    for j in range(440, 500):
        L[(645, j)] = ['up', 'down']

    for j in range(89, 205):
        L[(675, j)] = ['up', 'down']
    for j in range(385, 440):
        L[(675, j)] = ['up', 'down']

    ### points de virage ###
    # I
    L[(215, 89)] = ['down', 'right']
    L[(305, 89)] = ['right', 'left', 'down']
    L[(415, 89)] = ['left', 'down']
    L[(475, 89)] = ['down', 'right']
    L[(585, 89)] = ['left', 'right', 'down']
    L[(675, 89)] = ['left', 'down']

    # II
    L[(215, 149)] = ['up', 'down', 'right']
    L[(305, 149)] = ['up', 'down', 'right', 'left']
    L[(360, 149)] = ['down', 'right', 'left']
    L[(415, 149)] = ['up', 'right', 'left']
    L[(475, 149)] = ['up', 'right', 'left']
    L[(530, 149)] = ['down', 'right', 'left']
    L[(585, 149)] = ['up', 'down', 'right', 'left']
    L[(675, 149)] = ['up', 'down', 'left']

    # III
    L[(215, 205)] = ['up', 'right']
    L[(305, 205)] = ['up', 'down', 'left']
    L[(360, 205)] = ['up', 'right']
    L[(415, 205)] = ['down', 'left']
    L[(475, 205)] = ['down', 'right']
    L[(530, 205)] = ['up', 'left']
    L[(585, 205)] = ['up', 'down', 'right']
    L[(675, 205)] = ['up', 'left']

    # IV
    L[(360, 260)] = ['down', 'right']
    L[(415, 260)] = ['up', 'right', 'left']
    L[(475, 260)] = ['up', 'right', 'left']
    L[(530, 260)] = ['down', 'left']

    # V
    L[(305, 295)] = ['up', 'down', 'right', 'left']
    L[(360, 295)] = ['up', 'down', 'left']
    L[(530, 295)] = ['up', 'down', 'right']
    L[(585, 295)] = ['up', 'down', 'right', 'left']

    # VI
    L[(360, 330)] = ['up', 'down', 'right']
    L[(530, 330)] = ['up', 'down', 'left']

    # VII
    L[(215, 385)] = ['down', 'right']
    L[(305, 385)] = ['up', 'down', 'right', 'left']
    L[(360, 385)] = ['up', 'right', 'left']
    L[(415, 385)] = ['down', 'left']
    L[(475, 385)] = ['down', 'right']
    L[(530, 385)] = ['up', 'right', 'left']
    L[(585, 385)] = ['up', 'down', 'right', 'left']
    L[(675, 385)] = ['down', 'left']

    # VIII
    L[(215, 440)] = ['up', 'right']
    L[(245, 440)] = ['down', 'left']
    L[(305, 440)] = ['up', 'down', 'right']
    L[(415, 440)] = ['up', 'down', 'right', 'left']
    L[(475, 440)] = ['up', 'down', 'right', 'left']
    L[(585, 440)] = ['up', 'down', 'left']
    L[(645, 440)] = ['down', 'right']
    L[(675, 440)] = ['up', 'left']

    # IX
    L[(215, 500)] = ['right']
    L[(245, 500)] = ['up', 'right', 'left']
    L[(305, 500)] = ['up', 'right', 'left']
    L[(415, 500)] = ['up', 'right', 'left']
    L[(475, 500)] = ['up', 'right', 'left']
    L[(585, 500)] = ['up', 'right', 'left']
    L[(645, 500)] = ['up', 'right', 'left']
    L[(675, 500)] = ['left']

    if object == 'ghost':
        for i in range(395, 495):
            L[(i, 295)] = ['right', 'left']

        for j in range(260, 295):
            L[(445, j)] = ['up']

        L[(445, 260)] = ['right', 'left']
        L[(445, 295)] = ['right', 'left', 'up']
        L[(395, 295)] = ['right']
        L[(495, 295)] = ['left']

    return L
