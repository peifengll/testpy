def foo(self, *args, **kwargs):
    if self.request:
        print()
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('---------------------------------------')


if __name__ == '__main__':
    foo(1, 2, 3, 4)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, 4, a=1, b=2, c=3)
    foo('a', 1, None, a=1, b='2', c=3)
    # foo(a=1, b='2', c=3, a, 1, None, )
# ╰─ python args_kwargs.py
#   File "D:\code\py\tests\grammar\argsabout\args_kwargs.py", line 12
#     foo(a=1, b='2', c=3, a, 1, None, )
#                                      ^
# SyntaxError: positional argument follows keyword argument
#
