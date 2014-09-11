__author__ = 'subin'
from threading import Timer
def Print(arg):
    print 'subin'

timer = Timer(1, Print(0))
timer.start()



