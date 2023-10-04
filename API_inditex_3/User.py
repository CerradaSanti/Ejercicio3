import requests

def createMyUser():

    createUserEndpoint = "https://direccion.com/api/v1/usuarios/user"
    myUser = {
      "id": 0,
      "username": "Santiago",
      "firstName": "Cerrada",
      "lastName": "Fernandez",
      "email": "test@gmail.com",
      "password": "admin",
      "phone": "600000000",
      "userStatus": 0
    }

    response = requests.post(createUserEndpoint, json=myUser)

    if response.status_code == 200:
        print("Usuario creado exitosamente.")
    else:
        print("Error al crear el usuario:", response.status_code)


def getMyUser():
    getUserEndpoint = "https://direccion.com/api/v1/usuarios/Santiago"
    response = requests.get(getUserEndpoint)

    if response.status_code == 200:

        datosRespuesta = response.json()

        print("id :", datosRespuesta["id"])
        print("username :", datosRespuesta["username"])
        print("firstName :", datosRespuesta["firstName"])
        print("lastName :", datosRespuesta["lastName"])
        print("email: ", datosRespuesta["email"])
        print("password:", datosRespuesta["password"])
        print("phone :", datosRespuesta["phone"])
        print("userStatus :", datosRespuesta["userStatus"])
    else:
        print("Error al obtener los datos del usuario:", response.status_code)