from HMMMImplementation import *

myList = [Command(CommandTypes.READ, 4),
          Command(CommandTypes.SETN, 1, 0),
          Command(CommandTypes.SETN, 2, 1),
          Command(CommandTypes.SETN, 5, 1),
          Command(CommandTypes.JEQZN, 4, 9),
          Command(CommandTypes.ADD, 3, 1, 2),
          Command(CommandTypes.COPY, 2, 1),
          Command(CommandTypes.COPY, 1, 3),
          Command(CommandTypes.SUB, 4, 4, 5),
          Command(CommandTypes.JGTZN, 4, 4),
          Command(CommandTypes.WRITE, 1),
          Command(CommandTypes.JUMPN, 0)]

runProgram(myList)
