import tkinter as tk
win = tk. Tk()

at = tk.Label(win, text = "Zadaj a koeficient:")
at.pack()
a = tk.Entry(win)
a.pack()
bt = tk.Label(win, text = "Zadaj b koeficient:")
bt.pack()
b = tk.Entry(win)
b.pack()
ct = tk.Label (win,text = "Zadaj c koeficient:")
ct.pack()
c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 - 4*ka*kc
    if d <0:
        label = tk.Label(win, text="nema riesenie")
        label.pack()
    elif d==0:
        jednox = -kb / (2 * ka)
        label = tk.Label(win, text = "ma jedno x")
        label.pack()
    else:
        xjedna = ((-kb+d**0.5)/(2*ka))
        xdva = ((-kb-d**0.5)/(2*ka))
        xx = xjedna,xdva
        label = tk.Label(win, text = "ma dve x")
        label.pack()

button = tk.Button(win, text = "vyries", command = executor)
button.pack()

win.mainloop()
