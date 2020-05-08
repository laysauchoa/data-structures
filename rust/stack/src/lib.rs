trait LIFO<T> {
    fn new() -> Self;
    fn push(&mut self, value: T) -> ();
    fn pop(&mut self) -> &Option<T>;
}

struct Stack<T> {
    stack_vec: [Box<Option<T>>; 3],
    index: Option<u32>,
}
impl<T> LIFO<T> for Stack<T> {
    fn new() -> Self {
        return Self {
            stack_vec: [Box::new(None), Box::new(None), Box::new(None)],
            index: None,
        };
    }
    fn push(&mut self, value: T) -> () {
        self.index = match self.index {
            None => {
                self.stack_vec[0] = Box::new(Some(value));
                Some(0)
            }
            Some(index) => {
                self.stack_vec[(index + 1) as usize] = Box::new(Some(value));
                Some(index + 1)
            }
        };
    }
    fn pop(&mut self) -> &Option<T> {
        println!("self.index {:?}", self.index);
        match self.index {
            None => {
                self.index = None;
                return &None;
            }
            Some(0) => {
                self.index = None;
                return &self.stack_vec[0];
            }
            Some(index) => {
                self.index = Some(index - 1);
                return &self.stack_vec[index as usize];
            }
        }
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_stack() {
        use super::*;
        let mut stack: Stack<u32> = Stack::new();
        stack.push(2);
        stack.push(42);

        assert_eq!(stack.pop(), &Some(42));
        assert_eq!(stack.pop(), &Some(2));
    }
}
