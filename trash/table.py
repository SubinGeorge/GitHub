from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = Tk()
window.geometry('850x450')

plotFigure = Figure(figsize=(5, 4), dpi=100)
axis2 = plotFigure.add_subplot(111)
#ax=plt.gca()
col_labels=[] #'col1','col2','col3', 'col4']
row_labels=[] #'row1','row2','row3']
table_vals=[['a','b','c'],[21,22,23],[31,32,33]]
# the rectangle is where I want to place the table
the_table = axis2.table(cellText=table_vals,
                  colWidths = [0.1]*3,
                  loc='center right')
                  #rowLabels=row_labels,
                  #colLabels=col_labels,

the_table.set_fontsize(24)
the_table.scale(3, 2)
canvas3 = FigureCanvasTkAgg(plotFigure, master=window)
canvas3.show()
canvas3.get_tk_widget().place(x=10, y=10)

window.mainloop()