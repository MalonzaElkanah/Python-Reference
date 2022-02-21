'''
A Data structure is a particular way of organizing data in a computer so that it can be used effectively. It is a specialized format for organizing, processing, retrieving and storing data. Algorithm on the hand is a set of well-defined instructions in calculation or to solve a particular problem.

Common Data Structures in computer programming in general are:

    Stack - LIFO
    Queues - FIFO
    Linked Lists
    Hash Tables
    Trees
    Graphs
'''


'''

1. Stack

A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed. Stack has one end where the insertion and deletion happens i.e. from the top of the stack.
operation in stack data structures

    push() - Pushing (storing) an element on the stack
    pop() - Removing (accessing) an element from the stack
    peek() - get the top data element of the stack, without removing it.
    isEmpty() - check if stack is empty.
    isFull() - check if stack is full.

Example:
'''
# Creating a stack
def stack():
    stack = []
    return stack

# Creating an empty stack
def isEmpty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (isEmpty(stack)):
        return "stack is empty"

    return stack.pop()

stack = stack()
push(stack, "me")
push(stack, "we")
push(stack, "us")

print("popped item: " + pop(stack))
print("stack after popping an element: ", stack)

'''output
pushed item: me
pushed item: we
pushed item: us
popped item: us
stack after popping an element:  ['me', 'we']
'''




'''
2. Queues

A Queue is a linear data structure that follows the principle of First In First Out (FIFO). This means the first element inserted inside the stack is removed first. Stack has two end where one is for insertion (enqueue) and the other is for deletion (dequeue).
operations in queue data structure

    enqueue() − add (store) an item to the queue.     
    dequeue() − remove (access) an item from the queue.
    peek() − Gets the element at the front of the queue without removing it.     
    isFull() − Checks if the queue is full.     
    isEmpty() − Checks if the queue is empty. 

'''


#queues
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Check the first element in a Queue
    def peek(self):
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    # Check if the Queue is Empty
    def isEmpty(self):
        return len(self.queue) < 1

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(0)
q.enqueue(2)
q.enqueue(0)
q.enqueue(2)
q.enqueue(2)

q.peek()
q.display()

q.dequeue()

print("After removing an element")
q.peek()
q.display()

''' output
0
[0, 2, 0, 2, 2]
After removing an element
2
[2, 0, 2, 2]
'''



''''
linked list

linked list is a linear data structure where data are connected together via links. It consists of nodes where each node contains a data field and a reference(link) to the next node in the list.
Operations in linked list

    Insertion − Adds an element at the beginning of the list.     
    Deletion − Deletes an element at the beginning of the list.     
    Display − Displays the complete list.     
    Search − Searches an element using the given key.     
    Delete − Deletes an element using the given key. 
'''

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
'''output
Mon
Tue
Wed
'''



'''
4. Hash Tables

Hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.
In a hash table, data is stored in an array format, where each data value has its own unique index value. Access of data becomes very fast if we know the index of the desired data.

Operations in hash tables

    Search − Searches an element in a hash table.     
    Insert − inserts an element in a hash table.     
    delete − Deletes an element from a hash table. 
'''



# HashTable 
hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "make a circle")
insertData(456, "a big circle")
insertData(789, "like a sufuria")

print(hashTable)

removeData(123)

print(hashTable)

'''output
[[], [], [123, 'make a circle'], [], [], [456, 'a big circle'], [], [], [789, 'like a sufuria'], []]
[[], [], 0, [], [], [456, 'a big circle'], [], [], [789, 'like a sufuria'], []]
'''

