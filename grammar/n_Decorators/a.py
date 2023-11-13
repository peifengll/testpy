def deco(func):
    def inner():
        print('running inner（　）')

    return inner


@deco
def target():
    print('running target（　）')


target()

deco(target)()

'''严格来说，装饰器只是语法糖。如前所示，装饰器可以像常规的可调用对象那样调用，
其参数是另一个函数。有时，这样做更方便，尤其是做元编程（在运行时改变程序的行为）时。'''
