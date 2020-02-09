from Command import *
import sys
from HMMMImplementation import *
from CommandTypes import *

def strToType(head):
    if head == " halt":
        type = CommandTypes.HALT
    elif head == "read":
        type = CommandTypes.READ
    elif head == "write":
        type = CommandTypes.WRITE
    elif head == "nop":
        type = CommandTypes.NOP
    elif head == "setn":
        type = CommandTypes.SETN
    elif head == "addn":
        type = CommandTypes.ADDN
    elif head == "copy":
        type = CommandTypes.COPY
    elif head == "add":
        type = CommandTypes.ADD
    elif head == "sub":
        type = CommandTypes.SUB
    elif head == "neg":
        type = CommandTypes.NEG
    elif head == "mul":
        type = CommandTypes.MUL
    elif head == "div":
        type = CommandTypes.DIV
    elif head == "mod":
        type = CommandTypes.MOD
    elif head == "jumpn":
        type = CommandTypes.JUMPN
    elif head == "jumpr":
        type = CommandTypes.JUMPR
    elif head == "jeqzn":
        type = CommandTypes.JEQZN
    elif head == "jnezn":
        type = CommandTypes.JNEZN
    elif head == "jgtzn":
        type = CommandTypes.JGTZN
    elif head == "jltzn":
        type = CommandTypes.JLTZN
    elif head == "calln":
        type = CommandTypes.CALLN
    elif head == "pushr":
        type = CommandTypes.PUSHR
    elif head == "popr":
        type = CommandTypes.POPR
    elif head == "loadn":
        type = CommandTypes.LOADN
    elif head == "storen":
        type = CommandTypes.STOREN
    elif head == "loadr":
        type = CommandTypes.LOADR
    else:
        type = CommandTypes.STORER
    return type

path = sys.argv[1]
raw = open(path).read()
lines = raw.split("\n")
if lines[-1] == '':
    lines = lines[:-1]
prgm = []
for line in lines:
    words = line.split(" ")
    cmdType = strToType(words[0])
    args = [int(word) for word in words[1:]]
    newCmd = Command(cmdType, *args)
    prgm.append(newCmd)

runProgram(prgm)
