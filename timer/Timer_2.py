__author__ = 'subin'

from repeated_timer import repeatedTimer
def Print():
    print('hai')
def Print2():
    print(' Subin')
t1 = repeatedTimer(1, Print)
t1.start()
t2 = repeatedTimer(.1, Print2)
t2.start()