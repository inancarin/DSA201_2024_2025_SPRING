from stack import Stack
from collections import deque

def checkExpression_v2(s):
    myStack = deque()

    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    for ch in s:
        if ch in "({[":
            myStack.append(ch)
        else:
            if not myStack:
                return False
            if myStack[-1] == d[ch]:
                myStack.pop()
            else:
                return False
    
    if myStack:
        return False
    return True

def checkExpression(s):
    stack = Stack()

    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    for ch in s:
        if ch in "({[":
            stack.push(ch)
        else:
            if stack.isEmpty():
                return False
            if stack.peek() == d[ch]:
                stack.pop()
            else:
                return False
    
    return stack.isEmpty()


s = input("Enter a string: ")
print(checkExpression_v2(s)) # (((([()])))){({})}