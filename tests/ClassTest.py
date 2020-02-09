class TestClass():
    def __init__(self, n):
        self.n = n

l = [TestClass(x) for x in range(10)]

for c in l:
    print(c.n)
