__author__ = 'psk'
import pygame

class Cam(object):
    def __init__(self, camid, cwidth, cheight):
        print "Cam __init__"
        self.camid=camid
        self.width= cwidth
        self.height=cheight


    def initialize(self):
        print "Cam initialize: " + str(self.camid)
        #Init and set up variables...
        pygame.camera.init()
        self.csnapshot = pygame.surface.Surface((self.width,self.height),0) #current frame
        self.psnapshot = pygame.surface.Surface((self.width,self.height),0) #previous frame
        self.cam = pygame.camera.Camera(self.camid,(self.width,self.height),"RGB")


    def update(self):
        #update each loop
        self.psnapshot = self.csnapshot
        self.csnapshot = self.cam.get_image(self.csnapshot)
        return self.csnapshot


    def draw(self):
        #draw each loop
        return