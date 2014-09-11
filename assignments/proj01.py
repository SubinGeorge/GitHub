# Assignment_1, 11 Aug 14, 05:09
__author__ = 'subin'
# Function For Addition
def Addition(First_Input,Second_Input):
    Add=First_Input+Second_Input
    return Add # Return result of Addition
# Function For Subtraction
def Subtraction(First_Input,Second_Input):
    Sub=First_Input-Second_Input
    return Sub # Return result of Subtraction
# Function For Multiplication
def Multiplication(First_Input,Second_Input):
    Mul=First_Input*Second_Input
    return Mul # Return result of Multiplication
# Function For Division
def Division(First_Input,Second_Input):
    Div=[0,1]
    Div[0] = First_Input/Second_Input
    Div[1] = First_Input%Second_Input
    return Div # Return result of Division
# Read first number
First_Input = input('Give your first input: ')
# Read second number
Second_Input = input('Give your second input: ')
# Call function Addition
Sum = Addition(First_Input, Second_Input)
# Call function Subtraction
Diff = Subtraction(First_Input, Second_Input)
# Call function Multiplication
Prod = Multiplication(First_Input, Second_Input)
# Call function Division
Quot = Division(First_Input, Second_Input)
# Print sum
print 'Sum of {0} and {1} is {2}.'.format(First_Input, Second_Input, Sum)
# Print difference
print 'Difference of {0} and {1} is {2}.'.format(First_Input, Second_Input, Diff)
# Print product
print 'Product of {0} and {1} is {2}.'.format(First_Input, Second_Input, Prod)
# Print quotient and reminder
print 'Quotient of {0} and {1} is {2} and reminder is {3}.'.format(First_Input, Second_Input, Quot[0], Quot[1])
