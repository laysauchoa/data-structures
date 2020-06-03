# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + ","
            current_node = current_node.get_next_node()
        return string_list[:-1]

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        previous_node = Node(None, None)
        if current_node.value == value_to_remove:
            self.head_node = current_node.next_node
            current_node.set_next_node(None)
            return
        while current_node != None:
            if current_node.value == value_to_remove:
                previous_node.set_next_node(current_node.next_node)
                current_node.next_node = None
                return
            else:
                previous_node = current_node
                current_node = current_node.next_node
                continue

    def reverse_list(self):
        """
        Reverse the self linked list
        """
        # Time complexity O(N)
        # Space Complexity: O(1)
        current_node = self.get_head_node()
        if current_node.get_next_node() is None or current_node is None:
            return current_node
        self.head_node = current_node.next_node
        self.reverse_list()
        current_node.next_node.set_next_node(current_node)
        current_node.set_next_node(None)

    # detecting Loops in Linked Lists
    @property
    def iscircular(self):
        """
        Determine whether the Linked List is circular or not

        Args:
        self(obj): Linked List to be checked
        Returns:
        bool: Return True if the linked list is circular, return False otherwise
        """
        fast_pointer = self.get_head_node()
        slow_pointer = self.get_head_node()

        if self.get_head_node() is None:
            return True

        while fast_pointer and fast_pointer.get_next_node():
            fast_pointer = fast_pointer.get_next_node().get_next_node()
            slow_pointer = slow_pointer.get_next_node()
            if slow_pointer == fast_pointer:
                return True

        return False


if __name__ == "__main__":
    la = LinkedList(4)
    la.insert_beginning(3)
    la.insert_beginning(2)
    la.insert_beginning(1)

    print(la.stringify_list())
    la.reverse_list()
    print(la.stringify_list())
    list_with_loop = LinkedList([2, -1, 3, 0, 5])
    print("Before turn Linked List circular", la.iscircular)

    current_node = la.get_head_node()
    while current_node.get_next_node():
        current_node = current_node.get_next_node()
    current_node.set_next_node(la.get_head_node().get_next_node())
    print("Before turn Linked List circular", la.iscircular)
    
    print("After turning Linked List", la.iscircular)
    empty_linked_list = LinkedList()
    print("Empty Linked list", empty_linked_list.iscircular)
