# Test3

class Root:
    def _func(self):
        print('root')

class Child(Root):
    def __init__(self):
        self._func()
Child()
