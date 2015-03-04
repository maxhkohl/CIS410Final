__author__ = 'Sexymax'

from Seed import Seed
import Utils
from nimble import cmds


class Sun:

    _sunSeed = 0
    sunLoc = [0, 0, 0]
    _size = 0
    _minSize = 10
    _maxSize = 50 - _minSize
    _temperature = 0
    _minTemp = 2600
    _maxTemp = 26000 - _minTemp
    _maxDistance = 100
    _minDistance = 0
    _axis = [0, 0, 0]
    _distanceFromCenter = 0

    def __init__(self, seedValue, distance):
        """Creates a sun based on a seed value"""
        self._sunSeed = Seed(seedValue)
        self._size = int(self._sunSeed.fvalue() * self._maxSize) + self._minSize
        self.temperature = int(self._sunSeed.fvalue() * self._maxTemp) + self._minTemp
        self._minLoc = int(self._size * 0.5)
        self._distanceFromCenter = distance

        for i in range(len(self.sunLoc)):
            #self.sunLoc[i] = self._sunSeed.fvalue() * self._maxLoc * Utils.randSign(self._sunSeed.ivalue())
            self._axis[i] = self._sunSeed.fvalue() * Utils.randSign(self._sunSeed.ivalue())

        self._obj = cmds.polySphere(axis=(0,1,0), name="Sun", radius=1, subdivisionsX=20, subdivisionsY=20)

    def addTo(self, parent):
        cmds.parent(self._obj[0],parent)

    def getSize(self):
        """Returns integer size"""
        return self._size

    def getTemp(self):
        """Returns integer temperature"""
        return self._temperature

    def getAxis(self):
        """Returns 3 element list of floats"""
        return self._axis

    def move(self, transformList):
        for i in range(transformList):
            self.sunLoc[i] += transformList[i]

    def draw(self):
        print("DRAW SUN!")

    def getDistanceFromCenter(self):
        return self._distanceFromCenter