from Seed import Seed
from SolarSystem import SolarSystem
from nimble import cmds
import Utils

class Galaxy:

    _galaxySeed = 0
    _solarSystems = []
    _numSolarSystems = 0
    _maxSolarSystems = 20
    _axis = [0, 0, 0]
    _center = (0, 0, 0)
    _maxDistance = 1000



    def __init__(self, seedValue, numSystems = 1):
        self._galaxySeed = Seed(seedValue)
        if numSystems == 0:
            self._numSolarSystems = 1
        else:
            self._numSolarSystems = self._galaxySeed.ivalue() % self._maxSolarSystems

        for i in range(len(self._axis)):
            self._axis[i] = self._galaxySeed.fvalue()

<<<<<<< HEAD
        self._speed = self._galaxySeed.fvalue()*(Utils.degrees/2) + (Utils.degrees/2)

=======
<<<<<<< HEAD
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae
       # print("Systems: " + str(self._numSolarSystems) + "\nAxis:" + str(self._axis))
        self._transformNode = cmds.createNode('transform', n = 'Galaxy')#
        for s in range(self._numSolarSystems):
            distanceFromCenter = self._galaxySeed.fvalue() * self._maxDistance * Utils.randSign(self._galaxySeed.ivalue())
            self._solarSystems.append(SolarSystem(self._galaxySeed.ivalue(), distanceFromCenter, s, self._transformNode))

        x = self._axis[0] * Utils.degrees
        y = self._axis[1] * Utils.degrees
        z = self._axis[2] * Utils.degrees
<<<<<<< HEAD
        cmds.select(self._transformNode)
        cmds.currentTime(1)
        cmds.rotate(x,y,z, absolute=True, ws=1)
        cmds.setKeyframe()
=======
        cmds.rotate(x,y,z)
=======
        print("Systems: " + str(self._numSolarSystems) + "\nAxis:" + str(self._axis))

        for s in range(self._numSolarSystems):
            distanceFromCenter = self._galaxySeed.fvalue() * self._maxDistance
            self._solarSystems.append(SolarSystem(self._galaxySeed.ivalue(), distanceFromCenter))
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae

    def draw(self, rot, frames):
        if rot:
            time = self._speed
            cmds.select(self._transformNode)
            while time < frames:
                cmds.currentTime(time)
                cmds.setKeyframe()
                cmds.currentTime(time)
                cmds.rotate(0,359,0, r=True, objectSpace=True)
                cmds.setKeyframe()
                time += self._speed
            for s in range(self._numSolarSystems):
                self._solarSystems[s].draw(frames)
        else:
            print("NO ROTATION!")

    def delete(self):
        if (self._transformNode):
            cmds.select(self._transformNode)
            cmds.delete(self._transformNode)
    def cat(self):
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

            #EVERY OBJECT GETS THIS ROTATION!
            #cmds.rotate(0,45,0, relative = True, objectSpace = 1) where 45 is the angle of change between keyframes.


            flipped = 0
            for time in range(1,362, 10):
<<<<<<< HEAD
                if y == 270:
                    cmds.currentTime(time)
                    cmds.rotate(stuff[i][0], (x,y,z), absolute = False)
                    #cmds.setAttr(stuff[i][0]+".rotateAxisY", y, keyable = 1)
                    cmds.setKeyframe()
                    time += 1
                    cmds.currentTime(time)
                    y = -90
                    cmds.setAttr(stuff[i][0]+".rotateAxisY", y, keyable = 1)
                    cmds.setKeyframe()
                    #flipped = 1
                #elif y == -100:
                    #cmds.currentTime(time)
                    #cmds.setAttr(stuff[i][0]+".rotateAxisY", y, keyable = 1)
                    #cmds.setKeyframe()
                    #time += 1
                    #cmds.currentTime(time)
                    #y = 270
                    #cmds.setAttr(stuff[i][0]+".rotateAxisY", y, keyable = 1)
                    #cmds.setKeyframe()
                    #flipped = 0
                else:
                    cmds.currentTime(time)
                    cmds.setAttr(stuff[i][0]+".rotateAxisY", y, keyable = 1)
                    cmds.setKeyframe()
                #if flipped == 1:
                   # y -= 10
                #else:
                    #y += 10
                y += 10
=======
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

>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5


