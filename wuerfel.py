import pygame, sys, random 
from pygame.locals import *
from gpiozero import Button
pygame.init
button_links = Button()
button_rechts = Button()

FELD = pygame.display.set_mode((640, 320))
pygame.display.set_caption("Wuefel")

BLAU = (0, 0, 255); WEISS = (255, 255, 255); ROT = (255, 0, 0)

#Würfel rechts
P1 = ((480,160)); P2 = ((380, 60)); P3 = ((480, 60))
P4 = ((580, 60))
P5 = ((380, 260)); P6 = ((480, 260)); P7 = ((580, 260))

#Würfel links
P21 = ((160,160)); P22 = ((60, 60)); P23 = ((160, 60))
P24 = ((260, 60))
P25 = ((60, 260)); P26 = ((160, 260)); P27 = ((260, 260))

FELD.fill(BLAU)
pygame.draw.line(FELD, ROT, (320, 0), (320, 320), 5)


mainloop = True

print ("Beliebige Taste drücken, um zu würfeln, ESC beendet das Spiel")

while mainloop:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            mainloop = False

        if button_links.is_pressed or button_rechts.is_pressed:
            FELD.fill(BLAU)
            pygame.draw.line(FELD, ROT, (320, 0), (320, 320), 5)

        if button_links.is_pressed():
            ZAHL = random.randrange (1, 7); print (ZAHL)

            #Würfel 1/rechts
            if ZAHL == 1:
                pygame.draw.circle(FELD, WEISS, P1, 40)
            
            if ZAHL == 2:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)

            if ZAHL == 3:
                pygame.draw.circle(FELD, WEISS, P1, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
            
            if ZAHL == 4:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)

            if ZAHL == 5:
                pygame.draw.circle(FELD, WEISS, P1, 40)
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)

            if ZAHL == 6:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P3, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P6, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)

        if button_links.is_pressed():
            ZAHL2 = random.randrange (1,7);print (ZAHL2)

            #Würfel 2/links
            if ZAHL2 == 1:
                pygame.draw.circle(FELD, WEISS, P21, 40)
            
            if ZAHL2 == 2:
                pygame.draw.circle(FELD, WEISS, P22, 40)
                pygame.draw.circle(FELD, WEISS, P27, 40)

            if ZAHL2 == 3:
                pygame.draw.circle(FELD, WEISS, P21, 40)
                pygame.draw.circle(FELD, WEISS, P24, 40)
                pygame.draw.circle(FELD, WEISS, P25, 40)
            
            if ZAHL2 == 4:
                pygame.draw.circle(FELD, WEISS, P22, 40)
                pygame.draw.circle(FELD, WEISS, P24, 40)
                pygame.draw.circle(FELD, WEISS, P25, 40)
                pygame.draw.circle(FELD, WEISS, P27, 40)

            if ZAHL2 == 5:
                pygame.draw.circle(FELD, WEISS, P21, 40)
                pygame.draw.circle(FELD, WEISS, P22, 40)
                pygame.draw.circle(FELD, WEISS, P24, 40)
                pygame.draw.circle(FELD, WEISS, P25, 40)
                pygame.draw.circle(FELD, WEISS, P27, 40)

            if ZAHL2 == 6:
                pygame.draw.circle(FELD, WEISS, P22, 40)
                pygame.draw.circle(FELD, WEISS, P23, 40)
                pygame.draw.circle(FELD, WEISS, P24, 40)
                pygame.draw.circle(FELD, WEISS, P25, 40)
                pygame.draw.circle(FELD, WEISS, P26, 40)
                pygame.draw.circle(FELD, WEISS, P27, 40)
        pygame.display.update()

pygame.quit()       