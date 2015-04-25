__author__ = 'psk'

import os, sys, pygame
import pygame.camera
import Loop

class Main(object):

    def __init__(self, camid, cwidth, cheigth):
        print "Main __init__"
        self.dwidth = 320
        self.dheight = 240
        self._loop=Loop.Loop(camid, cwidth, cheigth)



    def run(self):

        #Init and set up variables...
        pygame.init()
        self.display = pygame.display.set_mode((self.dwidth,self.dheight))
        print pygame.display.Info()
        self._loop.initialize()

        screensurface = pygame.surface.Surface((self.dwidth,self.dheight),0)
        #snapshot = pygame.image.load("roadsigns.jpg")

        print "Starting program evaluation loop"
        while 1:

            self._loop.update()

            black=0,0,0
            self.display.fill(black)

            snapshot=self._loop.draw()
            #resize snapshot to fit screensize using screensurface

            self.display.blit(snapshot,(0,0))
            pygame.display.flip()


if __name__ == "__main__":
    #Set to webcam ID, std is 0. Networked cam is probably 1
    camid=0
    #Set to resolution of your webcam
    width= 848
    height=480
    gl=Main(camid,width,height)
    gl.run()