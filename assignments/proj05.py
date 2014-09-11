__author__ = 'subin'
# Define a function
def Valid_Expression(Operands):
# Checking Length of Elements in 'Oprands'
    if (len(Operands)==3):
# Addition
        if Operands[1]=='+':
            status =str(float(Operands[0])+float(Operands[2]))
# Subtraction
        elif Operands[1]=='-':
            status =str(float(Operands[0])-float(Operands[2]))
# Multiplication
        elif Operands[1]=='*':
            status = str(float(Operands[0])*float(Operands[2]))
# Division
        elif Operands[1] == '/':
            if Operands[2]!= '0':
                status = str(float(Operands[0])/float(Operands[2]))
# error messege
            else:
                status= 'Attempt_to_division_with_zero.'
        else:
            status = 'Invalid_operator.'
    else:
        status = 'Invalid_expression.'
    return status

while True:
# Read expression
    Expression = raw_input('Enter your expression.\nOerands and operator are seperate by using white space : ')
#split into strings
    Operands = Expression.split()
# Call Function ' Valid_Expression'
    Calc = Valid_Expression(Operands)
    print Calc
    Repeat=raw_input('Press \'Yes\',  \'yes\',  \'Y\' or \'y\' to continue...\nPress \'Enter\' to quit...')
    if ((Repeat!='Yes')&(Repeat!='yes')&(Repeat!='Y')&(Repeat!='y')):
        quit()