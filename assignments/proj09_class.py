__author__ = 'subin'
'''---------------------------------------------------------------
-------------------------- CALCULATOR ----------------------------
------------------------------------------------------------------'''
class Calculator():
#-------------------------------- Addition -------------------------------------------
    def Addition(self, First_Operand, Second_Operand):
        return First_Operand + Second_Operand
#------------------------------- Subtraction -----------------------------------------
    def Subtraction(self, First_Operand, Second_Operand):
        return First_Operand - Second_Operand
#-------------------------------- Multiplication -------------------------------------
    def Multiplication(self, First_Operand, Second_Operand):
        return First_Operand * Second_Operand
#----------------------------------- Division ----------------------------------------
    def Division(self, First_Operand, Second_Operand):
        return First_Operand / Second_Operand
'''---------------------------------------------------------------
------------------------ VALIDITY CHECKING -----------------------
------------------------------------------------------------------'''
class Validity():
#------------------ Checking the expression is valid or not --------------------------
    def Valid_Expression(self, Expression_split):
        if len(Expression_split) == 3:
            return 1
        else:
            return 0
#------------------ Checking the operator is valid or not --------------------------
    def Valid_Operator(self, Expression_split):
        Operator = Expression_split[1]
        if Operator == '+':
            return 1
        elif Operator == '-':
            return 2
        elif Operator == '*':
            return 3
        elif Operator == '/':
            return 3
        else:
            return 0
#------------------ Checking the operand is valid or not --------------------------
    def Valid_Operand(self, Expression_split):
        #Operands = int(Expression_split[0]), int(Expression_split[2])
        return True
'''---------------------------------------------------------------
---------------- ROMAN NUMERAL - INTEGER CONVERTER ---------------
------------------------------------------------------------------'''
class Roman_Neumerals_Convert():
#------------------ Roman numerals convert into integer --------------------------
    def RomanToInteger(self, Roman_Numreral):
        LengthOfRoman = len(Roman_Numreral)
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        Intger = ()
        for i in Roman_Numreral:
            Intger += eval(i),
        LengthOfInteger = len(Intger)
        IntValue = Intger[LengthOfInteger-1]
        if LengthOfInteger > 1:
            for i in range(LengthOfInteger-1, 0, -1):
                if Intger[i] <= Intger[i-1]:
                    IntValue += Intger[i-1]
                else:
                    IntValue = abs(IntValue) - Intger[i-1]
        return IntValue
#------------------ Integer convert into Roman Numerals --------------------------
    def IntegerToRoman(self, IntegerNumber):
        if IntegerNumber == 0:
            return 'NIL'
        RomanValue = (1000, 500, 100, 50, 10, 5, 1)
        RomanValue_2 = (10, 5, 10, 5, 10, 5)
        RomanInteger = ()
        for i in RomanValue:
            Flag = IntegerNumber/i
            RomanInteger += Flag,
            IntegerNumber = IntegerNumber%i
        Thousands = RomanInteger[0]
        Hundreds = RomanInteger[1] * 5 + RomanInteger[2]
        Tens = RomanInteger[3] * 5 + RomanInteger[4]
        Ones = RomanInteger[5] * 5 + RomanInteger[6]
        RomanInteger = (Thousands, Hundreds, Tens, Ones)
        SpecialCase = ('CM', 'XC', 'IX', 'CD', 'XL', 'IV')
        SpecialCase_2 = ('D', 'L', 'V', 'C', 'X', 'I')
        RomanNumber = 'M' * Thousands
        for i in range(0,3):
            if RomanInteger[i+1] == 9:
                RomanNumber += SpecialCase[i]
            elif RomanInteger[i+1] >= 5:
                RomanNumber += SpecialCase_2[i] + (SpecialCase_2[i+3] * (RomanInteger[i+1]-5))
            elif RomanInteger[i+1] == 4:
                RomanNumber += SpecialCase[i+3]
            elif RomanInteger[i+1] < 4:
                RomanNumber += SpecialCase_2[i+3] * RomanInteger[i+1]
            else:
                pass
        return RomanNumber
'''-----------------------------------------------------------------------------------------------
---------------------------------------MAIN-------------------------------------------------------
--------------------------------------------------------------------------------------------------'''
while True:
    Expression = raw_input('Enter your expression: ').upper()
    Expression_split = Expression.split()
    Calculator_obj = Calculator()
    Validity_obj = Validity()
    Roman_Neumerals_Convert_obj = Roman_Neumerals_Convert()
    if Validity_obj.Valid_Expression(Expression_split) == 1:
        if Validity_obj.Valid_Operand(Expression_split) == True:
            First_Operand = Roman_Neumerals_Convert_obj.RomanToInteger(Expression_split[0])
            Second_Operand = Roman_Neumerals_Convert_obj.RomanToInteger(Expression_split[2])
            if Validity_obj.Valid_Operator(Expression_split) == 1:
                Value = Calculator_obj.Addition(First_Operand, Second_Operand)
                print Expression, '=', Roman_Neumerals_Convert_obj.IntegerToRoman(Value)
            elif Validity_obj.Valid_Operator(Expression_split) == 2:
                Value = Calculator_obj.Subtraction(First_Operand, Second_Operand)
                print Expression, '=', Roman_Neumerals_Convert_obj.IntegerToRoman(Value)
            elif Validity_obj.Valid_Operator(Expression_split) == 3:
                Value = Calculator_obj.Multiplication(First_Operand, Second_Operand)
                print Expression, '=', Roman_Neumerals_Convert_obj.IntegerToRoman(Value)
            elif Validity_obj.Valid_Operator(Expression_split) == 4:
                Value = Calculator_obj.Division(First_Operand, Second_Operand)
                print Expression, '=', Roman_Neumerals_Convert_obj.IntegerToRoman(Value)
            else:
                print 'Error: Invalid operator'
        else:
            print 'Error: Invalid operand'
    else:
        print 'Error: Invalid expression'
