class Test:
    def __init__(self, obj):
        self.obj = obj
    def __add__(self, other):
        # return self.obj + other.obj
        # return self.obj / other.obj
        # return self.obj - other.obj
        return self.obj * other.obj

t1 = Test(10)
t2 = Test(20)

print(t1+t2)


class OverL:
    def __init__(self, obj):
        self.obj = obj
    def __eq__(self, other):
        return self.obj == other.obj

p1 = OverL("venu")
p2 = OverL("gopi")
print(p1==p2)

