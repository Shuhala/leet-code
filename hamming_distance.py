x = 1
y = 4

class Solution(object):

    @staticmethod
    def hammingDistance(x, y):

        # bin converts to binary
        # ^ is a XOR operator
        # 0 0 0 1 ^ 0 1 0 0 = 0 1 0 1
        return bin(x^y).count('1')

print Solution.hammingDistance(x,y)
print bin(x)
print bin(y)
print bin(x^y)
