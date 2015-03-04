__author__ = 'Sexymax'

from Seed import Seed
import Utils
from nimble import cmds

class Planet:

    _planetSeed = 0
    planetLoc = [0, 0, 0]
    _size = 0
    _minSize = 1
    _maxSize = 5 - _minSize
    _temperature = 0
    _minTemp = 2600
    _maxTemp = 26000 - _minTemp
    _maxLoc = 100
    _minLoc = 0
    _axis = [0, 0, 0]
    _distanceFromCenter = 0

    def __init__(self, seedValue, distance):
        """Creates a sun based on a seed value"""
        self._planetSeed = Seed(seedValue)
        self._size = int(self._planetSeed.fvalue() * self._maxSize) + self._minSize
        self.temperature = int(self._planetSeed.fvalue() * self._maxTemp) + self._minTemp
        self._minLoc = int(self._size * 0.5)
        self._distanceFromCenter = distance
        self._obj = cmds.polySphere(axis=(0,1,0), name="Planet", radius=1, subdivisionsX=20, subdivisionsY=20)

        for i in range(len(self.planetLoc)):
            self.planetLoc[i] = self._planetSeed.fvalue() * self._maxLoc * Utils.randSign(self._planetSeed.ivalue())
            self._axis[i] = self._planetSeed.fvalue() * Utils.randSign(self._planetSeed.ivalue())

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
            self.planetLoc[i] += transformList[i]

    def getDistanceFromCenter(self):
        return self._distanceFromCenter