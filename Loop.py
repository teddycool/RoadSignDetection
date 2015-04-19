__author__ = 'psk'

import Inputs
import pygame

class Loop(object):
    def __init__(self):
        print "Loop constructor"
        self._inputs=Inputs.Inputs(self)

    def initialize(self):
        print "Loop init..."
        self._inputs.initialize()

    def update(self,screen, snapshot):
        self._inputs.update(screen)


    def draw(self, screen):
        black = 0, 0, 0
        self._inputs.draw(screen)
        myfont = pygame.font.SysFont("Arial", 20)
        autolabel = myfont.render("AUTO: Forward", 1, (255,255,255))

        screen.blit(autolabel, (0,100))
     #   self._obstacles.draw(snapshot)

