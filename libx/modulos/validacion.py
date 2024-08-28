import re

class Validacion:
    
    def __init__ (self, ):
        pass
    
    def check_campos(titulo, autor):
        patron = re.compile(r"^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
        if ((patron.search(str(titulo)) is not None) and (patron.search(str(autor)) is not None)):
            return True
        else:
            return False
        
    def check_equals(titulo, autor, data):
        if (data == []):
            return True
        for i in data:
            if (titulo == i[1]) and (autor == i[2]):
                return False
        return True
            