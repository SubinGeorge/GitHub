__author__ = 'subin'
'''----------------------------------------------------------------------------------
--------------------- Create a class Calculator -------------------------------------
-------------------------------------------------------------------------------------'''
class Calculator:
#-------------------------------- Addition -------------------------------------------
    def Addition(self, First_Operand, Second_Operand):
        return float(First_Operand) + float(Second_Operand)
#------------------------------- Subtraction -----------------------------------------
    def Subtraction(self, First_Operand, Second_Operand):
        return float(First_Operand) - float(Second_Operand)
#-------------------------------- Multiplication -------------------------------------
    def Multiplication(self, First_Operand, Second_Operand):
        return float(First_Operand) * float(Second_Operand)
#----------------------------------- Division ----------------------------------------
    def Division(self, First_Operand, Second_Operand):
        if int(Second_Operand) == 0:
            return '0'
        else:
            return int(First_Operand) / int(Second_Operand), int(First_Operand)% int(Second_Operand)
'''------------------------------------------------------------------------------------
--------------------- Create a class Varification -------------------------------------
---------------------------------------------------------------------------------------'''
class Varification:
#------------------ Checking the expression is valid or not --------------------------
    def Valid_Expression(self, Expression_split):
        if len(Expression_split) == 3:
            return True
        else:
            return False
#--------------------- Checking the operand is valid or not --------------------------
    def Valid_Operand(self, Expression_split):
        First_Operand = Expression_split[0]
        Second_Operand = Expression_split[2]
        if (First_Operand.isdigit() == True & Second_Operand.isdigit() == True):
            return True
        else:
            return False
#-------------------- Checking the operator is valid or not --------------------------
    def Valid_Operator(self, Expression_split):
        Operator = Expression_split [1]
        if Expression_split[1] == '+':
            Oper_Flag = 1
        elif Expression_split[1] == '-':
            Oper_Flag = 2
        elif Expression_split[1] == '*':
            Oper_Flag = 3
        elif Expression_split[1] == '/':
            Oper_Flag = 4
        else:
            Oper_Flag = 0
        return Oper_Flag

'-------------------------------------------------------------------------------------'
'--------------------------------- Main Program --------------------------------------'
'-------------------------------------------------------------------------------------'

while True:
    Expression = raw_input("Enter your Expression: ")
    Expression_split = Expression.split()
    Calculator_obj = Calculator()
    Varification_obj = Varification()
    if Varification_obj.Valid_Expression(Expression_split) == True:
        if Varification_obj.Valid_Operand(Expression_split) == True:
            Operands = Varification_obj.Valid_Operand(Expression_split)
            First_Operand = Expression_split[0]
            Second_Operand = Expression_split[2]
            if Varification_obj.Valid_Operator(Expression_split) == 0:
                print 'Error: ', Expression_split[1],' is s invalid operator'
                #break
            elif Varification_obj.Valid_Operator(Expression_split) == 1:
                print Expression, '=', Calculator_obj.Addition(First_Operand, Second_Operand)
            elif Varification_obj.Valid_Operator(Expression_split) == 2:
                print Expression, '=', Calculator_obj.Subtraction(First_Operand, Second_Operand)
            elif Varification_obj.Valid_Operator(Expression_split) == 3:
                print Expression, '=', Calculator_obj.Multiplication(First_Operand, Second_Operand)
            elif Varification_obj.Valid_Operator(Expression_split) == 4:
                Div = Calculator_obj.Division(First_Operand, Second_Operand)
                if Div[0] == '0':
                    print 'Error: Attempt to division by zero'
                else:
                    print Expression, '=', Div[0]
                    print 'Reminder = ', Div[1]
        else:
            print 'Error: ', Expression_split[0],'or', Expression_split[2], 'is a invalid operands'
    else:
        print 'Error: ', Expression, 'is a invalid expression'


