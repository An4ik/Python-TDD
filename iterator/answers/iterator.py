"""  The iterator pattern is a design pattern in which an iterator
    is used to traverse a container and access the container's elements. Iterator in Python is simply
    an object that can be iterated upon. An object which will return data, one element at a time. Technically speaking,
    Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
    In our __next__ we condider fibonacci number. In mathematics, the Fibonacci numbers are the numbers in the following integer sequence,
    called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones:

    1 1 2 3 5 8 13 21

    Often, especially in modern usage, the sequence is extended by one more initial term:
    0 1 1 2 3 5 8 13 21


    GOOG LUCK!
"""

class Iterator:
    def __init__(self, maxIndex=0):

        """

        __init__ sets value in an object in value attribute.

        Attributes:
            lastValue - value which considered as a last number in the list.
            punultimateValue - value that located before the last value in the list.
            currentIndex -  the index of the number in the list.
            maxIndex - last value that we should calculate.

        """
        self.lastValue = 1
        self.punultimateValue  = 0
        self.currentIndex = 0
        self.maxIndex = maxIndex

    def __iter__(self):

        """
           The __iter__ method that makes an object iterable.

           Returns: self

        """
        return self

    def __next__(self):

        """
         __next__ method returns the next method of iteration.

         __next__ considers fibonacci number. You should write conditions for punultimateValue
         and currentIndex.
         Conditions:
         1. First condition checks the punultimate value and currentIndex of list. Sets 0 for
         punultimate value, adds one more index for currentIndex of list and returns punultimateValue.
         2. Second condition checks when last value is 1 and currentIndex in 1. Sets lastValue
         into punulatimatevalue, adds one index to currents value and returns punultimateValue
         3. Third conditions for conditions when maxIndex greater than currentIndex. Saves lastValue
         as temperory, add punultimateValue to lastValue, punultimate values takes temp, currentIndex adds 1
         and returns last Value
         4. Condition for stopping iteration.

        """

        if  self.punultimateValue==0 and self.currentIndex == 0:
            self.punultimateValue = 0
            self.currentIndex += 1
            return self.punultimateValue
        elif self.lastValue==1 and self.currentIndex == 1:
            self.punultimateValue = self.lastValue
            self.currentIndex += 1
            return self.punultimateValue
        elif self.currentIndex < self.maxIndex:
            temp = self.lastValue
            self.lastValue += self.punultimateValue
            self.punultimateValue = temp
            self.currentIndex += 1
            return self.lastValue
        else:
            raise StopIteration()







