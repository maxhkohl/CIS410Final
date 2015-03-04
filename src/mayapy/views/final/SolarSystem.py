from Seed import Seed
from Sun import Sun
from Planet import Planet
<<<<<<< HEAD
from nimble import cmds
=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5

class SolarSystem:
    _solarSystemSeed = 0
    _numSuns = 0
    _maxSuns = 3
    _minSuns = 1
    _numPlanets = 0
    _maxPlanets = 5
    _maxDistance = 100
    center = [0, 0, 0]
    _planets = []
    _suns = []
    _maxSunDistance = 35
    _distanceFromCenter = 0

    def __init__(self, seedValue, distance):
        self._solarSystemSeed = Seed(seedValue)
        self._numSuns = self._solarSystemSeed.ivalue() % self._maxSuns + self._minSuns
        self._numPlanets = self._solarSystemSeed.ivalue() % self._maxPlanets
        self._distanceFromCenter = distance

<<<<<<< HEAD
        self._transformNode = cmds.createNode('transform', n = 'Solar System')
        for s in range(self._numSuns):
            sunDistance = self._solarSystemSeed.fvalue() * self._maxSunDistance
            self._suns.append(Sun(self._solarSystemSeed.ivalue(), sunDistance))
            self._suns[s].addTo(self._transformNode)

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
            distanceFromSun = self._solarSystemSeed.ivalue() % self._maxDistance
            self._planets.append(Planet(self._solarSystemSeed.ivalue(), distanceFromSun))
<<<<<<< HEAD
            self._planets[p].addTo(self._transformNode)

    def addTo(self, parentNode):
        cmds.parent(self._transformNode, parentNode)
=======
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5

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



