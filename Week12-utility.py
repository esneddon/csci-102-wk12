#Ethan Sneddon
#CSCI 102 Section E
#Python Lab 12A

def PrintOutput(input_str):
    print('OUTPUT', input_str)

def LoadFile(filename):
    file = open(filename)
    file_list = file.readlines()
    return file_list

def UpdateString(stringOne, stringTwo, indexInt):
    s = list(stringOne)
    s[indexInt] = stringTwo
    new_str = ''.join(s)
    print("OUTPUT", new_str )
