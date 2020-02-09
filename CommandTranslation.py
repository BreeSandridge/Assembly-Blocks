from CommandTypes import *
from Command import *

def numToCmd(n):
    e = n&255
    d = n&15
    c = (n>>4)&15
    b = (n>>8)&15
    a = (n>>12)&15
    if a == 0:
        if d == 0:
            return Command(CommandTypes.HALT)
        elif d == 1:
            return Command(CommandTypes.READ, b)
        elif d == 2:
            return Command(CommandTypes.WRITE, b)
        elif d == 3:
            return Command(CommandTypes.JUMP, b)
        else:
            raise ValueError
    elif a == 1:
        return Command(CommandTypes.SETN, b, e)
    elif a == 2:
        return Command(CommandTypes.LOADN, b, e)
    elif a == 3:
        return Command(CommandTypes.STOREN, b, e)
    elif a == 4:
        
