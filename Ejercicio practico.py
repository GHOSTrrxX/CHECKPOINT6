class Usuario:
    def __init__(self, usuario, contraseña):
      self.usuario=usuario
      self.contraseña=contraseña

usuario= Usuario("DANIEL", "1234")

print("Usuario", usuario.usuario)
print("contraseña" , usuario.contraseña)