'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

'''

from base_function import Node, LinkedListUtils
from typing import Optional

def reverse_linked_list(head: Optional[Node]) -> Optional[Node]:
    if head is None or head.next is None:
        return head
        
    curr = head.next
    head.next = None
    
    while curr is not None:
        next = curr.next
        curr.next = head
        head = curr
        curr = next
        
    return head

# Test the reverse function
if __name__ == "__main__":
    ll = LinkedListUtils()
    
    # Create test cases
    test_cases = [
        [1, 2, 3, 4, 5],  # Normal case
        [1],              # Single node
        [1, 2],          # Two nodes
        []               # Empty list
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        head = ll.create_linked_list(test_case)
        print("Original:", ll.print_linked_list(head))
        reversed_head = reverse_linked_list(head)
        print("Reversed:", ll.print_linked_list(reversed_head))