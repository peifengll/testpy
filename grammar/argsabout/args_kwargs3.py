# MyClass作为类的名字
import functools
import logging


def log_arguments(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        auth wrapper method
        """
        if self.request:
            logging.info("x:%d y:%d ", self.x, self.y)
            # logging.info("%s %s (%s), %s; %s (%s & %s)", self.request.method,
            #              self.request.uri, self.request.remote_ip,
            #              self.request.body, self.request.query, args, kwargs)
        return method(self, *args, **kwargs)

    return wrapper


class MyClass:
    x = None
    y = None
    request = None

    # 函数 __init__用来录入参数 放在self里面
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.request = True

    # method_1函数，可以用上面__init__的参数，同时也可以自己另加参数使用
    @log_arguments
    def method_1(self, a):
        print("method_1 called")
        return a * self.x

    # method_2函数，同上。
    def method_2(self):
        return self.x


# 上面的类，名字为MyClass, 有两个函数 作为属性，可以直接调用，调用方法如下:
# 需要放入两个参数作为x，y的值，放入self里面
my_class = MyClass(1, 2)
# 调用类里面的函数 method_1
print(my_class.method_1(5))
# output如下
# method_1 called
# 5
