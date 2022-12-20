lines = open("D5_Input.txt").readlines()

stacks = {}

listOne = ['S', 'L', 'W']
listTwo = ['J', 'T', 'N', 'Q']
listThree = ['S', 'C', 'H', 'F', 'J']
listFour = ['T', 'R', 'M', 'W', 'N', 'G', 'B']
listFive = ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B']
listSix = ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L']
listSeven = ['D', 'W', 'R', 'N', 'J', 'M']
listEight = ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J']
listNine = ['H', 'L', 'Q', 'N', 'B', 'F', 'T']

stacks.update({'1': listOne})
stacks.update({'2': listTwo})
stacks.update({'3': listThree})
stacks.update({'4': listFour})
stacks.update({'5': listFive})
stacks.update({'6': listSix})
stacks.update({'7': listSeven})
stacks.update({'8': listEight})
stacks.update({'9': listNine})


crates = 0
startStack = 0
endStack = 0

for line in lines:
    newLine = line[5:]
    if newLine[1] == ' ':
        crates = int(newLine[0])
        startStack = int(newLine[7])
        endStack = int(newLine[12])
    else:
        crates = int(newLine[0] + newLine[1])
        startStack = int(newLine[8])
        endStack = int(newLine[13])
    if crates == 1:
        stacks[str(endStack)].append(stacks[str(startStack)].pop())
        print(stacks[str(startStack)])
        print(stacks[str(endStack)])
        print('\n')
    else:
        print(stacks[str(startStack)])
        print(stacks[str(endStack)])
        cratePackage = []
        for i in range(crates):
            crate = stacks[str(startStack)].pop()
            cratePackage.append(crate)
        for i in range(len(cratePackage)):
            stacks[str(endStack)].append(cratePackage.pop())
        print(stacks[str(startStack)])
        print(stacks[str(endStack)])
        print('\n')
        
            
        
print(stacks['1'])
print(stacks['2'])
print(stacks['3'])
print(stacks['4'])
print(stacks['5'])
print(stacks['6'])
print(stacks['7'])
print(stacks['8'])
print(stacks['9'])
    