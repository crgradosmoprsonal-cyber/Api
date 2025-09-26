from fastapi import FastAPI
from sqlmodel import SQLModel

class User(SQLModel):
    usuario: str
    contraseña: str

BD = [
    User(usuario="Kati", contraseña="123"),
    User(usuario="Kata", contraseña="hola"),
    User(usuario="Cris", contraseña="xd"),
]

app = FastAPI()

@app.get("/user/{username}/password/{password}")
def read_user(username: str, password: str):
    user = None
    for u in BD:
        if u.usuario == username:
            user = u
            break

    if not user:
        return {"msg": "Usuario no encontrado"}

    if user.contraseña == password:
        return {"msg": f"Has ingresado correctamente a la cuenta de: {username}"}
    else:
        return {"msg": "Clave incorrecta"}
