class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        # see what the last item is but don't actually remove it
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.elements})'


if __name__ == '__main__':
    s = Stack()
    s.push('blah')
    s.push(7)
    s.push({'zzz'})
    print(s)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s)
    print(s.size())
