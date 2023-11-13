import sys
import functools

sys.path.append('D:/code/py/tests')
from grammar.n_Decorators.g2 import clock


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
