__author__ = 'subin'
def Matching(New_first_string, New_second_string ):
    LengthOfFirst = len(New_first_string)
    LengthOfSecond = len(New_second_string)
    if LengthOfFirst < LengthOfSecond:
        Diff = LengthOfSecond - LengthOfFirst
        New_first_string = New_first_string + '-' * Diff
    else:
        Diff = LengthOfFirst-LengthOfSecond
        New_second_string = New_second_string + '-' * Diff
    Strings_1 = [New_first_string, New_second_string]
    return Strings_1
def Score(New_first_string, New_second_string):
    New_first_string += ' '
    New_second_string += ' '
    First_string_1 = ''
    Second_string_1 = ''
    Match_temp = 0
    Missmatch_temp = 0
    for Ltr_1, Ltr_2 in zip(New_first_string, New_second_string):
        if Ltr_1 == Ltr_2:
            Match_temp += 1
            First_string_1 += Ltr_1.lower()
            Second_string_1 += Ltr_2.lower()
        else:
            Missmatch_temp += 1
            First_string_1 += Ltr_1.upper()
            Second_string_1 += Ltr_2.upper()
    Strings_2=[First_string_1, Second_string_1, Match_temp, Missmatch_temp]
    return Strings_2

First_string = raw_input('Enter first sample: ').upper()
Second_string = raw_input('Enter second sample: ').upper()
New_first_string = First_string
New_second_string = Second_string
while True:
    print '''----------------------------Choices------------------------------------------
 'a' for Add a 'Dash'.
 'd' for Delete a element.
 's' for print score.
 'q' for quit.
-----------------------------------------------------------------------------'''
    Choise = raw_input('Enter your choise: ')
    if Choise == 'a':
        Add = raw_input('Enter sample number, index: ')
        Index = int(Add[2])-1
        if Add[0] == '1':
            if Index <= len(New_first_string):
                New_first_string = New_first_string[:Index]+'-'+New_first_string[Index:]
                New_Strings = Matching(New_first_string, New_second_string)
                print '''
-----------------------------------------------------------------------------'''
                print New_Strings[0], 'edited.'
                print New_Strings[1]
                print '''
-----------------------------------------------------------------------------'''
            else:
                print 'Invalid index'
        elif Add[0] == '2':
            if Index <= len(New_second_string):
                New_second_string = New_second_string[:Index]+'-'+New_second_string[Index:]
                New_Strings = Matching(New_first_string, New_second_string)
                print '''
-----------------------------------------------------------------------------'''
                print New_Strings[0]
                print New_Strings[1], 'edited.'
                print '''
-----------------------------------------------------------------------------'''
            else:
                print 'Invalid index'
        else:
            print 'Invalid entry...'
    elif Choise == 'd':
        Del = raw_input('Enter sample number, index: ')
        Index = int(Del[2])-1
        if Del[0] == '1':
            if Index <= len(New_first_string):
                New_first_string = New_first_string[:Index]+New_first_string[Index+1:]
                New_Strings = Matching(New_first_string, New_second_string)
                print '''
-----------------------------------------------------------------------------'''
                print New_Strings[0], 'edited.'
                print New_Strings[1]
                print '''
-----------------------------------------------------------------------------'''
            else:
                print 'Invalid index'
        elif Del[0] == '2':
            if Index <= len(New_second_string):
                New_second_string = New_second_string[:Index]+New_second_string[Index+1:]
                New_Strings = Matching(New_first_string, New_second_string)
                print '''
-----------------------------------------------------------------------------'''
                print New_Strings[0]
                print New_Strings[1], 'edited.'
                print '''
-----------------------------------------------------------------------------'''
            else:
                print 'Invalid index'
        else:
            print 'Invalid entry...'
    elif Choise == 's':
        Scr_value=Score(New_first_string, New_second_string)
        print '''
-----------------------------------------------------------------------------'''
        print 'First sample: ', Scr_value[0]
        print 'Second sample: ', Scr_value[1]
        print 'Number of matching: ', Scr_value[2]
        print 'Number of missmatching: ', Scr_value[3]
        print '''
-----------------------------------------------------------------------------'''
    elif Choise == 'q':
        quit()
    else:
        print 'Invalid Choise'
