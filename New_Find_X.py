#findx program

#equation = newvar + 4 * 3 #divides the equation in both sides (answer + expression)
# 4x + 3 = 15 is actually x = (15 - 3)/4

#The code will gather the position of operators within a given equation, and then solve
#the equation by going through the equation with the position of operators in order of 
#operations.

import time

OperatorSigns = "-+*/÷^"

equation = input("Submit your equation: ")

def ImprovedMarkOperator():
    EPosition = 0
    OSPosition = 0
    AddtoList = []
    checkdone = False
    while EPosition != len(equation) - 1:
    #one letter equation won't run (it is len(equation) - 1)
        while True:
            #originally was while checkdone == False:
            if equation[EPosition] == OperatorSigns[OSPosition]:
                AddtoList.append(EPosition)
                break
                checkdone == True
            elif OSPosition == len(OperatorSigns) - 1:
                break
                checkdone = True
            else:
                OSPosition = OSPosition + 1
        OSPosition = 0
        EPosition = EPosition + 1
        #checkdone = False
    return AddtoList

OperatorPositions = ImprovedMarkOperator()
print(OperatorPositions)