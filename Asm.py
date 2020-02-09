from Command import *
import sys
import HMMMImplementation
from CommandTypes import CommandTypes


def to_commands(li):
    commands = []
    type = None

    while len(li) > 0:
        if len(li) > 0:
            head = li.pop(0)
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
            elif head == "storer":
                type = CommandTypes.STOREN

            inputs = []
            while li[0] is not ";":
                inputs.append(int(li.pop(0)))
            li.pop(0)
            commands.append(Command(type, *inputs))

    return commands


def get_tokens(file_path):
    raw = open(path).read()
    lines = raw.split("\n")
    words = sum(((line.split(" ") + [";"]) for line in lines), [])
    return words


path = sys.argv[1]
commands = to_commands(get_tokens(path))
HMMMImplementation.runProgram(commands)
