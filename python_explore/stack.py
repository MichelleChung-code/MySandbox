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
    word = 'Michelle'
    s = Stack()
    for w in word:
        s.push(w)

    sol = ''
    while not s.is_empty():
        sol += s.pop()

    # reverse a string with a stack
    assert sol == word[::-1]