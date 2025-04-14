from typing import Optional, List

class Node:
    """Base Node class for Linked List"""
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None

class LinkedListUtils:
    """Utility class containing common linked list operations"""
    
    @staticmethod
    def create_linked_list(arr: List[int]) -> Optional[Node]:
        """
        Create a linked list from an array
        Args:
            arr: List of integers
        Returns:
            Head node of the created linked list
        """
        try:
            if not arr:
                return None
            head = Node(arr[0])
            current = head
            for data in arr[1:]:
                current.next = Node(data)
                current = current.next
            return head
        except Exception as e:
            print(f"Error creating linked list: {e}")
            return None

    @staticmethod
    def print_linked_list(head: Optional[Node]) -> str:
        """
        Convert linked list to string representation
        Args:
            head: Head node of the linked list
        Returns:
            String representation of the linked list
        """
        try:
            if head is None:
                return "Empty list"
            current = head
            result = []
            while current:
                result.append(str(current.data))
                current = current.next
            return ' -> '.join(result)
        except Exception as e:
            return f"Error printing linked list: {e}"

    @staticmethod
    def get_length(head: Optional[Node]) -> int:
        """
        Get length of the linked list
        Args:
            head: Head node of the linked list
        Returns:
            Length of the linked list
        """
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    @staticmethod
    def get_middle_node(head: Optional[Node]) -> Optional[Node]:
        """
        Find middle node of the linked list using fast and slow pointer
        Args:
            head: Head node of the linked list
        Returns:
            Middle node of the linked list
        """
        if not head or not head.next:
            return head
            
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def insert_at_beginning(head: Optional[Node], data: int) -> Node:
        """
        Insert a new node at the beginning of the linked list
        Args:
            head: Head node of the linked list
            data: Data to be inserted
        Returns:
            New head of the linked list
        """
        new_node = Node(data)
        new_node.next = head
        return new_node

    @staticmethod
    def insert_at_end(head: Optional[Node], data: int) -> Optional[Node]:
        """
        Insert a new node at the end of the linked list
        Args:
            head: Head node of the linked list
            data: Data to be inserted
        Returns:
            Head of the linked list
        """
        if not head:
            return Node(data)
            
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)
        return head

    @staticmethod
    def delete_node(head: Optional[Node], key: int) -> Optional[Node]:
        """
        Delete first occurrence of a node with given key
        Args:
            head: Head node of the linked list
            key: Value to be deleted
        Returns:
            Head of the modified linked list
        """
        if not head:
            return None

        if head.data == key:
            return head.next

        current = head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                break
            current = current.next
        return head

# Example usage and test cases
def test_base_functions():
    ll = LinkedListUtils()
    
    # Test list creation and printing
    print("\nTest 1: Create and Print")
    test_list = ll.create_linked_list([1, 2, 3, 4, 5])
    print("Created List:", ll.print_linked_list(test_list))
    
    # Test length
    print("\nTest 2: Length")
    print("Length:", ll.get_length(test_list))
    
    # Test middle node
    print("\nTest 3: Middle Node")
    middle = ll.get_middle_node(test_list)
    print("Middle Node Value:", middle.data if middle else "None")
    
    # Test insertion at beginning
    print("\nTest 4: Insert at Beginning")
    test_list = ll.insert_at_beginning(test_list, 0)
    print("After insertion at beginning:", ll.print_linked_list(test_list))
    
    # Test insertion at end
    print("\nTest 5: Insert at End")
    test_list = ll.insert_at_end(test_list, 6)
    print("After insertion at end:", ll.print_linked_list(test_list))
    
    # Test deletion
    print("\nTest 6: Delete Node")
    test_list = ll.delete_node(test_list, 3)
    print("After deleting 3:", ll.print_linked_list(test_list))

if __name__ == "__main__":
    test_base_functions()
