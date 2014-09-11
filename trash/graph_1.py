__author__ = 'subin'

from Tkinter import *
import pylab
import numpy
import cv2
"Video capture and store into 'Video'"
Video = cv2.VideoCapture(0)

#   Function for calculate mean value
def Y_Axis_Change(arg):
#   Read convert into Gray scale
    Gray_1 = cv2.cvtColor(Video.read(0)[1], cv2.COLOR_BGR2GRAY)
#   Read convert into Gray scale
    Gray_2 = cv2.cvtColor(Video.read(0)[1], cv2.COLOR_BGR2GRAY)
#   Finding absolute value of difference of Gray_2 and Gray_1
    Difference = abs(Gray_2 - Gray_1)
#   Finding Mean value
    Mean_value = numpy.mean(Difference)
#   Print mean value
    print Mean_value
#   Mean value append to list 'Value'
    Values.append(Mean_value)

#   Function for move x axis
def X_Axis_Change(arg):

    global Values
#   Change initial value and final value
    ChangeInXAxis = pylab.arange(len(Values)-100, len(Values), 1)
    Plot[0].set_data(ChangeInXAxis, pylab.array(Values[-100:]))
#   Set Dimension of axis as 100 x 255
    Axis.axis([ChangeInXAxis.min(), ChangeInXAxis.max()+1, 0, 255])

    manage.canvas.draw()


Window = Tk()
Window.title('Window')
'''====================================================================
=========================== MAIN ======================================
======================================================================='''
#   Create a list for x axis(0 to 100)
X_Axis = pylab.arange(0, 100, 1)
#   Create a list for y axis(100 elements)
Y_Axis = pylab.array([0]*100)
#   Create a figure
#Figure_1 = Figure(figsize=(5,4), dpi=100)
Figure = pylab.figure(1)
#   Create an axis
Axis = Figure.add_subplot(111)
#   For axis grid
Axis.grid(True)
# Title
Axis.set_title("Mean value per Frame")
#   x- label
Axis.set_xlabel("Frame")
#   Y- label
Axis.set_ylabel("Mean value")
#   Set axis size as 100 x 255
Axis.axis([0, 100, 0, 255])
#    plot  graph
Plot = Axis.plot(X_Axis, Y_Axis, 'o-', color='r', markersize=2)

manage = pylab.get_current_fig_manager()
#   Create list for store values
Values = [0 for x in range(100)]
#   Create Timer_1
Timer_1 = Figure.canvas.new_timer(interval=10)
#   Calling of function for move x axis
Timer_1.add_callback(X_Axis_Change, ())
#   Create Timer_2
Timer_2 = Figure.canvas.new_timer(interval=10)
#   Calling of function for get mean value
Timer_2.add_callback(Y_Axis_Change, ())
#   To start Timer_1
Timer_1.start()
#   To start Timer_2
Timer_2.start()
#   To show plotted graph
pylab.show()
