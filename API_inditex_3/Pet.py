import requests

def findByStatus():
    url = "https://direccion.com/api/v1/pet/findByStatus"
    params = {"status": "sold"}

    response = requests.get(url, params=params)
    # {id, name}
    listaMascotasVendidas = []

    if response.status_code == 200:
        mascotas_vendidas = response.json()

        for mascota in mascotas_vendidas:
            id_mascota = mascota.get("id")
            nombre_mascota = mascota.get("name")
            if id_mascota and nombre_mascota:
                tupla = (id_mascota, nombre_mascota)
                listaMascotasVendidas.append(tupla)

    #for id_mascota, nombre_mascota in listaMascotasVendidas:
    #    print("ID: ",{id_mascota}, ", Nombre: ",{nombre_mascota})

        return listaMascotasVendidas

    else:
        print("Error al obtener la lista de mascotas vendidas:", response.status_code)
        return listaMascotasVendidas


