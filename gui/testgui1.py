import cv2
import numpy
import pylab
from repeated_timer import repeatedTimer
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def VideoPlot():
    #frame = video.read(0)[1]

    axis1.table(row=5, cols=5)
    canvas1.show()
    canvas1.get_tk_widget().place(x=10, y=10)

#def GraphPlot():
    #global gray1, values

    #gray2 = cv2.cvtColor(video.read(0)[1], cv2.COLOR_BGR2GRAY)
    #difference = abs(gray1 - gray2)
    #meanvalue = numpy.mean(difference)
    #print (meanvalue, len(values))
    #gray1 = gray2
    #values.append(meanvalue)
    #values.remove(values[0])
    #changeInXAxis = pylab.arange(len(values)-100, len(values), 1)
    #plotGraph[0].set_data(changeInXAxis, pylab.array(values[-100:]))
    #axis2.axis([changeInXAxis.min(), changeInXAxis.max()+1, 0, 255])
    #canvas2.show()
    #canvas2.get_tk_widget().place(x=430, y=10)

#xAxis = pylab.arange(0, 100, 1)
#yAxis = pylab.array([0]*100)

#video = cv2.VideoCapture(0)
#gray1 = cv2.cvtColor(video.read(0)[1], cv2.COLOR_BGR2GRAY)
window = Tk()
window.geometry('850x450')

#values = [0 for x in range(100)]

videoFigure = Figure(figsize=(5, 4), dpi=80)
axis1 = videoFigure.add_subplot(111)
axis1.set_title('Video frame')
canvas1 = FigureCanvasTkAgg(videoFigure, master=window)
canvas1.show()
canvas1.get_tk_widget().place(x=10, y=10)

#Figure = Figure(figsize=(5, 4), dpi=80)
#axis2 = plotFigure.add_subplot(111)
#axis2.grid(True)
#axis2.set_title("Mean value per Frame")
#canvas2 = FigureCanvasTkAgg(plotFigure, master=window)
#canvas2.show()
#canvas2.get_tk_widget().place(x=300, y=10)

#axis2.axis([0, 100, 0, 255])
#plotGraph = axis2.plot(xAxis, yAxis, 'o-', color='r', markersize=2)

#timer1 = repeatedTimer(.01, GraphPlot)
timer2 = repeatedTimer(.01, VideoPlot)

window.mainloop()



