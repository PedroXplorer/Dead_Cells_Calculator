from tkinter import *
from tkinter import ttk

def calculate(*args):
    total_a.set(total.get())
    try: 
        dano1 = float(base.get())
        dano2 = float(adicional.get())
        per_a = float(percentual.get())
        total.set(float((dano1 + dano2)+((dano1+dano2)*(per_a/100))))
    except ValueError:
        pass

def reset(*args):
    total_a.set(0)
    base.set(0)
    adicional.set(0)
    percentual.set(0)
    total.set(0)

root = Tk()
root.title("Dead Cells Calculadora")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


base = StringVar()
base_Entrada = ttk.Entry(mainframe, width=7, textvariable=base)
base_Entrada.grid(column=2, row=1, sticky=(W, E))

adicional = StringVar()
adicional_Entrada = ttk.Entry(mainframe, width=7, textvariable=adicional)
adicional_Entrada.grid(column=2, row=2, sticky=(W, E))

percentual = StringVar()
percentual_Entrada = ttk.Entry(mainframe, width=7, textvariable=percentual)
percentual_Entrada.grid(column=2, row=3, sticky=(W, E))

total = StringVar()
ttk.Label(mainframe, textvariable=total).grid(column=2, row=4, sticky=(W, E))

total_a = StringVar()        
ttk.Label(mainframe, textvariable=total_a).grid(column=2, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text="Resetar", command=reset).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="Dano Base: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Dano adicional: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Percentual adicional de dano: ").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Dano total da arma: ").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="Dano total calculado anteriormente: ").grid(column=1, row=5, sticky=E)
reset()
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

base_Entrada.focus()
root.bind("<Return>", calculate)

root.mainloop()

