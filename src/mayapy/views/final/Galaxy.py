from Seed import Seed
from SolarSystem import SolarSystem
import nimble
from nimble import cmds
import Utils

class Galaxy:

    _galaxySeed = 0
    _solarSystems = []
    _numSolarSystems = 0
    _maxSolarSystems = 5
    _axis = [0, 0, 0]
    _center = (0, 0, 0)
    _maxDistance = 100


    def __init__(self, seedValue, numSystems = 1):
        self._galaxySeed = Seed(seedValue)
        if numSystems == 0:
            self._numSolarSystems = 1
        else:
            self._numSolarSystems = self._galaxySeed.ivalue() % self._maxSolarSystems

        for i in range(len(self._axis)):
            self._axis[i] = self._galaxySeed.fvalue()

        print("Systems: " + str(self._numSolarSystems) + "\nAxis:" + str(self._axis))

        for s in range(self._numSolarSystems):
            distanceFromCenter = self._galaxySeed.fvalue() * self._maxDistance
            self._solarSystems.append(SolarSystem(self._galaxySeed.ivalue(), distanceFromCenter))

    def draw(self, rot):
        if rot:
            print("ROTATION!")
        else:
            print("NO ROTATION!")
        x = self._axis[0] * Utils.degrees
        y = self._axis[1] * Utils.degrees
        z = self._axis[2] * Utils.degrees
        stuff = []
        for i in range(5):
            g = cmds.polySphere(axis=(0,1,0), name="G", radius=1, subdivisionsX=20, subdivisionsY=20)
            stuff.append(g)
            x = self._galaxySeed.fvalue() * Utils.degrees
            y = self._galaxySeed.fvalue() * Utils.degrees
            z = self._galaxySeed.fvalue() * Utils.degrees
            cmds.rotate(x,y,z)
            #cmds.setAttr(stuff[i][0]+".translateX", self._galaxySeed.fvalue()*10, keyable = 1)
            cmds.move(self._galaxySeed.fvalue()*10, 0, 0, absolute = 0, objectSpace = 1 )
            cmds.move(0,0,0,  stuff[i][0]+".rotatePivot", stuff[i][0]+".scalePivot",absolute = 1 )
            y = 0
            flipped = 0
            for time in range(1,362, 10):
                cmds.currentTime(time)
                cmds.setAttr(stuff[i][0]+".rotateAxisY", y, keyable = 1)
                if flipped == 1:
                    y -= 10
                else:
                    y += 10
                if y == 261:
                    y = -91
                    flipped = 1
                elif y == 0:
                    flipped = 1
                cmds.setKeyframe()



