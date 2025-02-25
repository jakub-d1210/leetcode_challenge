from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        pointer = l3
        carry = 0
        
     
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            l3_val = l1_val + l2_val + carry
            carry = l3_val // 10
            new_node = ListNode(l3_val % 10)
            

            pointer.next = new_node
            pointer = pointer.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return l3.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
l4 = ListNode()

print(f'type of l1 {type(l1)}')
print_list(l1)
print(f'type of l4 {type(l4)}')
print_list(l4)


solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the resulting linked list
print_list(result)


