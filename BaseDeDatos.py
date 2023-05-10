#Aqui van las funciones de base de datos
import sqlite3



def verificar_credenciales(matricula, password):
    # Establecer la conexión a la base de datos
    conn = sqlite3.connect('microdex.db')
    cursor = conn.cursor()

    # Verificar las credenciales en la tabla "Usuarios"
    cursor.execute("SELECT * FROM Usuarios WHERE Matricula=? AND Password=?", (matricula, password))
    usuario = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conn.close()

    return usuario


def insertar_usuario(nombre, matricula, password, rol):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Usuarios (Nombre, Matricula, Password, Rol) VALUES (?, ?, ?, ?)",
        (nombre, matricula, password, rol)
    )
    conn.commit()
    conn.close()

def actualizar_contraseña(nombre, matricula, nueva_contrasena):
    with sqlite3.connect("microdex.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Usuarios SET Password = ? WHERE Nombre = ? AND Matricula = ?",
            (nueva_contrasena, nombre, matricula)
        )
        if cursor.rowcount == 1:
            conn.commit()
            return True
        else:
            return False
        