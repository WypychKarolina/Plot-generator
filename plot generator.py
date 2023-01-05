"""Program which plots whatever you want"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib import *
from numpy import *

def constant_function(x, i):
    """Create a numpy.ndarray filled with i and with length equal length of x.

    Keyword arguments
    x -- arguments on x axis 
    i -- value which must be repeated in numpy.ndarray
    
    return: numpy.ndarray which contain i x-length times
    """
    return full(x.shape, i)

def replacing(equations):
    """Replace input symbol to symbol understable for Python

    Keyword argument
    equations -- symbol which is supposed to be replaced

    for constant function use constant_function(x,y)
    diplay a warning when formula is unproper
    
    return: replaced symbol
    """
    equations = equations.replace("^","**")
    return equations
    
def plotting():
    """Draw a plot

        return: plot
    """ 
    fig = Figure(figsize = (5,5), dpi = 100)
    my_plot = fig.add_subplot(111)
    fig = Figure(figsize = (5,5), dpi = 100)
    my_plot = fig.add_subplot(111)

    if (float(x_from_value.get())>=float(x_to_value.get())
        or float(y_from_value.get())>=float(y_to_value.get())):
        messagebox.showwarning("BAD RANGE!","From must be less than to.")
    else:   
        x = linspace(float(x_from_value.get()),float(x_to_value.get()), 100)
    
    formulas = formula.get()
    equations = formulas.split(";")

    for i in equations:
        if "," in formulas:
            messagebox.showwarning("DON'T DO THAT!","Separate formulas with \",\", please.")

        elif "/0" in formulas:
            messagebox.showwarning("DON'T DO THAT!","Dividing by zero is unacceptable.")
        else:
            try:
                float(i)
                y = constant_function(x,float(i))
                my_plot.plot(x,y)
            except:
                f = eval("lambda x: " + replacing(i))
                y = f(x)
                my_plot.plot(x,y)

            
            my_plot_canvas = FigureCanvasTkAgg(fig, root)
            my_plot_canvas.draw()
            my_plot_canvas.get_tk_widget().place(height=380, width = 500,
                                                          x = 650, y = 100)

        if int(tick.get()) == 1:
            my_plot.legend(equations)
            
        my_plot.set_xlabel(str(horizontal_name.get()))
        my_plot.set_ylabel(str(vertical_name.get()))
        my_plot.set_title(str(title.get()))
        my_plot.set_xlim(float(x_from_value.get()),float(x_to_value.get()))
        my_plot.set_ylim(float(y_from_value.get()),float(y_to_value.get()))
    return fig


root= Tk()
root.title("Plot's drafter")
canvas1 = Canvas(root, width = 1200, height = 600,  relief = 'raised')
canvas1.pack()

head_label = Label(root, text='Let me draw your plot!')
head_label.config(font=('courier 25 bold'), fg = "black", bg = "pink",)
canvas1.create_window(500, 50, window=head_label)




x_range = Label(root, text='x range:')
x_range.config(font=('courier 18 bold'), bg = "pink")
canvas1.create_window(200, 130, window=x_range)

x_from_label = Label(root, text='From:')
x_from_label.config(font=('courier 15 bold'))
canvas1.create_window(80, 170, window=x_from_label)

x_to_label = Label(root, text='To:')
x_to_label.config(font=('courier 15 bold'))
canvas1.create_window(280, 170, window=x_to_label)

x_from_value = Entry(root, width = 8)
x_from_value.insert(0,'Number')
x_from_value.config(font=('courier 13 bold'))
canvas1.create_window(160, 170, window = x_from_value)

x_to_value = Entry(root, width = 8)
x_to_value.insert(0,'Number')
x_to_value.config(font=('courier 13 bold'))
canvas1.create_window(350, 170, window = x_to_value)







y_range = Label(root, text='y range:')
y_range.config(font=('courier 18 bold'), bg = "pink")
canvas1.create_window(200, 230, window=y_range)

y_from_label = Label(root, text='From:')
y_from_label.config(font=('courier 15 bold'))
canvas1.create_window(80, 270, window=y_from_label)

y_to_label = Label(root, text='To:')
y_to_label.config(font=('courier 15 bold'))
canvas1.create_window(280, 270, window=y_to_label)

y_from_value = Entry(root, width = 8)
y_from_value.insert(0,'Number')
y_from_value.config(font=('courier 13 bold'))
canvas1.create_window(160, 270, window = y_from_value)

y_to_value= Entry(root, width = 8)
y_to_value.insert(0,'Number')
y_to_value.config(font=('courier 13 bold'))
canvas1.create_window(350, 270, window = y_to_value)






title_label = Label(root, text='Plot\'s title:')
title_label.config(font=('courier 18 bold'))
canvas1.create_window(135, 330, window=title_label)

title= Entry(root, width = 12)
title.insert(0,'Text')
title.config(font=('courier 13 bold'))
canvas1.create_window(295, 330, window = title)




x_label = Label(root, text='Horizontal axis\' name:')
x_label.config(font=('courier 18 bold'))
canvas1.create_window(200, 380, window=x_label)

horizontal_name = Entry(root, width = 12)
horizontal_name.insert(0,'Text')
horizontal_name.config(font=('courier 13 bold'))
canvas1.create_window(425, 380, window = horizontal_name)





y_label = Label(root, text='Vertical axis\' name:')
y_label.config(font=('courier 18 bold'))
canvas1.create_window(185, 430, window=y_label)

vertical_name= Entry(root, width = 12)
vertical_name.insert(0,'Text')
vertical_name.config(font=('courier 13 bold'))
canvas1.create_window(390, 430, window = vertical_name)





formula_label = Label(root, text='Give me your formula!')
formula_label.config(font=('courier 18 bold'))
canvas1.create_window(185, 480, window = formula_label)

formula = StringVar()
formula= Entry(root, width = 20, textvariable=formula)
formula.insert(0,'Formula')
formula.config(font=('courier 13 bold'))
canvas1.create_window(430, 480, window = formula)


draw_button = Button(root, text='DRAW', command = plotting, bg='pink',
                 fg='white', width = 10, font=('courier 20 bold'), activebackground = 'grey')
canvas1.create_window(850, 550, window = draw_button)




quit_button = Button(root, text = "Quit", command = root.destroy, bg='red',
               fg='white', font=('courier 20 bold'), activebackground = 'grey')
canvas1.create_window(1000,550, window = quit_button)



tick = IntVar()
legend_button = Checkbutton(root, text = "Legend", variable = tick, onvalue = 1,
                      offvalue = 0,  height = 2, width = 8, bg='pink',
                      font=('courier 18 bold'), command = legend)
canvas1.create_window(120, 550, window = legend_button)



root.mainloop()
