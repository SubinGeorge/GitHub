# Assignment_2, 11 Aug 14, 06:40
__author__ = 'subin'
# Function For Game
def Game(Input):
# Check length of array 'Input'
    if (len(Input)>3):
        print '''An error occurred
        Please give a 3 digit number'''
# Check diff between first and last digits
    elif (abs(int(Input[0]) - int(Input[2]))<2):
        print '''An error occured
        The first and last digits must differ by at least two.'''
    else:
# Reverse of 'Input' store to 'Rev_Num'
        Rev_Num = Input[::-1]
# Find diff between Rev_ Num and Input
# Rev_ Num and Input are strings, so convert into integer by using 'int'
# 'abs' is used to get absolute number
        First_Diff=abs(int(Rev_Num)-int(Input))
# First_Diff convert to string and store into Second_Num
        Second_Num = str(First_Diff)
# Reverse of 'Second_Num' store to 'Rev_Sec_Num'
        Rev_Sec_Num = Second_Num[::-1]
# Sum of Rev_Sec_Num and First_Diff store into Result
        Result = int(Rev_Sec_Num) + int(First_Diff)
# All values stored in an array 'Output'
        Output=[Input, Rev_Num, First_Diff, Second_Num, Rev_Sec_Num, Result]
# return Output of function Game
        return Output
print ''' This is a puzzle favored by Einstein. You will be asked to enter
a 3 digit number, where the hundred's digit differs from the
one's digit by at least two. The procedure eill always yield '1089'.
'''
# Read number as string
Input = raw_input('Give your number: ')
# Call function Game
game=Game(Input)
# Print values
print 'Reverse number of {0} is {1}.'.format(game[0], game[1])
print 'Difference between {0} and {1} is {2}.'.format(game[0], game[1], game[2])
print 'Reverse number of {0} is {1}.'.format(game[3], game[4])
print 'Sum of {0} and {1} is {2}.'.format(game[3], game[4], game[5])
