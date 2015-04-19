__author__ = 'psk'

import os, sys, pygame
import pygame.camera
from pygame.locals import *
import Loop


class Main(object):

    def __init__(self, width, height, camid):
        print "Init pygame..."
        self.cwidth = width
        self.cheight = height
        self.dwidth = 320
        self.dheight = 240
        self.camId=camid
        self._loop=Loop.Loop()


    def run(self):
        #Init and set up variables...
        pygame.init()
        pygame.camera.init()

        self.screen = pygame.display.set_mode((self.dwidth,self.dheight),HWSURFACE|DOUBLEBUF|RESIZABLE)
        print pygame.display.Info()

        self._loop.initialize()

        self.cam = pygame.camera.Camera(self.camId,(self.cwidth,self.cheight),"RGB")
        self.cam.start()


        #Set surface to handle a frame from camera
        snapshot = pygame.surface.Surface((self.cwidth,self.cheight), 0, self.screen)
        screensurface = pygame.surface.Surface((self.dwidth,self.dheight), 0, self.screen)
        testsurface = pygame.surface.Surface((400,120), 0, self.screen)
        pygame.transform.scale(snapshot, (400,120), testsurface)

        self.cam.get_image(snapshot)
        print "snapshot size: " + str(snapshot.get_size())
        print "screensurface size: " + str(screensurface.get_size())
        print "testsurface size: " + str(testsurface.get_size())


        print "Program evaluation-loop started"
        while 1:
            self.cam.get_image(snapshot)
            self._loop.update(screensurface, snapshot)
            black=0,0,0
            self.screen.fill(black)

            pygame.transform.scale(snapshot, (self.dwidth,self.dheight), screensurface)

            self._loop.draw(screensurface)
            self.screen.blit(screensurface, (0,0))
            pygame.display.flip()



#Testcode to run module. Standard Python way of testing modules.
#OBS !! comment out   line 47: "C:\Python27\Lib\site-packages\pygame\_camera_vidcapture.py":
#       #self.dev.setresolution(width, height) on row 49 in:
#
if __name__ == "__main__":
    #Set to webcam ID, std is 0. Networked cam is probably 1
    camid=0
    #Set to resolution of your webcam
    width= 640
    height=480
    gl=Main(width,height, camid)
    gl.run()