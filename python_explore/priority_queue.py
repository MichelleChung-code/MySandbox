import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, elem, priority):
        # push while preserving the order based on priority
        heapq.heappush(self.elements, (priority, elem))

    def get(self):
        # just return the elem, i.e. index 1 and not index 0 which is the priority value
        return heapq.heappop(self.elements)[1]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.elements})'

    def peek(self):
        # return the highest priority elem
        return self.elements[0][1]


if __name__ == '__main__':
    pq = PriorityQueue()

    # item, priority
    # higher priority is lower priority value i.e. 1 > 2

    pq.put('p2', 2)
    pq.put('p1', 1)
    pq.put('p3', 3)

    print(pq.peek())
    # print(pq.get())
    # print(pq.get())
    # print(pq.get())

    print(pq)
