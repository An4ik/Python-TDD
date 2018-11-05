"""
    The iterator pattern is a design pattern in which an iterator
    is used to traverse a container and access the container's elements. Iterator in Python is simply
    an object that can be iterated upon. An object which will return data, one element at a time.

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
        

    def __iter__(self):

        """
           The __iter__ method that makes an object iterable.

           Returns: self

        """
     

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

     







