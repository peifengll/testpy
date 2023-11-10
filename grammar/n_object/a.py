class Test:
    def prt(self, sel):
        print(sel)
        print(sel.__class__)


t = Test()
t.prt(4)