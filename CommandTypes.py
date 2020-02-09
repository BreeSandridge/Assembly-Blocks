from enum import Enum


class CommandTypes(Enum):

    # System Instructions
    HALT = 0
    READ = 1
    WRITE = 2
    NOP = 3

    # Setting Register Data
    SETN = 4
    ADDN = 5
    COPY = 6

    # Arithmetic
    ADD = 7
    SUB = 8
    NEG = 9
    MUL = 10
    DIV = 11
    MOD = 12

    # Jumps
    JUMPN = 13
    JUMPR = 14
    JEQZN = 15
    JNEZN = 16
    JGTZN = 17
    JLTZN = 18
    CALLN = 19

    # Interacting with memory (RAM)
    PUSHR = 20
    POPR = 21
    LOADN = 22
    STOREN = 23
    LOADR = 24
    STORER = 25
