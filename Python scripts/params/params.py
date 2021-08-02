def accepts(*types):
    def check_accepts(function):
        assert len(types) == function.__code__.co_argcount

        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), f'arg {a} does not match {t}'
            return function(*args, **kwds)
        return new_f
    return check_accepts


def returns(rtype):
    def check_returns(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), \
                f'return value {result} does not match {rtype}'
            return result
        return new_f
    return check_returns


NUMERIC = (int, float)
if __name__ == '__main__':
    @returns(NUMERIC)
    @accepts(NUMERIC, NUMERIC)
    def foo(num1, num2): return num1 * num2 / (num1 + num2)

    print(foo(2.716, 3.14159265))
