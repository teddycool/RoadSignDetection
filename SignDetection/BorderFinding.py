__author__ = 'psk'
import cv2
import numpy as np
import pygame

class Borders(object):

    def __init__(self):
        return

    def update(self, img):
        #img = cv2.
        #img = pygame.surfarray.array3d(snapshot)
        img1 = cv2.medianBlur(img,1)
        cimg = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
        #cv2.imwrite("C:\\Users\\psk\\PycharmProjects\\RoadSignDetection\\SignDetection\\testimg\\seq253_gray.jpg",cimg)

        circles = cv2.HoughCircles(img1,cv2.cv.CV_HOUGH_GRADIENT,1,150, param1=100,param2=10,minRadius=12,maxRadius=20)
        print "Circles: " + str(len(circles))
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        return img

#def draw(self, screen):

if __name__ == "__main__":

    #snapshot = pygame.surface.Surface((640,480),0)
    snapshot = cv2.imread("C:\\Users\\psk\\PycharmProjects\\RoadSignDetection\\SignDetection\\testimg\\seq391.jpg", 0)
    bf = Borders()
    img = bf.update(snapshot)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()