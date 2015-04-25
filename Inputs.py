__author__ = 'psk'
import Main
import pygame
import sys
from PComponents import Button
from pygame.locals import *

class Inputs(object):
    def __init__(self,main):
        print "Inputconstructor"
        self.Buttons = {}

    def initialize(self):
        print "Input init..."
        #Array/collection of buttons
        self.Buttons["Exit"] = Button.Button((280,200,40, 40))
        self.Buttons["Exit"].color=(0,0,0,0)
        self.Buttons["Exit"].iconFg= pygame.image.load("Icons/Frame_Exit.png")
        self.Buttons["Exit"].callback = sys.exit

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if(event.type is MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()

                for button in self.Buttons:
                    if self.Buttons[button].selected(pos) == True:
                        self.Buttons[button].selectedImage = self.Buttons[button].iconFgPressed

                if(event.type is MOUSEBUTTONUP):
                    for button in self.Buttons:
                        self.Buttons[button].selectedImage = self.Buttons[button].iconFg

    def draw(self, screen):
        for button in self.Buttons:
            self.Buttons[button].draw(screen)

