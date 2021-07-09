from collections import deque


# don't use lists for queues, operations to remove from front are inefficient for lists
class Queue:
    # FIFO - first in, first out
    def __init__(self):
        self.elements = deque()

    def is_empty(self):
        return len(self.elements) == 0

    def enqueue(self, elem):
        # add to the end
        self.elements.append(elem)

    def dequeue(self):
        return self.elements.popleft()

    def size(self):
        return len(self.elements)

    def peek(self):
        # get the first item
        return self.elements[0]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.elements})'


if __name__ == '__main__':
    q = Queue()
    q.enqueue('blah')
    q.enqueue('blah2')
    print(q)
    q.dequeue()
    print(q)
    print(q.peek())
