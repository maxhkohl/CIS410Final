__author__ = 'Sexymax'

from Seed import Seed
import Utils
<<<<<<< HEAD
from nimble import cmds

=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5

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

    def __init__(self, seedValue, distance, t, s):
        """Creates a sun based on a seed value"""
        self._sunSeed = Seed(seedValue)
        self._size = int(self._sunSeed.fvalue() * self._maxSize) + self._minSize
        self.temperature = int(self._sunSeed.fvalue() * self._maxTemp) + self._minTemp
        self._minLoc = int(self._size * 0.5)
        self._distanceFromCenter = distance

        for i in range(len(self.sunLoc)):
            #self.sunLoc[i] = self._sunSeed.fvalue() * self._maxLoc * Utils.randSign(self._sunSeed.ivalue())
            self._axis[i] = self._sunSeed.fvalue() * Utils.randSign(self._sunSeed.ivalue())

<<<<<<< HEAD
        self._obj = cmds.polySphere(axis=(0,1,0), name="Sun" + str(t) + str(s),radius=1, subdivisionsX=20, subdivisionsY=20) # name="Sun"
        self._light = cmds.pointLight(d=2,rgb=[1,1,1],rs=1)
        cmds.parent(self._light,self._obj[0])
        self.addTo(t)
=======
<<<<<<< HEAD
        self._obj = cmds.polySphere(axis=(0,1,0), name="Sun", radius=1, subdivisionsX=20, subdivisionsY=20)
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae

        self._sunShader = cmds.shadingNode('blinn', asShader=1)

        self._speed = self._sunSeed.fvalue()*(Utils.degrees/2) + (Utils.degrees/2)

        cmds.select(self._obj[0])
        cmds.currentTime(1)
        #cmds.rotate(self._axis[0]*Utils.degrees,self._axis[1]*Utils.degrees,self._axis[2]*Utils.degrees,r=True,objectSpace=1)
        #cmds.move(self._axis[0]*distance,self._axis[1]*distance,self._axis[2]*distance, r=True)
        cmds.setKeyframe()
        #cmds.addAttr(shortName = 'n', longName = 'name', dataType = "string");
        #cmds.setAttr(self._obj[0] + '.' + 'name', "Sun" + str (t) + str(s), type="string");

    def addTo(self, p):
        if '|' in p:
            p = p[1:]
        cmds.parent(self._obj[0],p)
        #There is a namespace issue. Need to find a way to give every object a unique name

    def draw(self, frames):
        time = self._speed
        cmds.select(self._transformNode)
        while time < frames:
            cmds.currentTime(time)
            cmds.setKeyframe()
            cmds.currentTime(time) #7100
            cmds.rotate(0,359,0, r=True)
            cmds.setKeyframe()
            time += self._speed

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
            self.sunLoc[i] += transformList[i]

    def draw(self):
        print("DRAW SUN!")

    def getDistanceFromCenter(self):
        return self._distanceFromCenter