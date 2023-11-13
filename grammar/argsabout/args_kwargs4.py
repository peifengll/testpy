# from time import sleep
#
#
# class Task:
#     def run(self):
#         print('任务开始执行')
#         sleep(1)
#         print('任务执行结束')
#
#
# task = Task()
# task.run()

#
# from time import sleep, time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         func(*args, **kwargs)
#         print(time() - start)
#
#     return wrapper
#
#
# class Task:
#     @timer
#     def run(self):
#         print('任务开始执行')
#         sleep(1)
#         print('任务执行结束')
#
#
# task = Task()
# task.run()

from time import sleep, time


def timer(func):
    def wrapper(self, *args, **kwargs):
        start = time()
        func(self, *args, **kwargs)
        print(time() - start)
        self.tasks += 1

    return wrapper


class Task:
    def __init__(self):
        self.tasks = 0

    @timer
    def run(self):
        print('任务开始执行')
        sleep(1)
        print('任务执行结束')


task = Task()
print(task.tasks)

task.run()
print(task.tasks)

task.run()
print(task.tasks)

task.run()
print(task.tasks)

task.run()
print(task.tasks)
