from repr_str import repr_str


class Borg:
    _shared_state = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state  # Becomes an attribute dictionary


class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return repr_str(self, self._shared_state)


x = Singleton(Greeting='henlo')
y = Singleton(Name='fren')

# Will have both x and y
print(y)
assert str(y) == "Singleton({'Greeting': 'henlo', 'Name': 'fren'})"
