import time


def clock(func):
    def clocked(*args):  # ➊
        t0 = time.perf_counter()
        result = func(*args)  # ➋
        elapsed = time.perf_counter()
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s)->%r' % (elapsed, name, arg_str, result))
        return result

    return clocked  # ➌
