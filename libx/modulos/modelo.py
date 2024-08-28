import os
import sqlite3
from peewee import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(BASE_DIR,'libreria.db')

db = SqliteDatabase(ruta_db)

class BaseModel(Model):
    class Meta:
        database = db

class Libreria(BaseModel):
    titulo = CharField()
    autor = CharField()    
    
db.connect()
db.create_tables([Libreria])


class Modelo():
    
    tabla = []
    
    def __init__(self, controlador):
        self.ctrl = controlador
        
    def actualizar_tabla(self,):
        global tabla
        tabla = []
        for row in Libreria.select():
            tabla.append((row.id,row.titulo,row.autor))
        return tabla
         
    def alta_db(self, titulo, autor):
        libreria = Libreria()
        libreria.titulo = titulo
        libreria.autor = autor
        libreria.save()
        
    def baja_db(self,id):
        deleting = Libreria.get(Libreria.id == id)
        deleting.delete_instance()
    
    def edit_db(self, id, t, a):
        updating = Libreria.update(titulo = t, autor = a).where(Libreria.id == id)
        updating.execute()
 