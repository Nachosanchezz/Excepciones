import re

class (Correo):
    def __init__(self, correo):
        self.correo = correo

    def validar(self):
        valida = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.correo)
        introducirCorreo = input("->")
        if valida:
            if introducirCorreo == self.correo:
                nombre = ""
                for i in self.correo:
                    if i == "@":
                        break
                    else:
                        nombre += i
                nombre = nombre.capitalize()
                return "Bienvenido " + nombre
            else:
                raise Exception("El correo no coincide")
        else:
            return "Correo no valido"

