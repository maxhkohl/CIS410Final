__author__ = 'Sexymax'
import sys

class Seed:

    #Data Members
    _seedMax = 1000
    _series = [0,0]
    _fCounter = 0
    _dataMax = sys.maxint/2
    __name__ = "Seed"

    #Member Functions
    #Default Constructor
    def __init__(self, seedValue):
        if (type(seedValue) == "float"):
            seedValue *= 1000
            seedValue = int(seedValue)
        if (seedValue == self._seedMax or seedValue == 0): #Make sure mod operation goes well
            seedValue += 7  #I picked an arbitrary prime number to make sure that every mod operation doesn't return 0
        #The seed value we are given is the highest value in the series.
        self._series[0] = seedValue
        #Add another arbitrary number to the series
        self._series[1] = seedValue - 1

        #Go through the increment process a few times in order to get a large enough number to be useful.
        while self._series[0] < self._seedMax:
                self._increment()

    #Accessor
    def fvalue(self):
        """Returns the current Seed value, between 0 and 1"""
        #Save the current value of the Seed function
        temp = self._series[0];
        #Now increment the series so the next time we call the value we get a different number
        self._increment();

        #Make sure the value is between 0 and the maximum
        return (temp % self._seedMax) / float(self._seedMax)

    def ivalue(self):
        """Returns the current Seed value, between 0 and 1000"""
        #Save the current value of the Seed function
        temp = self._series[0];
        #Now increment the series so the next time we call the value we get a different number
        self._increment();

        #Make sure the value is between 0 and the maximum
        return (temp % self._seedMax)

    def _resetSeries(self):
        """This will reset the series so it does not overflow the unsigned long long int limit."""
        #Store the values of the series.
        s0 = self._series[0]
        s1 = self._series[1]

        #Mod each value by the max value for a seed. This resets the sequence to something more managable.
        self._series[0] = s0 % self._seedMax
        self._series[1] = s1 % self._seedMax

        #Tell us wtf is going on
        print("SERIES RESET!")

        #Reset the counter
        self._fCounter = 0



    def _increment(self):
        """Increment the value of the Fibonacci series."""
        #Check to make sure that the seed value will not overflow.
        if (self._series[0] >= self._dataMax): # Check to see if adding the lowest and the highest value of the series can overflow
            #Reset the series
            self._resetSeries()

        #Store the current series. The 0 element is the higher value (and current), the 1 element is the lower value.
        s0 = self._series[0];
        s1 = self._series[1];

        #Move the highest value into the second slot (the lowest value, index 1)
        self._series[1] = s0
        #Now add the lowest and highest values in order to get the new value, stored in the highest value slot (index 0)
        t = s0 + s1
        #Set the first element to the new value.
        self._series[0] = t
        #Update the counter for total number of fib's
        self._fCounter += 1

    def peek(self):
        return self._series[0]