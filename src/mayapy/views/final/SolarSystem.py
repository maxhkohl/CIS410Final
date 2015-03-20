from Seed import Seed
from Sun import Sun
from Planet import Planet
<<<<<<< HEAD
from nimble import cmds
<<<<<<< HEAD
import Utils
=======
=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae

class SolarSystem:
    _solarSystemSeed = 0
    _numSuns = 0
    _maxSuns = 1
    _minSuns = 1
    _numPlanets = 0
    _maxPlanets = 5
    _maxDistance = 100
    center = [0, 0, 0]
    _planets = []
    _suns = []
    _maxSunDistance = 35
    _distanceFromCenter = 0

    def __init__(self, seedValue, distance, s, tn):
        self._solarSystemSeed = Seed(seedValue)
        self._numSuns = self._solarSystemSeed.ivalue() % self._maxSuns + self._minSuns
        self._numPlanets = self._solarSystemSeed.ivalue() % self._maxPlanets
        self._distanceFromCenter = distance
        self._axis = [0,0,0]
        for i in range(len(self._axis)):
            self._axis[i] = self._solarSystemSeed.fvalue()

<<<<<<< HEAD
        self._transformNode = cmds.createNode('transform', n = 'Solar System' + str(s))#, n = 'Solar System'
        self.addTo(tn)
=======
<<<<<<< HEAD
        self._transformNode = cmds.createNode('transform', n = 'Solar System')
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae
        for s in range(self._numSuns):
            sunDistance = self._solarSystemSeed.fvalue() * self._maxSunDistance * Utils.randSign(self._solarSystemSeed.ivalue())
            self._suns.append(Sun(self._solarSystemSeed.ivalue(), sunDistance, self._transformNode, s))

=======
        for s in range(self._numSuns):
            sunDistance = self._solarSystemSeed.fvalue() * self._maxSunDistance
            self._suns.append(Sun(self._solarSystemSeed.ivalue(), sunDistance))
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5
        if self._numSuns > 1:
            self.center = self.calculateCenter()
        else:
            self.center = self._suns[0].sunLoc
        for p in range(self._numPlanets):
<<<<<<< HEAD
            distanceFromSun = (self._solarSystemSeed.fvalue() * self._maxDistance) * Utils.randSign(self._solarSystemSeed.ivalue())
            self._planets.append(Planet(self._solarSystemSeed.ivalue(), distanceFromSun, self._transformNode, p))
        self._speed = self._solarSystemSeed.fvalue()*(Utils.degrees/2) + (Utils.degrees/2)

        cmds.select(self._transformNode)
        cmds.currentTime(1)
        cmds.rotate(self._axis[0]*Utils.degrees,self._axis[1]*Utils.degrees,self._axis[2]*Utils.degrees,r=True,objectSpace=1)
        cmds.move(self._axis[0]*distance,self._axis[1]*distance,self._axis[2]*distance, r=True)
        cmds.setKeyframe()

=======
            distanceFromSun = self._solarSystemSeed.ivalue() % self._maxDistance
            self._planets.append(Planet(self._solarSystemSeed.ivalue(), distanceFromSun))
<<<<<<< HEAD
            self._planets[p].addTo(self._transformNode)
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae

    def addTo(self, parentNode):
        cmds.parent(self._transformNode, parentNode)
=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5

    def draw(self, f):
        frames = f
        time = self._speed
        cmds.select(self._transformNode)
        while time < f:
            cmds.currentTime(time)
            cmds.setKeyframe()
            cmds.currentTime(time) #7100
            cmds.rotate(0,359,0, r=True, objectSpace=True)
            cmds.setKeyframe()
            time += self._speed
        #for s in range(self._numSuns):
            #self._suns[s].draw(frames)
        #for p in range(self._numPlanets):
            #self._planets[p].draw(frames)
        #cmds.select(self._transformNode)
        #cmds.currentTime(self._speed)
        #cmds.rotate(0,359,r=True,objectSpace=1)
        #cmds.setKeyframe()


    def calculateCenter(self):
        loc = [0,0,0]
        mass = 0
        for i in range(self._numSuns):
            loc[0] += self._suns[i].sunLoc[0] * self._suns[i].getSize()
            loc[1] += self._suns[i].sunLoc[1] * self._suns[i].getSize()
            loc[2] += self._suns[i].sunLoc[2] * self._suns[i].getSize()
            mass += self._suns[i].getSize()
        for i in range(len(loc)):
            loc[i] = loc[i] / float(mass)
        return loc



