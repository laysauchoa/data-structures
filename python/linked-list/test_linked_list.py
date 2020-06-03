import pytest

from linked_list import LinkedList

def test_get_head_node():
    linked_list = LinkedList()
    linked_list.insert_beginning(3)
    linked_list.insert_beginning(2)
    linked_list.insert_beginning(1)

    assert linked_list.get_head_node().get_value() == 1
def test_remove_node():
    linked_list = LinkedList()
    linked_list.insert_beginning(3)
    linked_list.insert_beginning(2)
    linked_list.insert_beginning(1)

    linked_list.remove_node(2)
    assert linked_list.get_head_node().get_value() == 1
    assert linked_list.get_head_node().get_next_node().get_value() == 3

def test_stringify_list():
    linked_list = LinkedList()
    linked_list.insert_beginning(3)
    linked_list.insert_beginning(2)
    linked_list.insert_beginning(1)

    assert linked_list.stringify_list() == '1,2,3'

def test_reverse_list():
    linked_list = LinkedList()
    linked_list.reverse_list()
    assert linked_list.stringify_list() == ''

    linked_list.insert_beginning(3)

    linked_list.reverse_list()
    assert linked_list.stringify_list() == '3'

    linked_list.insert_beginning(2)
    linked_list.insert_beginning(1)

    linked_list.reverse_list()
    assert linked_list.stringify_list() == '3,2,1'

def test_iscircular():

    list_with_loop = LinkedList()
    list_with_loop.insert_beginning(4)
    list_with_loop.insert_beginning(3)
    list_with_loop.insert_beginning(2)
    list_with_loop.insert_beginning(1)

    assert not list_with_loop.iscircular

    # Make the linked list circular
    current_node = list_with_loop.get_head_node()
    while current_node.get_next_node():
        current_node = current_node.get_next_node()
    current_node.set_next_node(list_with_loop.get_head_node().get_next_node())

    assert list_with_loop.iscircular
