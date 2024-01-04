import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import random
from tkinter import ttk
from tkinter import * 

# ------------ functions ---------------
global rand_num, rand_num2, current_tab_index, MONEY, COUNTER

MONEY = 500
COUNTER = 0


def on_tab_selected(event):
    global current_tab_index
    current_tab_index = notebook.index(notebook.select())


def generate_data(): 
    global rand_num
    rand_num = random.randint(5, 10000)
    return rand_num

def generate_data2(): 
    global rand_num2
    rand_num2 = random.randint(100, 20000)
    return rand_num2



def update_plot(frame): # plot updating
    data_point = generate_data()
    data.append(data_point)
    
    if len(data) > window_size:
        data.pop(0)
    
    ax.clear()
    ax.plot(range(len(data)), data, marker='o')
    ax.set_title('Dynamic Plot')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

def update_plot2(frame): # plot updating
    data_point = generate_data2()
    data2.append(data_point)
    
    if len(data) > window_size2:
        data.pop(0)
    
    ax2.clear()
    ax2.plot(range(len(data2)), data2, marker='o')
    ax2.set_title('Dynamic Plot')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Value')



def func_buy():
    global MONEY, COUNTER
    if current_tab_index == 0:
        MONEY = MONEY - rand_num
    else:
        MONEY = MONEY - rand_num2
    if MONEY > 0: 
        result_label1.config(text=str(MONEY))
        COUNTER += 1
    
def func_sold():
    global MONEY, COUNTER
    if current_tab_index == 0:
        MONEY = MONEY + rand_num
    else:
        MONEY = MONEY + rand_num2
    if COUNTER == -1:
        COUNTER = 0
    if COUNTER > 0:
        result_label1.config(text=str(MONEY))
        COUNTER -= 1

# ------------ functions ---------------
    
root = tk.Tk()
root.geometry('800x800')
root.title('<-<-<Monopoly>->->')



notebook = ttk.Notebook(root)
notebook.bind("<<NotebookTabChanged>>", on_tab_selected)
notebook.pack(pady=10, expand=True)


# ------------------------------------------------------------
frame = tk.Frame(notebook, width=800, height=550)
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame.pack_propagate(False)
notebook.add(frame, text='TESLA')


fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)

window_size = 30
data = [0] * window_size

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

ani = FuncAnimation(fig, update_plot, interval=3000)

# ---- 2

frame2 = tk.Frame(notebook, width=800, height=550)
frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame2.pack_propagate(False)
notebook.add(frame2, text='GOOGLE')


fig2 = Figure(figsize=(5, 4), dpi=100)
ax2 = fig2.add_subplot(1, 1, 1)

window_size2 = 30
data2 = [0] * window_size2

canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
canvas_widget2 = canvas2.get_tk_widget()
canvas_widget2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

ani2 = FuncAnimation(fig2, update_plot2, interval=2000)

# ------------------------------------------------------------

Btn1 = Button(root, text="BUY", command=func_buy, font=("bold", 15))
Btn1.place(x=100, y=750)

Btn2 = Button(root, text="SOLD", command=func_sold, font=("bold", 15))
Btn2.place(x=200, y=750)


result_label = Label(root, text="MONEY: ")
result_label.place(x=50, y=0)
result_label1 = Label(root, text=str(MONEY))
result_label1.place(x=120, y=0)



root.mainloop()
