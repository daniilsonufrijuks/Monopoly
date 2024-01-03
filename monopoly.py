import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import random
from tkinter import ttk
from tkinter import * 

# ------------ functions ---------------
global rand_num, MONEY, COUNTER
MONEY = 1000
COUNTER = 0
def generate_data(): 
    global rand_num
    rand_num = random.randint(0, 100)
    return rand_num

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

def func_buy():
    global MONEY, COUNTER
    MONEY = MONEY - rand_num
    COUNTER += 1
    result_label1.config(text=str(MONEY))
    
def func_sold():
    global MONEY, COUNTER
    MONEY = MONEY + rand_num
    COUNTER -= 1
    if COUNTER == -1:
        COUNTER = 0
    if COUNTER > 0:
        result_label1.config(text=str(MONEY))

# ------------ functions ---------------
    
root = tk.Tk()
root.geometry('800x800')
root.title('<-<-<Monopoly>->->')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)


# ------------------------------------------------------------
frame = tk.Frame(notebook, width=800, height=550)
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame.pack_propagate(False)
notebook.add(frame, text='MONOPOLY')


fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)

window_size = 30
data = [0] * window_size

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

ani = FuncAnimation(fig, update_plot, interval=2000)

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
