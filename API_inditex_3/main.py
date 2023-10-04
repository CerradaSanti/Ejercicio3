import User
import AnalizadorDatos


class Main:
    def __init__(self):
        pass

    def ejecutar(self):
        User.createMyUser()
        User.getMyUser()
        AnalizadorDatos.iniciar()


if __name__ == "__main__":
    programa_principal = Main()
    programa_principal.ejecutar()
