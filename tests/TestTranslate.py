from HMMMImplementation import *

myCmd = Command(CommandTypes.MOD, 5, 1, 2)
myCmdNum = cmdToNum(myCmd)
print("bin:", bin(myCmdNum))
myCmd2 = numToCmd(myCmdNum)
print("translated: ", myCmd2.commandType, myCmd2.args)
