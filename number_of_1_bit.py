x = 11


class Solution(object):

    @staticmethod
    def hammingWeight(n):
        # unsigned 32b
        mask = 0xffffffff
        return bin(n & mask).count('1')

print Solution.hammingWeight(x)
