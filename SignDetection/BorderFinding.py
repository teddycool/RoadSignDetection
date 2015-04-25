__author__ = 'psk'
import cv2
import numpy as np
import pygame

class Borders(object):

    def __init__(self):
        return

    def update(self, snapshot):
        #img = cv2.
        img = pygame.surfarray(snapshot)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,50,150,apertureSize = 3)

        lines = cv2.HoughLines(edges,1,np.pi/180,200)
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

        return img

#def draw(self, screen):

if __name__ == "__main__":

    #snapshot = pygame.surface.Surface((640,480),0)
    snapshot = pygame.image.load("r1501m.jpg")
    bf = Borders()
    img = bf.update(snapshot)
    pygame.image.save(img, "test.jpg")