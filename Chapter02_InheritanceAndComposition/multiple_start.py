# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Name_A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Name_B"


class C(A, B):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.bar)
        print(self.foo)
        print(self.name)



c = C()
c.showprops()
print(C.__mro__)  # Method Resoltuion Order