import re

class Correo ():
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

correo_uno = Correo("nacho1@yahoo.com")
correo_dos = Correo("nacho2@hotmail.com")
correo_tres = Correo("nacho3@bing.com")
correo_cuatro = Correo("nacho4@gmail.com")

correos = [correo_uno, correo_dos, correo_tres, correo_cuatro]
for i in correos:
    print(i.validar())
