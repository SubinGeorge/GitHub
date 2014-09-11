__author__ = 'subin'
import pylab
import numpy
import cv2
"Video capture and store into 'Video'"
video = cv2.VideoCapture(0)
#   Read convert into Gray scale
gray1 = cv2.cvtColor(video.read(0)[1], cv2.COLOR_BGR2GRAY)

#   Function for calculate mean value
def GraphPlot(arg):
    global gray1, values
#   Read convert into Gray scale
    gray2 = cv2.cvtColor(video.read(0)[1], cv2.COLOR_BGR2GRAY)
#   Finding absolute value of difference of Gray_2 and Gray_1
    difference = abs(gray1 - gray2)
#   Finding Mean value
    meanValue = numpy.mean(difference)
#   Print mean value
    print meanValue
    gray1 = gray2
#   Mean value append to list 'Value'
    values.append(meanValue)
#   Change initial value and final value
    ChangeInXAxis = pylab.arange(len(values)-100, len(values), 1)
    plot1[0].set_data(ChangeInXAxis, pylab.array(values[-100:]))
#   Set Dimension of axis as 100 x 255
    axis1.axis([ChangeInXAxis.min(), ChangeInXAxis.max()+1, 0, 255])

    manage.canvas.draw()

'''====================================================================
=========================== MAIN ======================================
======================================================================='''
#   Create a list for x axis(0 to 100)
xAxis = pylab.arange(0, 100, 1)
#   Create a list for y axis(100 elements)
yAxis = pylab.array([0]*100)
#   Create a figure
figure1 = pylab.figure(1)
#   Create an axis
axis1 = figure1.add_subplot(111)
#   For axis grid
axis1.grid(True)
# Title
axis1.set_title("Mean value per Frame")
#   x- label
axis1.set_xlabel("Frame")
#   Y- label
axis1.set_ylabel("Mean value")
#   Set axis size as 100 x 255
axis1.axis([0, 100, 0, 255])
#    plot  graph
plot1 = axis1.plot(xAxis, yAxis, 'o-', color='r', markersize=2)

manage = pylab.get_current_fig_manager()
#   Create list for store values
values = [0 for x in range(100)]
#   Create Timer_1
timer1 = figure1.canvas.new_timer(interval=10)
#   Calling of function for move x axis
timer1.add_callback(GraphPlot, ())
#   To start Timer_1
timer1.start()
#   To show plotted graph
pylab.show()
