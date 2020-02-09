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
        if d == 0:
            return Command(CommandTypes.LOADR, b, c)
        elif d == 1:
            return Command(CommandTypes.STORER, b, c)
        elif d == 2:
            return Command(CommandTypes.POPR, b, c)
        elif d == 3:
            return Command(CommandTypes.PUSHR, b, c)
    elif a == 5:
        return Command(CommandTypes.ADDN, b, e)
    elif a == 6:
        if d == 0:
            if b == 0 and c == 0:
                return Command(CommandTypes.NOP)
            else:
                return Command(CommandTypes.COPY, b, c)
        else:
            return Command(CommandTypes.ADD, b, c, d)
    elif a == 7:
        if c == 0:
            return Command(CommandTypes.NEG, b, d)
        else:
            return Command(CommandTypes.SUB, b, c, d)
    elif a == 8:
        return Command(CommandTypes.MUL, b, c, d)
    elif a == 9:
        return Command(CommandTypes.DIV, b, c, d)
    elif a == 10:
        return Command(CommandTypes.MOD, b, c, d)
    elif a == 11:
        if b == 0:
            return Command(CommandTypes.JUMPN, e)
        else:
            return Command(CommandTypes.CALLN, b)
    elif a == 12:
        return Command(CommandTypes.JEQZN, b, e)
    elif a == 13:
        return Command(CommandTypes.JNEZN, b, e)
    elif a == 14:
        return Command(CommandTypes.JGTZN, b, e)
    elif a == 15:
        return Command(CommandTypes.JLTZN, b, e)
