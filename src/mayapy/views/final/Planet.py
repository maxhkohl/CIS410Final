__author__ = 'Sexymax'

from Seed import Seed
import Utils
<<<<<<< HEAD
from nimble import cmds
=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5

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

    def __init__(self, seedValue, distance, t, p):
        """Creates a sun based on a seed value"""
        self._planetSeed = Seed(seedValue)
        self._size = int(self._planetSeed.fvalue() * self._maxSize) + self._minSize
        self.temperature = int(self._planetSeed.fvalue() * self._maxTemp) + self._minTemp
        self._minLoc = int(self._size * 0.5)
        self._distanceFromCenter = distance
<<<<<<< HEAD
        self._obj = cmds.polySphere(axis=(0,1,0), name = 'Planet' + str(t) + str(p), radius=1, subdivisionsX=20, subdivisionsY=20) #name="Planet",
        self.addTo(t)
=======
<<<<<<< HEAD
        self._obj = cmds.polySphere(axis=(0,1,0), name="Planet", radius=1, subdivisionsX=20, subdivisionsY=20)
=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae

        for i in range(len(self.planetLoc)):
            self.planetLoc[i] = self._planetSeed.fvalue() * self._maxLoc * Utils.randSign(self._planetSeed.ivalue())
            self._axis[i] = self._planetSeed.fvalue() * Utils.randSign(self._planetSeed.ivalue())

<<<<<<< HEAD
        self._speed = self._planetSeed.fvalue()*(Utils.degrees/2) + (Utils.degrees/2)

        cmds.select(self._obj[0])
        cmds.currentTime(1)
        #cmds.rotate(self._axis[0]*Utils.degrees,self._axis[1]*Utils.degrees,self._axis[2]*Utils.degrees,r=True)
        cmds.move(self._axis[0]*distance,self._axis[1]*distance,self._axis[2]*distance, r=True)
        cmds.setKeyframe()

    def addTo(self,  p):
        cmds.parent(self._obj[0],p)

    def draw(self, f):
        time = self._speed
        cmds.select(self._transformNode)
        while time < f:
            cmds.currentTime(time)
            cmds.setKeyframe()
            cmds.currentTime(time) #7100
            cmds.rotate(0,359,0, r=True)
            cmds.setKeyframe()
            time += self._speed
=======
<<<<<<< HEAD
    def addTo(self, parent):
        cmds.parent(self._obj[0],parent)
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae

=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5
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