#findx program

#equation = newvar + 4 * 3 #divides the equation in both sides (answer + expression)
# 4x + 3 = 15 is actually x = (15 - 3)/4

#similar to the brute thing, check each character for each sign,
#that way, we can get the position of each operator allowing us to check
#the number or variable that is being used by the operator 

#AdditionSigns = "+"
#AdditionPosition = [-1]
#NegativeSigns = "-"
#NegativePosition = [-1]
#MultiplicationSigns = "*"
#MultiplicationPosition = [-1]
#DivisionSigns = "/"
#DivisionPosition = [-1]

#Perhaps their can be a list of position of operators and a function would check the
#list and automatically do the math based off the operator that was found
#live rather than being saved into individual list

OperatorSigns = "+-*/÷^"
OperatorPositions = []

equation = input("Submit your equation: ")

EPosition = 0
OPosition = 0
ScanforOperator = ''
AddtoList = []
checkdone = False

def markoperator():
    for i in range(len(equation)):
        if ScanforOperator == OperatorSigns:
            AddtoList = AddtoList + ScanforOperator
        position = position + 1

def ImprovedMarkOperator():
    


#issues before I come back,
#ScanforOperator == OperatorSigns: only scans
#the whole thing. We need to make it so it checks each
#individual operator within the string, / and if statement
#where if it contains a character within the string it passes.
#Thinking about making a repeated loop where it == OperatorSigns[range]

#A way to specifically find each operator in the list, similar to the brute, is to check each letter in the
#inputted equation for the first position of the operator string, then another check for each position.