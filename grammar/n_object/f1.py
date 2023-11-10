# test1
class Root:
    def __init__(self):
        self.func()

    def func(self):
        print("root")


class Child(Root):
    def func(self):
        print("child")

Child()
