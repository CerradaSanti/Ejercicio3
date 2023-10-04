import Pet

class AnalizadorDatos:
    def __init__(self, mascotas_mapa):
        self.mascotas_mapa = mascotas_mapa


    def crearMapaMascotasMismoNombre(self):#mapa generado
        mapaMascotasVendidas = {}

        for mascota in self.mascotas_mapa:
            nombre = mascota.get("name")
            if nombre:
                nombre = nombre.strip()
                if nombre in mapaMascotasVendidas:
                    mapaMascotasVendidas[nombre] += 1
                else:
                    mapaMascotasVendidas[nombre] = 1

        return mapaMascotasVendidas

def iniciar():
    listadoAnimalesVendidos = Pet.findByStatus()
    datosMascota = AnalizadorDatos(listadoAnimalesVendidos)
    resultado = datosMascota.crearMapaMascotasMismoNombre()

    return print(resultado)
