# Definition for a binary tree node.
from typing import List
from utils import print_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return

        mid = len(nums) // 2

        # mid is element of the root
        root = TreeNode(nums[mid])

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(nums[:mid])

        # right subtree of root has all
        # values >arr[mid]
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


solution = Solution()
res = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
print_tree(res)
