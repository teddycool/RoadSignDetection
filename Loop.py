__author__ = 'psk'

import Inputs
import Cam
from SignDetection import BorderFinding

class Loop(object):
    def __init__(self, camid, cwidth, cheigth):
        print "Loop constructor"
        self._inputs=Inputs.Inputs(self)
        self._cam=Cam.Cam(camid, cwidth, cheigth)
        self._border= BorderFinding.Borders()


    def initialize(self):
        print "Loop init..."
        self._inputs.initialize()
        self._cam.initialize()

    def update(self):
        self._inputs.update()
        self._cam.update()

        self._border.update(snapshot)

    def draw(self, screen):
        self._inputs.draw(screen)
        self._border.draw(screen)