import functools


def user_login_data(f):
    """
    注释掉下边这个看不同
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


@user_login_data
def num1():
    print("aaa")


if __name__ == '__main__':
    print(num1.__name__)

# ╰─ python functools_wraps_test.py
# wrapper

# ╰─ python functools_wraps_test.py
# num1
