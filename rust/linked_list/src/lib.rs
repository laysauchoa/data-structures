// <≧◉◡◉≦>
struct Node<T> where T: Copy {
  value: T,
  next: Option<Box<Node<T>>>
}

impl<T> Node<T> where T: Copy {

  pub fn new(value: T) -> Node<T> { 
    return Node{
      value: value,
      next: None
    };
  }

  fn add_recursively(&mut self, new_value: T) -> &mut Node<T> {
    match &mut self.next {
      None => self.next = Some(
        Box::new(Node::new(new_value))
      ),
      Some(next) => { next.add_recursively(new_value); () }
    };
    return self
  }

  // (⊙.⊙(☉̃ₒ☉)⊙.⊙)
  fn add_iteratively(&mut self, new_value: T) -> &mut Node<T> {
    let mut current_node :&mut Node<T> = self;
    while current_node.next.is_some() {
      current_node = current_node.next.as_mut().unwrap();
    }
    current_node.next = Some(Box::new(Node::new(new_value)));
    return self

  }

  // ( ͡° ͜ʖ ͡°)
  fn get_iteratively(&self, index: u32) -> Option<T> {

    let mut counter = 0 as u32;
    let mut res = self;

    while counter != index {
      if res.next.is_none() {
        return None;
      }
      res = res.next.as_ref().unwrap();
      counter = counter + 1;
    }
    return Some(res.value)
  }
}

