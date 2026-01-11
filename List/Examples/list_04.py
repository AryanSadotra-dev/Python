"""
Write a program to implement a Queue data structure.
Queue is a First In First Out (FIFO) list, 
in which addition takes place at the rear end of the queue and deletion takes place at the front end of the queue.
"""
import collections
Queue = collections.deque()
"""
import collections - collections is a built-in Python module
It provides special data structures better than normal lists for some tasks One of them is deque"""
#2. addition = append(), deletion = popleft()
Queue.append('Arun')
Queue.append(27)
Queue.append("sahil")
Queue.append(67)
Queue.append(45)
Queue.append("aryan")
Queue.append('Kaju')
print(Queue)

print(Queue.popleft())
print(Queue.popleft())
print(Queue.popleft())
print(Queue.popleft())

print(Queue)