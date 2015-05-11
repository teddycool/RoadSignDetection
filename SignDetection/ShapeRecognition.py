__author__ = 'psk'

import numpy as np
import cv2

class ShapeRegonition(object):

   # def __init__(self, shapesImg):



    def findContours(self, shapesImg):
        self.img = cv2.imread(shapesImg)
        self.gray = cv2.imread(shapesImg,0)

        ret,thresh = cv2.threshold(self.gray,100,255,cv2.THRESH_BINARY )

        contours,h = cv2.findContours(thresh,1,2)

        for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
            print len(approx)
            if len(approx)==5:
                print "pentagon"
                cv2.drawContours(self.img,[cnt],0,(255,0,0),-1)
            elif len(approx)==3:
                print "triangle"
                cv2.drawContours(self.img,[cnt],0,(0,255,0),-1)
            elif len(approx)==4:
                print "square"
                cv2.drawContours(self.img,[cnt],0,(0,0,255),-1)
            elif len(approx) == 9:
                print "half-circle"
                cv2.drawContours(self.img,[cnt],0,(255,255,0),-1)
            elif len(approx) > 9:
                print "circle"
                cv2.drawContours(self.img,[cnt],0,(0,255,255),-1)
        return self.img



if __name__ == "__main__":
    shapeImg = "C:\\Users\\psk\\PycharmProjects\\RoadSignDetection\\SignDetection\\testimg\\seq253.jpg"
    shapeImg = "C:\\Users\\psk\\PycharmProjects\\RoadSignDetection\\SignDetection\\testimg\\seq238.jpg"
    sr = ShapeRegonition()
    img = sr.findContours(shapeImg)
    cv2.imshow('ShapeRecognition',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()