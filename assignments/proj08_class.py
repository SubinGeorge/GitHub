__author__ = 'subin'
class Palindrome():
    def Check_palindrome(self, IntegerValue):
        IntegerValue = str(IntegerValue)
        LenOfInteger = len(IntegerValue)
        Half_length = LenOfInteger/2
        if LenOfInteger < 2:
            return 0
        elif LenOfInteger%2 == 0:
            for i in range(0, Half_length):
                if int(IntegerValue[i]) == int(IntegerValue[(LenOfInteger-1)-i]):
                    Flag = 1
                else:
                    Flag = 2
                    return Flag
        else:
            for i in range(0, Half_length):
                if int(IntegerValue[i]) == int(IntegerValue[(LenOfInteger-1)-i]):
                    Flag = 1
                else:
                    Flag = 2
                    return Flag
        return Flag
    def Check_lychrel(self, IntegerValue):
        IntegerValue = str(IntegerValue)
        Rev_Integervalue = IntegerValue[::-1]
        Value = int(IntegerValue) + int(Rev_Integervalue)
        return Value
IntegerValue = raw_input('Enter your Integer:')
Palindrome_obj = Palindrome()
if Palindrome_obj.Check_palindrome(IntegerValue) == 0:
    print 'Error: Please Enter a \'2\' digit number.\n','------------------------------------------------------------'
elif Palindrome_obj.Check_palindrome(IntegerValue) == 1:
    print IntegerValue, 'is a natural palindrome\n','------------------------------------------------------------'
else:
    New_IntegerValue = Palindrome_obj.Check_lychrel(IntegerValue)
    for i in range(1, 61):
        if Palindrome_obj.Check_palindrome(New_IntegerValue) == 2:
            IntegerValue_1 = Palindrome_obj.Check_lychrel(New_IntegerValue)
        else:
            print 'Yeild a palindrome {0} in {1} iteration using \'196\' algorithm.'.format(New_IntegerValue, i),'\n------------------------------------------------------------'
            break
    if Palindrome_obj.Check_palindrome(New_IntegerValue) == 2:
        print IntegerValue, 'is a LYCHREL NUMBER.\n', '------------------------------------------------------------'
