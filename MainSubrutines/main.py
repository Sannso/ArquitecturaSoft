import graphics as g
import data as d
from tkinter import *
from tkinter import ttk

def main():
    root = Tk(className='Proyecto Arquitectura')
    root.geometry('800x500')
    g.principalView(root)
    root.mainloop()

def getData(departamento, limite):
    departamento = str(departamento).upper()
    print(departamento, " y ", limite)
    limite = int(limite)
    return d.getData(limite, departamento)

if __name__ == "__main__":
    main()