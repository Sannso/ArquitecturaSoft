from tkinter import *
from tkinter import ttk
import tkinter
import main as mn
import pandas as pd


def principalView(root):
    frm = ttk.Frame(root, padding=10)
    frm.place(relwidth=1, relheight=1)
    formData(root, frm)

def formData(root, frm):
    departamento = tkinter.StringVar()
    limit = tkinter.StringVar()

    ttk.Label(frm, text="Ingrese departamento").place(relx=0.1, rely=0.1)
    ttk.Label(frm, text="Ingrese limite de datos a mostrar").place(relx=0.3, rely=0.1)

    ttk.Entry(frm, width=20, textvariable=departamento).place(relx=0.1, rely=0.15)
    ttk.Entry(frm, width=20, textvariable=limit).place(relx=0.3, rely=0.15)

    
    ttk.Button(frm, text="Buscar", command=lambda:(refresh(root, frm, departamento.get(), limit.get()))).place(relx=0.6, rely=0.13)

def tabla(frm, data):
    columns = ('ciudad_municipio_nom', 'departamento_nom', 'edad',
                 'sexo', 'estado', 'pais_procedencia')
    print(data)
    tree = ttk.Treeview(frm, height=15, columns=columns, show='headings')
    tree.place(relx=0.015, rely=0.22)
    tree.heading('ciudad_municipio_nom', text='Ciudad Ubicacion', anchor=CENTER)
    tree.column('ciudad_municipio_nom', minwidth=0, width=150, stretch=NO)

    tree.heading('departamento_nom', text='Departamento', anchor=CENTER)
    tree.column('departamento_nom', minwidth=0, width=120, stretch=NO)

    tree.heading('edad', text='Edad', anchor=CENTER)
    tree.column('edad', minwidth=0, width=100, stretch=NO)

    tree.heading('sexo', text='Sexo', anchor=CENTER)
    tree.column('sexo', minwidth=0, width=100, stretch=NO)

    tree.heading('estado', text='Estado', anchor=CENTER)
    tree.column('estado', minwidth=0, width=120, stretch=NO)

    tree.heading('pais_procedencia', text='Lugar de Procedencia', anchor=CENTER)
    tree.column('pais_procedencia', minwidth=0, width=130, stretch=NO)


    # add data to the treeview
    for index in data.index:
        value = (data.loc[index].ciudad_municipio_nom,
                 data.loc[index].departamento_nom,
                 data.loc[index].edad,
                 data.loc[index].sexo,
                 data.loc[index].estado,
                 data.loc[index].pais_viajo_1_nom)
        tree.insert('', 'end', values=value)


    scrollbar = ttk.Scrollbar(frm, orient='vertical', command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.945, rely=0.22)

def refresh(root, frm, departamento, limit):
    data = mn.getData(departamento, limit)
    for widget in frm.winfo_children():
        widget.destroy()
    formData(root, frm)
    tabla(frm, data)
