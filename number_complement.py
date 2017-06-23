
class Solution(object):

    @staticmethod
    def findComplement(num):
        # mask everything
        mask = 0xFFFFFFFF

        # Convert int to 32b
        bin_value = '{0:032b}'.format(num)
        complement = '{0:032b}'.format(~num & mask)

        # Converts to an int
        return int(complement[bin_value.index('1'):],2)

    # Other solutions from others
    def _findComplement(self, num):
        return int("".join(["1" if ls == "0" else "0" for ls in "{0:b}".format(num)]), 2)

    def __findComplement(self, num):
        # ** = math.pow()
        return 2 ** (len(bin(num)) - 2) - num - 1


x1 = 1      # expected 0
x2 = 5      # expected 2
x3 = 23     # expected 8
x4 = 1111   # expected 936

print Solution.findComplement(1111)
