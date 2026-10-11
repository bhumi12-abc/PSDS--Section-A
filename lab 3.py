class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode
        print(data, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        print(self.top.data, "popped from stack")
        self.top = self.top.next


# Queue using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newnode = Node(data)

        if self.rear is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

        print(data, "inserted into queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        print(self.front.data, "deleted from queue")
        self.front = self.front.next

        if self.front is None:
            self.rear = None


# Main program
s = Stack()
print("STACK OPERATIONS")
s.push(10)
s.push(20)
s.push(30)
s.pop()

q = Queue()
print("\nQUEUE OPERATIONS")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()