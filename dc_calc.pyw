from tkinter import *
from tkinter import ttk

def calculator(*args):
    try:
        base = float(input("Dano inicial: "))
        adicional = float(input("Dano secundário: "))
        per_a = float(input("Porcentagem de dano adicional: "))
        dano_t = base + adicional+(base+adicional*(per_a/100))
        print(f"Dano total da armas: {dano_t}")
    except ValueError:
        pass 


def calculate(*args):
    try:
        dano1 = float(base.get())
        dano2 = float(adicional.get())
        per_a = float(percentual.get())
        total.set(float((dano1 + dano2)+((dano1+dano2)*(per_a/100))))
    except ValueError:
        pass

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

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=5, sticky=W)

ttk.Label(mainframe, text="Dano Base: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Dano adicional: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Percentual adicional de dano: ").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Dano total da arma: ").grid(column=1, row=4, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

base_Entrada.focus()
root.bind("<Return>", calculate)

root.mainloop()

