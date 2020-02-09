from CommandTypes import *
from Command import *

def addZeros(numString, maxLength):
    temp = numString
    while len(temp) < maxLength:
        temp = "0" + temp

    return temp


def cmdToNum(cmd):
    if cmd.commandType == CommandTypes.HALT:
        #0000 0000 0000 0000
        return int("0000" + "0000" + "0000" + "0000")
    elif  cmd.commandType == CommandTypes.READ:
        return int("0000" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + "0000" + "0001", 2)
    elif cmd.commandType == CommandTypes.WRITE:
        #0000 XXXX 0000 0010
        return int("0000" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + "0000" + "0010", 2)
    elif cmd.commandType == CommandTypes.NOP:
        #0110 0000 0000 0000
        return  int("0110" + "0000" + "0000" + "0000")
    elif cmd.commandType == CommandTypes.SETN:
        #0001 XXXX #### ####
        return int("0001" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 8), 2)
    elif cmd.commandType == CommandTypes.LOADR:
        #0100 XXXX YYYY 0000
        return int("0100" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + "0000", 2)
    elif cmd.commandType == CommandTypes.STORER:
        #0100 XXXX YYYY 0001
        return int("0100" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + "0001", 2)
    elif cmd.commandType == CommandTypes.POPR:
        #0100 XXXX YYYY 0010
        return int("0100" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + "0010", 2)
    elif cmd.commandType == CommandTypes.PUSHR:
        #0100 XXXX YYYY 0011
        return int("0100" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + "0011", 2)
    elif cmd.commandType == CommandTypes.LOADN:
        #0010 XXXX #### ####
        return int("0010" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]), 8).replace("0b", ""), 2)
    elif cmd.commandType == CommandTypes.STOREN:
        #0011 XXXX #### ####
        return int("0011" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 8), 2)
    elif cmd.commandType == CommandTypes.ADDN:
        #0101 XXXX #### ####
        return int("0101" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 8), 2)
    elif cmd.commandType == CommandTypes.COPY:
        #0110 XXXX YYYY 0000
        return int("0110" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + "0000", 2)
    elif cmd.commandType == CommandTypes.NEG:
        #0111 XXXX 0000 YYYY
        return int("0111" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + "0000" + addZeros(bin(cmd.args[1]).replace("0b", ""), 4), 2)
    elif cmd.commandType == CommandTypes.ADD:
        #0110 XXXX YYYY ZZZZ
        return int("0110" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + addZeros(bin(cmd.args[2]).replace("0b", ""), 4), 2)
    elif cmd.commandType == CommandTypes.SUB:
        #0111 XXXX YYYY ZZZZ
        return int("0111" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + addZeros(bin(cmd.args[2]).replace("0b", ""), 4), 2)
    elif cmd.commandType == CommandTypes.MUL:
        #1000 XXXX YYYY ZZZZ
        return int("1000" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + addZeros(bin(cmd.args[2]).replace("0b", ""), 4), 2)
    elif cmd.commandType == CommandTypes.DIV:
        #1001 XXXX YYYY ZZZZ
        return int("1001" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + addZeros(bin(cmd.args[2]).replace("0b", ""), 4), 2)
    elif cmd.commandType == CommandTypes.MOD:
        #1010 XXXX YYYY ZZZZ
        return int("1010" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4) + addZeros(bin(cmd.args[2]).replace("0b", ""), 4), 2)
    elif cmd.commandType == CommandTypes.JUMPR:
        #0000 XXXX 0000 0011
        return int("0000" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + "0000" + "0011", 2)
    elif cmd.commandType == CommandTypes.JUMPN:
        #1011 0000 #### ####
        return int("1011" + "0000" + addZeros(bin(cmd.args[0]).replace("0b", ""), 8), 2)
    elif cmd.commandType == CommandTypes.JEQZN:
        #1100 XXXX #### ####
        return int("1100" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 8), 2)
    elif cmd.commandType == CommandTypes.JNEZN:
        #1101 XXXX #### ####
        return int("1101" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 8), 2)
    elif cmd.commandType == CommandTypes.JGTZN:
        #1110 XXXX #### ####
        return int("1110" + addZeros(bin(cmd.args[0]).replace("0b", ""), 4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 8), 2)
    elif cmd.commandType == CommandTypes.JLTZN:
        #1111 XXXX #### ####
        return int("1111" + addZeros(bin(cmd.args[0]).replace("0b", ""),4) + addZeros(bin(cmd.args[1]).replace("0b", ""), 4), 2)
    elif cmd.commandType == CommandTypes.CALLN:
        #1011 XXXX 0000 0000
        return int("1011" + addZeros(bin(cmd.args[0]).replace("0b", ""),4) + "0000" + "0000", 2)


def numToCmd(n):
    e = n&255
    d = n&15
    c = (n>>4)&15
    b = (n>>8)&15
    a = (n>>12)&15
    #print(a, b, c, d)
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
