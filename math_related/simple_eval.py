def eval_integer(num, inner):
    if not inner:
        return str(num)
    else:
        return eval(f"{num} {inner}")


def zero(inner=False):
    return eval_integer(0, inner)


def one(inner=False):
    return eval_integer(1, inner)


def two(inner=False):
    return eval_integer(2, inner)


def three(inner=False):
    return eval_integer(3, inner)


def four(inner=False):
    return eval_integer(4, inner)


def five(inner=False):
    return eval_integer(5, inner)


def six(inner=False):
    return eval_integer(6, inner)


def seven(inner=False):
    return eval_integer(7, inner)


def eight(inner=False):
    return eval_integer(8, inner)


def nine(inner=False):
    return eval_integer(9, inner)


def plus(inner):
    return f'+ {inner}'


def minus(inner):
    return f'- {inner}'


def times(inner):
    return f'* {inner}'


def divided_by(inner):
    # integer or floor division
    return f'// {inner}'


if __name__ == '__main__':
    res = seven(times(five()))
    print(res)
