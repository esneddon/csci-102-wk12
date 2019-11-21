#Ethan Sneddon
#CSCI 102 Section E
#Python Lab 12A

def PrintOutput(input_str):
    print('OUTPUT', input_str)

def LoadFile(filename):
    x = int(0)
    file = open(filename)
    file_list = file.readlines()
    for i in file_list:
        file_list[x] = file_list[x].rstrip('\n')
        x += 1
    return file_list

def UpdateString(stringOne, stringTwo, indexInt):
    s = list(stringOne)
    s[indexInt] = stringTwo
    new_str = ''.join(s)
    print("OUTPUT", new_str )

def FindWordCount(myList, myStr):
    count = int(0)
    for i in myList:
        if i == myStr:
            count += 1
    return count

def ScoreFinder(listOne, listTwo, string):
    if string in listOne or string.capitalize() in listOne:
        print('OUTPUT', string.capitalize(), 'got a score of', listTwo[listOne.index(string.capitalize())])
    else:
        print('OUTPUT player not found')

def Union(listOne, listTwo):
    return listOne + listTwo

def Intersection(listOne, listTwo):
    x = int(0)
    listInter = []
    for i in listOne:
        if listOne[x] in listTwo:
            listInter.append(listOne[x])
        x += 1
    return listInter













