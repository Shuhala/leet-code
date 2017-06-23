
class Solution(object):

    @staticmethod
    def reverse(x):
        mask = 0xFFFFFFFF

        # Convert int to 32b
        bin_value = '{0:032b}'.format(x)
        complement = '{0:032b}'.format(~x & mask)
        print complement

        # Converts to an int
        return int(complement[bin_value.index('1'):],2)



x1 = 43261596      # expected 964176192

print Solution.reverse(x1)

# 00000010100101000001111010011100
# 00000010100101000001111010011100

# 11111101011010111110000101100011
# 00111001011110000010100101000000
