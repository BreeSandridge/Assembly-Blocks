from CommandTypes import *
from Command import *
import numpy as np
import sys

registers = np.ndarray(16, dtype=np.uint16)
memory = np.ndarray(256, dtype=np.uint16)

class Jump(Exception):
    def __init__(self, dest):
        Exception.__init__(self)
        self.dest = dest

class Halt(Exception):
    pass

def runProgram(cmdList):
    cmdPtr = 0
    while True:
        try:
            executeInstruction(cmdList[cmdPtr])
            cmdPtr += 1
        except Jump as jump:
            cmdPtr = jump.dest
        except IndexError:
            print("Error: instruction out of bounds. Either you have written a bad JUMP statement or you have not put a HALT command at the end of the program.")
            break
        except AssertionError:
            print("Error: command", cmdPtr, "was called with an invalid number of arguments.")
            break
        except ValueError:
            print("Error: command", cmdPtr, "contains an invalid argument (wrong type or out of range).")
            break
        except Halt:
            break
    
def executeInstruction(command):
    cmd = command.commandType
    cmdArgs = command.args
    numArgs = len(cmdArgs)
    #print(cmd, cmdArgs)
    if cmd is CommandTypes.HALT:
        assert numArgs == 0
        raise Halt
    elif cmd is CommandTypes.READ:
        assert numArgs == 1
        registers[cmdArgs[0]] = int(input(""))        
    elif cmd is CommandTypes.WRITE:
        assert numArgs == 1
        print(registers[cmdArgs[0]])
    elif cmd is CommandTypes.NOP:
        assert numArgs == 0
        pass
    elif cmd is CommandTypes.SETN:
        assert numArgs == 2
        registers[cmdArgs[0]] = cmdArgs[1]
    elif cmd is CommandTypes.ADDN:
        assert numArgs == 2
        registers[cmdArgs[0]] += cmdArgs[1]
    elif cmd is CommandTypes.COPY:
        assert numArgs == 2
        registers[cmdArgs[0]] = registers[cmdArgs[1]]
    elif cmd is CommandTypes.ADD:
        assert numArgs == 3
        registers[cmdArgs[0]] = registers[cmdArgs[1]]+registers[cmdArgs[2]]
    elif cmd is CommandTypes.SUB:
        assert numArgs == 3
        registers[cmdArgs[0]] = registers[cmdArgs[1]]-registers[cmdArgs[2]]
    elif cmd is CommandTypes.NEG:
        assert numArgs == 2
        registers[cmdArgs[0]] = -registers[cmdArgs[1]]
    elif cmd is CommandTypes.MUL:
        assert numArgs == 3
        registers[cmdArgs[0]] = registers[cmdArgs[1]]*registers[cmdArgs[2]]
    elif cmd is CommandTypes.DIV:
        assert numArgs == 3
        registers[cmdArgs[0]] = registers[cmdArgs[1]]//registers[cmdArgs[2]]
    elif cmd is CommandTypes.MOD:
        assert numArgs == 3
        registers[cmdArgs[0]] = registers[cmdArgs[1]]%registers[cmdArgs[2]]
    elif cmd is CommandTypes.JUMPN:
        assert numArgs == 1
        raise Jump(cmdArgs[0])
    elif cmd is CommandTypes.JUMPR:
        assert numArgs == 1
        raise Jump(registers[cmdArgs[0]])
    elif cmd is CommandTypes.JEZQN:
        assert numArgs == 2
        if (registers[cmdArgs[0]] == 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.JNEZN:
        assert numArgs == 2
        if (registers[cmdArgs[0]] != 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.JGTZN:
        assert numArgs == 2
        if (registers[cmdArgs[0]] > 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.JLTZN:
        assert numArgs == 2
        if (registers[cmdArgs[0]] < 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.CALLN:
        assert numArgs == 2 # Forget this for now
    elif cmd is CommandTypes.PUSHR:
        assert numArgs == 2
        memory[registers[cmdArgs[1]]] = registers[cmdArgs[0]]
        registers[cmdArgs[1]] += 1
    elif cmd is CommandTypes.POPR:
        assert numArgs == 2
        registers[cmdArgs[1]] -= 1
        registers[cmdArgs[0]] = memory[registers[cmdArgs[1]]]
    elif cmd is CommandTypes.LOADN:
        assert numArgs == 2
        registers[cmdArgs[0]] = memory[cmdArgs[1]]
    elif cmd is CommandTypes.STOREN:
        assert numArgs == 2
        memory[cmdArgs[1]] = registers[cmdArgs[0]]
    elif cmd is CommandTypes.LOADR:
        assert numArgs == 2
        registers[cmdArgs[0]] = memory[registers[cmdArgs[1]]]
    elif cmd is CommandTypes.STORER:
        assert numArgs == 2
        memory[registers[cmdArgs[1]]] = registers[cmdArgs[0]]
    else:
        print("Unrecognized command", cmd)
