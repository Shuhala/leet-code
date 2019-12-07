# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        current_node = root
        while l1 and l2:
            if l1.val <= l2.val:
                current_node.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next

        if l1:
            current_node.next = l1
        elif l2:
            current_node.next = l2

        return root.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

result = ListNode(1)
result.next = ListNode(1)
result.next.next = ListNode(2)
result.next.next.next = ListNode(3)
result.next.next.next.next = ListNode(4)
result.next.next.next.next.next = ListNode(4)

solution = Solution()
assert result == solution.mergeTwoLists(list1, list2)
