use std::fmt::Debug;
use std::iter::FromIterator;

pub struct Node<T> {
    data: T,
    next: Option<Box<Node<T>>>,
}
impl<T> Node<T> {
    pub fn new(value: T, next: Option<Box<Node<T>>>) -> Self {
        Node {
            data: value,
            next: next,
        }
    }
}

pub struct SimpleLinkedList<T> {
    head: Option<Box<Node<T>>>,
}

impl<T: Copy> Clone for SimpleLinkedList<T> {
    fn clone(&self) -> SimpleLinkedList<T> {
        let mut out: SimpleLinkedList<T> = SimpleLinkedList::new();
        let mut cur = &self.head;
        while let Some(node) = cur {
            cur = &node.next;
            out.push(node.data)
        }
        out
    }
}

impl<T> Default for SimpleLinkedList<T> {
    fn default() -> Self {
        SimpleLinkedList { head: None }
    }
}

impl<T> SimpleLinkedList<T> {
    pub fn new() -> Self {
        Default::default()
    }

    pub fn len(&self) -> usize {
        let mut size = 0 as usize;
        let mut current_node = self.head.as_ref();
        while let Some(node) = current_node {
            size = size + 1;
            current_node = (node.as_ref().next).as_ref();
        }
        return size;
    }

    pub fn push(&mut self, _element: T) -> () {
        let head = self.head.take();
        let mut new_node = Box::new(Node::new(_element, head));
        self.head = Some(new_node);
    }

    pub fn pop(&mut self) -> Option<T> {
        let mut res: Option<T> = None;
        if let Some(head_node) = self.head.take() {
            res = Some(head_node.data);
            self.head = head_node.next;
        } else {
            res = None;
        }
        return res;
    }

    pub fn peek(&self) -> Option<&T> {
        match &self.head {
            Some(node) => Some(&node.data),
            None => None,
        }
    }

    pub fn rev(self) -> SimpleLinkedList<T>
    where
        T: Copy,
    {
        let mut simple_linked_list = SimpleLinkedList::new();
        let mut current_node: Option<&Box<Node<T>>> = self.head.as_ref();

        while let Some(node) = current_node {
            simple_linked_list.push(node.data);
            current_node = node.next.as_ref();
        }
        return simple_linked_list;
    }
}

impl<T: Debug> FromIterator<T> for SimpleLinkedList<T> {
    fn from_iter<I: IntoIterator<Item = T>>(_iter: I) -> Self {
        let mut simple_linked_list = Self::new();
        _iter.into_iter().for_each(|x| simple_linked_list.push(x));
        return simple_linked_list;
    }
}

// In general, it would be preferable to implement IntoIterator for SimpleLinkedList<T>
// instead of implementing an explicit conversion to a vector. This is because, together,
// FromIterator and IntoIterator enable conversion between arbitrary collections.
// Given that implementation, converting to a vector is trivial:
//
// let vec: Vec<_> = simple_linked_list.into_iter().collect();
//
// The reason this exercise's API includes an explicit conversion to Vec<T> instead
// of IntoIterator is that implementing that interface is fairly complicated, and
// demands more of the student than we expect at this point in the track.

impl<T: Copy> Into<Vec<T>> for SimpleLinkedList<T> {
    fn into(self) -> Vec<T> {
        let mut vec_nodes: Vec<T> = vec![];
        let mut cp_simple_linked_list = self.clone();
        while let Some(head_node) = cp_simple_linked_list.head.as_ref() {
            vec_nodes.push(head_node.data);
            cp_simple_linked_list.pop();
        }
        return vec_nodes;
    }
}
