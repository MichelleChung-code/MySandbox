import string


class ManualRepeater:
    """ Class to explore what is going on in the background in Iterators """

    def __init__(self, value, iter_limit):
        """
        Args:
            value: value to yield on iteration
            iter_limit: <int> maximum times to iterate
        """
        self.value = value
        self.stop_limit = iter_limit
        self.counter = 0

    def __iter__(self):
        """ For returning the actual iterator object """
        return self

    def __next__(self):
        """ Get the actual value per iteration """
        if self.counter >= self.stop_limit:
            raise StopIteration

        # increment the counter
        self.counter += 1
        return self.value


def generator_function(value, iter_limit):
    """
    Args:
        value: value to yield on iteration
        iter_limit: <int> maximum number of iterations

    Returns: <generator>
    """
    for i in range(iter_limit):
        yield value


def get_alphabet():
    for i in string.ascii_lowercase:
        yield i


def make_upper(seq):
    for i in seq:
        yield i.upper()


def random_add_blah(seq):
    for i in seq:
        yield i + '_blah'.upper()


def chain_generators():
    # define generator functions first and then chain
    chain_1 = list(random_add_blah(make_upper(get_alphabet())))

    # just define and chain on the fly
    alpha_ls = list(string.ascii_lowercase)
    upper = (i.upper() for i in alpha_ls)
    chain_2 = list(i + '_blah'.upper() for i in upper)

    # check that both ways yield the same result
    assert chain_1 == chain_2


if __name__ == '__main__':
    # check that they all do the same thing
    repeater_res = [x for x in ManualRepeater('Michelle', 5)]
    gen_func_res = list(generator_function('Michelle', 5))
    gen_expr_res = list('Michelle' for i in range(5))

    assert repeater_res == gen_func_res == gen_expr_res

    # play with chaining generators
    chain_generators()
