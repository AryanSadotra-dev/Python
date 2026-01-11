#Write a program to implement a Stack data structure.
#Stack is a Last In First Out (LIFO) list in which addition and deletion takes place at the same end.

#1.
stack = []
#2.- push - append() then pop - pop()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
