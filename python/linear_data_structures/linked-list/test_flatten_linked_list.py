import pytest
from flatten_linked_list import LinkedList, merge, Node, NestedLinkedList

def test_with_nones():
    linked_list = None
    second_linked_list = None

    merged = merge(None, None)
    res = []
    assert merged is None

def test_merge_with_none():

    linked_list = LinkedList(Node(1))
    linked_list.append(3)
    linked_list.append(5)

    merged = merge(linked_list, None)
    res = []
    node = merged.head
    while node is not None:
        res.append(node.value)
        node = node.next
    assert res == [1,3,5]

def test_merge_with_two_linked_list():
    linked_list = LinkedList(Node(1))
    linked_list.append(3)
    linked_list.append(5)

    second_linked_list = LinkedList(Node(2))
    second_linked_list.append(4)

    merged = merge(linked_list, second_linked_list)

    assert merged.to_list() == [1, 2, 3, 4, 5]

def test_neste_linked_list():
    linked_list = LinkedList(Node(1))
    second_linked_list = LinkedList(Node(2))
    third_linked_list = LinkedList(Node(3))

    nested_linked_list = NestedLinkedList(Node(linked_list))
    nested_linked_list.append(second_linked_list)

    nested_linked_list.append(third_linked_list)

    flattened = nested_linked_list.flatten()

    assert flattened.to_list() == [1, 2]


