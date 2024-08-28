import os
from tkinter import Tk, Button, Entry, Label, LabelFrame, Frame, ttk, CENTER, RIGHT, X, Y, W, N, Scrollbar

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_icon = os.path.join(BASE_DIR,'assets','icon.ico')

class Vista:
    
    def __init__(self, controlador):
        self.ctrl = controlador
        self.root = Tk()
        self.ventana()
        self.root.mainloop()
    
    def ventana(self):
        self.root.title('Lib - Alx')
        self.root.iconbitmap(ruta_icon)
        self.root.geometry('600x400')
        self.root.configure(background='#B2AE93')
        
        self.style_tview()
        self.data_tview()
        
        
    def style_tview(self,):
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Treeview",
                    background ="#D8D5C0",
                    foreground = "black",
                    rowheight = 25,
                    fieldbackground ="#D8D5C0")
        self.style.map("Treeview", background = [("selected", "#ADA694")])
        
    def data_tview(self,):
        #TREE
        tree_frame = Frame(self.root)
        tree_frame.pack(anchor=CENTER, pady=5,padx=20)
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT,fill = Y)
        
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

        tree_scroll.config(command=my_tree.yview)

        my_tree['columns'] = ['Titulo','Autor','ID DB']
        my_tree.column("#0", width = 0, stretch=False, anchor=W)
        my_tree.column("Titulo", width = 150 , anchor = CENTER)
        my_tree.column("Autor", width = 200 , anchor = CENTER)
        my_tree.column("ID DB", width = 50 , anchor = CENTER)
        
        my_tree.heading("#0", text = 'Libros')
        my_tree.heading("Titulo", text = 'Titulo')
        my_tree.heading("Autor", text = 'Autor')
        my_tree.heading("ID DB", text = 'ID DB')    
        
        
        self.ctrl.actualizar_tree(my_tree)
        
        
        my_tree.pack()
    
        #CAMPOS DE TEXTO#
        data_frame = LabelFrame(self.root, background = "#D8D5C0", text = 'Datos')
        data_frame.pack(anchor= N, fill = X, expand = 'yes', padx = 0)

        data_titulo = Label(data_frame, background='#D8D5C0', width=10, text= "Titulo: ", padx=5)
        data_titulo.grid(row = 0, column = 0)
        
        entry_titulo = Entry(data_frame)
        entry_titulo.grid(row = 0, column = 1)

        data_autor = Label(data_frame, background='#D8D5C0', width=10, text= "Autor: ", padx= 5)
        data_autor.grid(row = 0, column = 3)
        
        entry_autor = Entry(data_frame)
        entry_autor.grid(row = 0, column = 4)
        
        #BOTONES#
        button_frame = LabelFrame(self.root, background = "#D8D5C0", text = "Acciones")
        button_frame.pack(anchor= N, fill = X, expand = 'yes', padx = 0)

        borrar_button = Button(button_frame, text ='Borrar', padx= 10, pady=10, width = 13, command=lambda:self.ctrl.borrar(my_tree))
        borrar_button.grid (row = 0, column = 1)
        
        consultar_button = Button(button_frame, text ='Consultar', padx= 10, pady=10, width = 13, command=self.ctrl.consulta)
        consultar_button.grid (row = 0, column = 2)
        
        agregar_button = Button(button_frame, text ='Agregar', padx= 10, pady=10, width = 13, command = lambda:self.ctrl.alta(my_tree,entry_titulo.get(),entry_autor.get()))
        agregar_button.grid (row = 0, column = 3)
        
        editar_button = Button(button_frame, text ='Editar', padx= 10, pady=10, width = 13, command = lambda:self.ctrl.editar(my_tree,entry_titulo.get(),entry_autor.get()))
        editar_button.grid (row = 0, column = 4)
        

