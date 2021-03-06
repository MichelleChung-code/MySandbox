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


if __name__ == '__main__':
    pq = PriorityQueue()

    # item, priority
    # higher priority is lower priority value i.e. 1 > 2

    pq.put('p2', 2)
    pq.put('p1', 1)
    pq.put('p4', 4)
    pq.put('p3', 3)
    # order only guarentees that the first element is the highest priority
    # the following returns PriorityQueue([(1, 'p1'), (2, 'p2'), (4, 'p4'), (3, 'p3')])
    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())

    print(pq)
