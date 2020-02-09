class CustomError(Exception):
    def __init__(self, n):
        Exception.__init__(self)
        self.n = n

try:
    raise CustomError(3)
except CustomError as c:
    print(c.n)
