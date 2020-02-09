from HMMMImplementation import *

myList = [Command(CommandTypes.READ, 0),
          Command(CommandTypes.WRITE, 0),
          Command(CommandTypes.HALT)]

runProgram(myList)
