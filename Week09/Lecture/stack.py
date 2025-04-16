class Stack:
    def __init__(self):
        self.myStack = []
    
    def push(self, elem):
        self.myStack.append(elem)
    
    def isEmpty(self):
        return len(self.myStack) == 0

    def peek(self):
        if not self.isEmpty():
            return self.myStack[-1]
        return None # stack is empty
    
    def pop(self):
        if self.isEmpty():
            return None
        removedElem = self.myStack.pop()
        return removedElem

    def printStack(self):
        print(self.myStack)

# main
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())
stack.push(30)
elem = stack.pop()
print(elem)
print(stack.peek())
stack.printStack()

