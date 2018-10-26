class BruteForceFibonacci(object):

    def __init__(self):
        self.cache = {}

    def recursive_implementation(self, n):
        """
        :param n: n-th number of fibonacci numbers
        :rtype: int
        :return: fibonacci number
        """

        if n < 0:
            raise TypeError('please enter positive numbers')

        if n in self.cache:
            ans = self.cache[n]
        elif n <= 2:
            ans = 1
            self.cache[n] = ans
        else:
            ans = self.recursive_implementation(n - 2) + self.recursive_implementation(n - 1)
            self.cache[n] = ans

        return ans