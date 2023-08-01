import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import numpy as np


def plot():
    ax.clear()
    x = np.random.randint(0,10,10)
    y = np.random.randint(0,10,10)
    ax.scatter(x,y)
    canvas.draw()
root=tk.Tk()
fig,ax = plt.subplots()


frame = tk.Frame(root)
label = tk.Label(text="MAtplotlib + Tkinter!")
label.config(font=('courier',32))
label.pack()

canvas = FigureCanvasTkAgg()
canvas.get_tk_widget().pack()


toolbar = NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="w",fill=tk.X)

frame.pack()

tk.Button(frame,text = 'Plot graph',command=plot).pack(pady = 10)


root.mainloop()