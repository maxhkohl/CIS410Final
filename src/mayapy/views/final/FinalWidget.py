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
        self.makeSingleBtn.clicked.connect(self._handleSingle)
        self.makeAllBtn.clicked.connect(self._handleAll)
        self.deleteAllBtn.clicked.connect(self._handleDeleteAll)
        self.makeSeedBtn.clicked.connect(self._handleMakeSeed)
        self.incrementBtn.clicked.connect(self._handleIncrementSeed)
        self.frameJumpBtn.clicked.connect(self._handleJumpFrame)
        self._s = 0
        self._galaxy = 0
        self._labelText = "Current Seed: "

#===================================================================================================
#                                                                                 H A N D L E R S

    def _handleSingle(self):
        print("Single Solar System")
        if (self._s == 0 or len(self.seedBox.text()) == 0 ):
            self._s = Seed(0)
        self._galaxy = Galaxy(self._s.ivalue(), 0)
<<<<<<< HEAD
        frames = self.numFrames.text()
        if (not frames.isdigit()):
            frames = 2000
            print("INVALID INPUT!")
        elif int(frames) < 2000:
            frames = 2000
            self.frameAlert.setText("Min number of frames: 2000")
            self.numFrames.setText(str(frames))
        self._galaxy.draw(self.rotation.isChecked(), int(frames))

=======
<<<<<<< HEAD
        #self._galaxy.draw(self.rotation.isChecked())
=======
        self._galaxy.draw(self.rotation.isChecked())
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae
    def _handleAll(self):
        print("Multi-System")
        if (self._s == 0 or len(self.seedBox.text()) == 0 ):
            self._s = Seed(0)
        self._galaxy = Galaxy(self._s.ivalue())
<<<<<<< HEAD
        frames = self.numFrames.text()
        if (not frames.isdigit()):
            frames = 2000
            print("INVALID INPUT!")
        elif int(frames) < 2000:
            frames = 2000
            self.frameAlert.setText("Min number of frames: 2000")
            self.numFrames.setText(str(frames))

        self._galaxy.draw(self.rotation.isChecked(), int(frames))
=======
<<<<<<< HEAD
        #self._galaxy.draw(self.rotation.isChecked())
=======
        self._galaxy.draw(self.rotation.isChecked())
>>>>>>> afb0212cf83f3a6c4b667c98647fc9a96063a6c5
>>>>>>> 7e92e6b5feebc6be4a8a1435d1967e1dffbaf9ae
    def _handleDeleteAll(self):
        print("KILL THEM ALL!")
        self._galaxy.delete()

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

    def _handleJumpFrame(self):
        frame = self.frameJump.text()
        if (not frame.isdigit()):
            frame = 1
            print("INVALID INPUT!")
        else:
            self.currentFrameLabel.setText("Current Frame: " + str(frame))
            cmds.currentTime(frame)
