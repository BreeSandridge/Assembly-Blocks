

str = "34bf343cro3t4njkrnck3b4wk"
strLong = list(str)
listStr = []
isLn = False

wrd = ""
for i in range(len(strLong)):
    if isLn == True:
        isLn = False
        continue
    if 48 <= ord(strLong[i]) <= 57:
        if not wrd == "":
            listStr.append(wrd)
            wrd = ""
        listStr.append(strLong[i])
    elif 65 <= ord(strLong[i]) <= 90 or 96 <= ord(strLong[i]) <= 122:
        wrd += strLong[i]
    elif strLong[i] == "\":
        if strLong[i+1]=="n":
            if not wrd == "":
            listStr.append(wrd)
            wrd = ""
        listStr.append("\n")
        isLn = True

print(listStr)