from Command import *
from CommandTypes import *
from CommandTranslation import *
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
    registers.fill(0)
    memory.fill(0)
    for i in range(len(cmdList)):
        memory[i] = cmdToNum(cmdList[i])
    while True:
        cmdPtr = registers[0]
        try:
            executeInstruction(numToCmd(memory[cmdPtr]))
            registers[0] += 1
        except Jump as jump:
            registers[0] = jump.dest
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
    
def setReg(x, n):
    if x != 0:
        registers[x] = n

def getReg(x, n):
    if x == 0:
        return 0
    else
        return registers[x]

def executeInstruction(command):
    cmd = command.commandType
    cmdArgs = command.args
    numArgs = len(cmdArgs)
    if cmd is CommandTypes.HALT:
        assert numArgs == 0
        raise Halt
    elif cmd is CommandTypes.READ:
        assert numArgs == 1
        setReg(cmdArgs[0], int(input("")))        
    elif cmd is CommandTypes.WRITE:
        assert numArgs == 1
        print(getReg(cmdArgs[0]))
    elif cmd is CommandTypes.NOP:
        assert numArgs == 0
        pass
    elif cmd is CommandTypes.SETN:
        assert numArgs == 2
        setReg(cmdArgs[0], cmdArgs[1])
    elif cmd is CommandTypes.ADDN:
        assert numArgs == 2
        setReg(cmdArgs[0], getReg(cmdArgs[0])+cmdArgs[1])
    elif cmd is CommandTypes.COPY:
        assert numArgs == 2
        setReg(cmdArgs[0], getReg(cmdArgs[1]))
    elif cmd is CommandTypes.ADD:
        assert numArgs == 3
        setReg(cmdArgs[0], getReg(cmdArgs[1])+getReg(cmdArgs[2]))
    elif cmd is CommandTypes.SUB:
        assert numArgs == 3
        setReg(cmdArgs[0], getReg(cmdArgs[1])-getReg(cmdArgs[2]))
    elif cmd is CommandTypes.NEG:
        assert numArgs == 2
        setReg(cmdArgs[0], -getReg(cmdArgs[1]))
    elif cmd is CommandTypes.MUL:
        assert numArgs == 3
        setReg(cmdArgs[0], getReg(cmdArgs[1])*getReg(cmdArgs[2]))
    elif cmd is CommandTypes.DIV:
        assert numArgs == 3
        setReg(cmdArgs[0], getReg(cmdArgs[1])//getReg(cmdArgs[2]))
    elif cmd is CommandTypes.MOD:
        assert numArgs == 3
        setReg(cmdArgs[0], getReg(cmdArgs[1])%getReg(cmdArgs[2]))
    elif cmd is CommandTypes.JUMPN:
        assert numArgs == 1
        raise Jump(cmdArgs[0])
    elif cmd is CommandTypes.JUMPR:
        assert numArgs == 1
        raise Jump(getReg(cmdArgs[0]))
    elif cmd is CommandTypes.JEZQN:
        assert numArgs == 2
        if (getReg(cmdArgs[0]) == 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.JNEZN:
        assert numArgs == 2
        if (getReg(cmdArgs[0]) != 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.JGTZN:
        assert numArgs == 2
        if (getReg(cmdArgs[0]) > 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.JLTZN:
        assert numArgs == 2
        if (getReg(cmdArgs[0]) < 0):
            raise Jump(cmdArgs[1])
    elif cmd is CommandTypes.CALLN:
        assert numArgs == 2 # Forget this for now
    elif cmd is CommandTypes.PUSHR:
        assert numArgs == 2
        memory[getReg(cmdArgs[1])] = getReg(cmdArgs[0])
        setReg(cmdArgs[1], getReg(cmdArgs[1])+1)
    elif cmd is CommandTypes.POPR:
        assert numArgs == 2
        setReg(cmdArgs[1], getReg(cmdArgs[1])-1)
        setReg(cmdArgs[0], memory[getReg(cmdArgs[1])])
    elif cmd is CommandTypes.LOADN:
        assert numArgs == 2
        setReg(cmdArgs[0]], memory[cmdArgs[1]])
    elif cmd is CommandTypes.STOREN:
        assert numArgs == 2
        memory[cmdArgs[1]] = getReg(cmdArgs[0])
    elif cmd is CommandTypes.LOADR:
        assert numArgs == 2
        setReg(cmdArgs[0]], memory[getReg(cmdArgs[1])])
    elif cmd is CommandTypes.STORER:
        assert numArgs == 2
        memory[getReg(cmdArgs[1])] = getReg(cmdArgs[0])
    else:
        print("Unrecognized command", cmd)
