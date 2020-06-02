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

# Our LinkedList class


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
        return string_list

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
        current_node = self.get_head_node()
        if current_node.get_next_node() is None:
            self.head_node = current_node
            return current_node
        self.head_node = current_node.next_node
        self.reverse_list()
        current_node.next_node.set_next_node(current_node)
        current_node.set_next_node(None)
        return


if __name__ == "__main__":
    la = LinkedList(4)
    la.insert_beginning(3)
    la.insert_beginning(2)
    la.insert_beginning(1)

    print(la.stringify_list())
    la.reverse_list()
    print(la.stringify_list())
