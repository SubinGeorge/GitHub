__author__ = 'subin'
class Validity():
    def Valid_Code(self, Code):
        if len(Code) != 4:
            Flag = 0
        elif Code.isdigit() == False:
            Flag = 0
        else:
            Flag = 1
        return Flag
    def Valid_Guess(self, Input):
        for k in range(0, 4):
            if Input.count(Input[k]) == 1:
                Flag = 1
            else:
                Flag = 0
                break
        return Flag
    def Guess_result(self, Code, Input):
        Place = ''
        Flag = ''
        Iteration = 0
        Score = 0
        #Code += ' '
        #Input += ' '
        for Ltr_1, Ltr_2 in zip(Code, Input):
            Iteration += 1
            if Ltr_1 == Ltr_2:
                Score += 1
                Place += Ltr_2 + ', '
            elif Ltr_2 in Code:
                Place += '*, '
                Flag += Ltr_2 + ', '
            else:
                Place += '*, '
        return Place, Flag, Score
Code = raw_input('Enter your code: ')
Validity_obj = Validity()
if Validity_obj.Valid_Code(Code) == 0:
    print 'Error: Please ener a \'4 digit\' number.'
Guess = range(12,0,-1)
for i in Guess:
    print '{} guess is remaining'.format(i)
    Input = raw_input('Enter your guess: ')
    if Validity_obj.Valid_Code(Input) == 1:
        if Validity_obj.Valid_Guess(Input) == 1:
            Place, Flag, Score = Validity_obj.Guess_result(Code, Input)
            if Score != 0:
                print Place, 'matched...\n', 'Score: ', Score
                if len(Flag) != 0:
                    print Flag, 'misplaced in guess'
            elif Score == 4:
                print 'You are WINNER..'
                print '''----------------------------------------------------------------------
----------------------------------------------------------------------'''
                quit()
            else:
                print 'Score:', Score,'\nBad guess\n', '----------------------------------------------------------------------'
        else:
            print'Bad guess\n', '----------------------------------------------------------------------'
    else:
        print'Bad Guess\n', '----------------------------------------------------------------------'
print 'Sorry... You are loser...'
print 'The Code is', Code
print '''----------------------------------------------------------------------
----------------------------------------------------------------------'''