from CommandTypes import *

cmd1 = CommandTypes.HALT

if cmd1 is CommandTypes.HALT:
    print("It's halt")

def executeInstructionList(cmdList):
    cmdPtr = 0
    while True:
        executeInstruction(cmdList[cmdPtr])
    
def executeInstruction(cmd):
    if cmd is CommandTypes.HALT:
        pass
    elif cmd is CommandTypes.READ:
        pass
    elif cmd is CommandTypes.WRITE:
        pass
    elif cmd is CommandTypes.NOP:
        pass
    elif cmd is CommandTypes.SETN:
        pass
    elif cmd is CommandTypes.ADDN:
        pass
    elif cmd is CommandTypes.COPY:
        pass
    elif cmd is CommandTypes.ADD:
        pass
    elif cmd is CommandTypes.SUB:
        pass
    elif cmd is CommandTypes.NEG:
        pass
    elif cmd is CommandTypes.MUL:
        pass
    elif cmd is CommandTypes.DIV:
        pass
    elif cmd is CommandTypes.MOD:
        pass
    elif cmd is CommandTypes.JUMPN:
        pass
    elif cmd is CommandTypes.JUMPR:
        pass
    elif cmd is CommandTypes.JEZQN:
        pass
    elif cmd is CommandTypes.JNEZN:
        pass
    elif cmd is CommandTypes.JGTZN:
        pass
    elif cmd is CommandTypes.JLTZN:
        pass
    elif cmd is CommandTypes.CALLN:
        pass
    elif cmd is CommandTypes.PUSHR:
        pass
    elif cmd is CommandTypes.POPR:
        pass
    elif cmd is CommandTypes.LOADN:
        pass
    elif cmd is CommandTypes.STOREN:
        pass
    elif cmd is CommandTypes.LOADR:
        pass
    elif cmd is CommandTypes.STORER:
        pass
