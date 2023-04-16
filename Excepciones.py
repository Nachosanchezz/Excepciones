import re

class (Correo):
    def __init__(self, correo):
        self.correo = correo

    def validar(self):
        valida = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.correo)
        