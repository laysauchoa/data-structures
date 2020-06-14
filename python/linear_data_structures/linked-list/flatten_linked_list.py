from copy import deepcopy


class Node:
    def __init__(self, value):  # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, pass an integer as the "value" argument
    For creating a nested LinkedList, pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If head is None
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the current LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly created Node at the end of the current LinkedList
        node.next = Node(value)

    def remove(self):
        """ to be implemented """
        pass

    def to_list(self):
        """ Converts LinkedList into Python list of integers"""
        out = []
        node = self.head

        while node:
            print(node.value)
            out.append(int(str(node.value)))
            node = node.next

        return out


class NestedLinkedList(LinkedList):
    def flatten(self):
        # <-- self.head is a node for NestedLinkedList
        return self._flatten(self.head)

    '''  A recursive function '''

    def _flatten(self, node):

        # A termination condition
        if node.next is None:
            # <-- First argument is a simple LinkedList
            return merge(node.value, None)

        # _flatten() is calling itself untill a termination condition is achieved
        # <-- Both arguments are a simple LinkedList each
        return merge(node.value, self._flatten(node.next))


def merge(list1, list2):

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    head1 = list1.head
    head2 = list2.head
    res = LinkedList(None)

    while head1 and head2:
        if head1.value < head2.value:
            res.append(head1)
            head1 = head1.next
            merge(LinkedList(head1), LinkedList(head2))
        else:
            res.append(head2)
            head2 = head2.next
            merge(LinkedList(head1), LinkedList(head2))

    if head1 is None and head2:
        res.append(head2)
    if head2 is None and head1:
        res.append(head1)
    return res

