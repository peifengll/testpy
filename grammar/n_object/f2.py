# test2
class Root:
    def __init__(self):
        self.__func()

    def __func(self):
        print("root")


class Child(Root):
    def __func(self):
        print("child")

Child()
