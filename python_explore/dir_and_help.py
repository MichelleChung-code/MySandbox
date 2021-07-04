class BlahBlahBlah:
    def __init__(self, a, b, c):
        """
        Random class for testing

        Args:
            a: <int> jkhdsahdasjhiu
            b: <float> jhkfdjkhfdhjkfdkhj
            c: <str> auhsdkihuasdiuoshijuk
        """
        self.a = a
        self.b = b
        self.c = c


if __name__ == '__main__':
    print(dir(BlahBlahBlah))
    # dir() gives back the functions, classes, methods, attributes available on BlahBlahBlah
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
    # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

    print(help(BlahBlahBlah))

    # help() auto-generates the following documentation on class BlahBlahBlah lol

    """
    Help on class BlahBlahBlah in module __main__:

class BlahBlahBlah(builtins.object)
 |  BlahBlahBlah(a, b, c)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, a, b, c)
 |      Random class for testing
 |      
 |      Args:
 |          a: <int> jkhdsahdasjhiu
 |          b: <float> jhkfdjkhfdhjkfdkhj
 |          c: <str> auhsdkihuasdiuoshijuk
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

    """
