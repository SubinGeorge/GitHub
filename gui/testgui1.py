__author__ = 'subin'
import numpy
import cv2
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import Tkinter as Tk

from repeated_timer import repeatedTimer
matplotlib.use('TkAgg')
import pylab


def Video():
    image1 = video.read(0)[1]
    axis1.imshow(image1)
    canvas1 = FigureCanvasTkAgg(videoFigure, master=window)
    canvas1.show()
    canvas1.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
    canvas1._tkcanvas.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

video = cv2.VideoCapture(0)
window = Tk.Tk()
window.title("test_Gui")
window.geometry('500x500')
videoFigure = Figure(figsize=(5,4), dpi=100)
axis1 = videoFigure.add_subplot(111)
axis1.set_title("Test Frame")

timer1 = repeatedTimer(.1, Video)
timer1.start()

Tk.mainloop()