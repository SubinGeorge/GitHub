__author__ = 'subin'
# Function for calculate reading of used water.
def AmountOfWatter(Reading_Biginning, Reading_Ending):
    if(Reading_Biginning < Reading_Ending):
        Diff = Reading_Ending - Reading_Biginning
    else:
        Diff = 999999999 - Reading_Biginning + Reading_Ending + 1
    return Diff
# Function for calculate amount billed for water
def Billed_amount(Used_water, Customer_Code):
# For residential. use:
    if (Customer_Code == 'r'):
        Amount = 5.00+(Used_water*0.0005)
# For commercial use:
    elif(Customer_Code == 'c'):
        if(Used_water<=4000000):
            Amount = 1000.00
        else:
            Amount = 1000.00 + ((Used_water-4000000)*0.00025)
# For industrial use:
    elif(Customer_Code == 'i'):
        if(Used_water<=4000000):
            Amount = 1000.00
        elif(Used_water>=4000000 & Used_water<=10000000):
            Amount = 2000.00
        else:
            Amount = 2000.00 + ((Used_water-10000000)*0.00025)
    else:
        Amount = 'Enter correct code'
    return Amount
# Read customer code
Customer_Code = raw_input('Enter customer code: ')
if(Customer_Code=='r'):
    print 'Residential use'
elif(Customer_Code=='c'):
    print 'Commercial use'
elif(Customer_Code=='i'):
    print 'Industrial use'
else:
    print 'Invalid code'
    quit()
# Read meter readings
Reading_Biginning = input('Enter biginning reading: ')
Reading_Ending = input('Enter ending reading: ')
# Call function AmountOfWatter
Used_water = float((AmountOfWatter(Reading_Biginning, Reading_Ending)))/10
# Call function Billed_amount
Bill = round(Billed_amount(Used_water, Customer_Code),2)
# Print values:
print 'Customer Code: ', Customer_Code
print 'Biginning meter reading: ', Reading_Biginning
print 'Ending meter reading: ', Reading_Ending
print 'Gallons of water used: ', Used_water
print 'Amount billed:', Bill
