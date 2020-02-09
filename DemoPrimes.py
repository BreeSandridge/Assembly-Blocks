from HMMMImplementation import *

myList = [Command(CommandTypes.SETN, 4, 1),
          Command(CommandTypes.SETN, 1, 2),
          Command(CommandTypes.SETN, 2, 2),
          Command(CommandTypes.MUL, 3, 2, 2),
          Command(CommandTypes.SUB, 3, 3, 1),
          Command(CommandTypes.JGTZN, 3, 10),
          Command(CommandTypes.MOD, 5, 1, 2),
          Command(CommandTypes.JEQZN, 5, 11),
          Command(CommandTypes.ADD, 2, 2, 4),
          Command(CommandTypes.JUMPN, 3),
          Command(CommandTypes.WRITE, 1),
          Command(CommandTypes.ADD, 1, 1, 4),
          Command(CommandTypes.JUMPN, 2)]

runProgram(myList)
