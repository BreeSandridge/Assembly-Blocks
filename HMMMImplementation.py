from CommandTypes import *

class Jump(Exception):
    def __init__(self, dest):
        Exception.__init__(self)
        self.dest = dest

class Halt(Exception):
    pass

def executeInstructionList(cmdList):
    cmdPtr = 0
    while True:
        try:
            executeInstruction(cmdList[cmdPtr])
            cmdPtr += 1
        except IndexError:
            break
        except Halt:
            break
        except Jump as jump:
            cmdPtr = jump.dest
    
def executeInstruction(command):
    cmd = command.commandType
    cmdArgs = command.args
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
        raise Jump()
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
