# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
import random
import math
from Seed import Seed
from Galaxy import Galaxy


#___________________________________________________________________________________________________ Assignment1Widget
class FinalWidget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(FinalWidget, self).__init__(parent, **kwargs)
        self.initBtn.clicked.connect(self._handleInit)
        self.makeSingleBtn.clicked.connect(self._handleSingle)
        self.makeAllBtn.clicked.connect(self._handleAll)
        self.deleteAllBtn.clicked.connect(self._handleDeleteAll)
        self.makeSeedBtn.clicked.connect(self._handleMakeSeed)
        self.nextBtn.clicked.connect(self._handleNext)
        self.prevBtn.clicked.connect(self._handlePrev)
        self.deleteSelectedBtn.clicked.connect(self._handleDeleteSelected)
        self.incrementBtn.clicked.connect(self._handleIncrementSeed)
        self.frameJumpBtn.clicked.connect(self._handleJumpFrame)
        self._s = 0
        self._galaxy = 0
        self._labelText = "Current Seed: "

#===================================================================================================
#                                                                                 H A N D L E R S

    def _handleInit(self):
        print("CATS!")
    def _handleSingle(self):
        print("Single Solar System")
        if (self._s == 0 or len(self.seedBox.text()) == 0 ):
            self._s = Seed(0)
        self._galaxy = Galaxy(self._s.ivalue(), 0)
        self._galaxy.draw(self.rotation.isChecked())
    def _handleAll(self):
        print("Multi-System")
        if (self._s == 0 or len(self.seedBox.text()) == 0 ):
            self._s = Seed(0)
        self._galaxy = Galaxy(self._s.ivalue())
        self._galaxy.draw(self.rotation.isChecked())
    def _handleDeleteAll(self):
        print("KILL THEM ALL!")

    def _handleMakeSeed(self):
        print("Make Seed")
        seedNum = self.seedBox.text()
        if ('.' in seedNum):
            seedNum = float(seedNum)
            seedNum *= 1000
        if (len(seedNum) == 0):
            seedNum = 0
        seedNum = int(seedNum)
        self._s = Seed(seedNum)
        self.seedLabel.setText(self._labelText + str(seedNum))

    def _handleIncrementSeed(self):
        self.seedBox.setText(str(self._s.ivalue()))
    def _handleNext(self):
        print("Next")
    def _handlePrev(self):
        print("Prev")
    def _handleDeleteSelected(self):
        print("Delete Selected")

    def _handleJumpFrame(self):
        frame = self.frameJump.text()
        if (not frame.isdigit()):
            frame = 1
            print("INVALID INPUT!")
        print("Jumpt to frame: " + frame)
        cmds.currentTime(frame)