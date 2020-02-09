from enum import Enum


class CommandTypes(Enum):

    # System Instructions
    HALT = auto()
    READ = auto()
    WRITE = auto()
    NOP = auto()

    # Setting Register Data
    SETN = auto()
    ADDN = auto()
    COPY = auto()

    # Arithmetic
    ADD = auto()
    SUB = auto()
    NEG = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()

    # Jumps
    JUMPN = auto()
    JUMPR = auto()
    JEQZN = auto()
    JNEZN = auto()
    JGTZN = auto()
    JLTZN = auto()
    CALLN = auto()

    # Interacting with memory (RAM)
    PUSHR = auto()
    POPR = auto()
    LOADN = auto()
    STOREN = auto()
    LOADR = auto()
    STORER = auto()
