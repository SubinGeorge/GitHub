__author__ = 'subin'
# Read Order.
OrderOfSquare = input('Please give order of square: ')
# Read top left number.
TopLeftNumber = input('Please give top left number: ')
# Row incriment in for loop.
for row in range(0, OrderOfSquare):
# Column incriment in for loop.
    for col in range(0, OrderOfSquare):
# If TopLeftNumber is equal to order print TopLeftNumber and reset as '1'( to right).
        if TopLeftNumber == OrderOfSquare:
            print TopLeftNumber,
            TopLeftNumber = 1
# If TopLeftNumber is not equal to order print TopLeftNumber and incriment by '1'( to right).
        else:
            print TopLeftNumber,
            TopLeftNumber = TopLeftNumber+1
# If TopLeftNumber is equal to order, reset it as '1' (downword).
    if TopLeftNumber == OrderOfSquare:
        TopLeftNumber = 1
#If TopLeftNumber is not equal to order, incriment by '1'(downword).
    else:
        TopLeftNumber = TopLeftNumber+1
# Start new line.
    print '\n'
