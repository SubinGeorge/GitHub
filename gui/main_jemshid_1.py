__author__ = 'subin'
import sys
import numpy
import cv2
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import Tkinter as Tk
import pylab
from repeated_timer import repeatedTimer


def GraphPlot(arg):
    global gray1, values
    gray2 = cv2.cvtColor(video.read(0)[1], cv2.COLOR_BGR2GRAY)
    difference = abs(gray1 - gray2)
    meanValue = numpy.mean(difference)
    print meanValue
    gray1 = gray2
    values.append(meanValue)
    ChangeInXAxis = pylab.arange(len(values)-100, len(values), 1)
    plotGraph[0].set_data(ChangeInXAxis, pylab.array(values[-100:]))
    axis2.axis([ChangeInXAxis.min(), ChangeInXAxis.max()+1, 0, 255])
    canvas_1 = FigureCanvasTkAgg(graphFigure, master=window)
    canvas_1.show()
    canvas_1.get_tk_widget().pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
    canvas_1._tkcanvas.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
    manage.canvas.draw()



#~ video = cv2.VideoCapture(0)
gray1 = cv2.cvtColor(video.read(0)[1], cv2.COLOR_BGR2GRAY)

videoFigure = Figure(figsize=(5,4), dpi=100)
axis1 = videoFigure.add_subplot(111)
axis1.set_title("Frame")

xAxis = pylab.arange(0, 100, 1)
yAxis = pylab.array([0]*100)
graphFigure = Figure(figsize=(5,4), dpi=100)
axis2 = graphFigure.add_subplot(111)
axis2.grid(True)
axis2.set_title("Mean value per Frame")
axis2.set_xlabel("Frame")
axis2.set_ylabel("Mean value")
axis2.axis([0, 100, 0, 255])
plotGraph = axis2.plot(xAxis, yAxis, 'o-', color='r', markersize=2)
manage = pylab.get_current_fig_manager()
values = [0 for x in range(100)]

tableFigure = Figure(figsize=(5, 4), dpi=100)
axis3 = tableFigure.add_subplot(111)
axis3.set_title("Table")

window = Tk.Tk()
window.title("test_Gui")

#while True:
GraphPlot(0)
t1 = repeatedTimer(.1, GraphPlot(0))
t1.start()
#~ Tk.mainloop()
