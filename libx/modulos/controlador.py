from tkinter import *
from .modelo import Modelo
from .vista import Vista
from .validacion import Validacion

class Controlador:
    
    def __init__(self,):
        self.m = Modelo(self)
        self.v = Vista(self)
        
    def actualizar_tree(self, tree):
        lib_data = []
        l = tree.get_children()
        for i in l:
            tree.delete(i)
        
        lib_data = self.m.actualizar_tabla() 
        if lib_data != []:
            for i in lib_data:
                tree.insert('', 0,text= '',values = (str(i[1]),str(i[2]),str(i[0])))
            
        
    def alta(self, tree, titulo, autor):
        data = self.m.actualizar_tabla()
        if not Validacion.check_equals(titulo, autor, data):
            print("El libro ya está registrado")
            return False 
        if not Validacion.check_campos(titulo, autor):
            print("Ingrese caracteres válidos")
            return False
        
        self.m.alta_db(titulo, autor)
        self.actualizar_tree(tree)
        
    def borrar(self, tree):
        select = tree.selection()
        row = tree.item(select)
        id = row['values'][2]
        self.m.baja_db(id)
        self.actualizar_tree(tree)
        
    def editar(self, tree, titulo, autor):
        data = self.m.actualizar_tabla()
        if not Validacion.check_equals(titulo, autor, data):
            print("El libro ya está registrado")
            return False 
        if not Validacion.check_campos(titulo, autor):
            print("Ingrese caracteres válidos")
            return False    
        
        select = tree.selection()
        row = tree.item(select)
        id = row['values'][2]    
        self.m.edit_db(id, titulo, autor)
        self.actualizar_tree(tree)
        
    def consulta(self,):
        data = self.m.actualizar_tabla()
        print(data)
        
        
        
