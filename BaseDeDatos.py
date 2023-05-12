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

def consultar_tecnicas():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM Tecnica")
    tecnicas = cursor.fetchall()
    return tecnicas

def consultar_tinciones():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM Tincion")
    tinciones = cursor.fetchall()
    return tinciones

def consultar_laminillas():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Laminilla")
    laminillas = cursor.fetchall()
    return laminillas

def insertar_laminillas(numerodelaminilla, tipodemuestra, especie, tincion, observacion):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Laminilla (NumeroDeLaminilla, TipoDeMuestra, Especie, Tincion, Observacion) VALUES (?, ?, ?, ?, ?)",
        (numerodelaminilla, tipodemuestra, especie, tincion, observacion)
    )
    conn.commit()
    conn.close()

def insertar_tincion(nombre, descripcion):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Tincion (nombre, descripcion) VALUES (?, ?)",
        (nombre, descripcion)
    )
    conn.commit()
    conn.close()
def insertar_tecnica(nombre, descripcion):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Tecnica (Nombre, Descripcion) VALUES (?, ?)",
        (nombre, descripcion)
    )
    conn.commit()
    conn.close()

def insertar_roles(nombre,descripcion):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Roles (Nombre, Descripcion) VALUES (?, ?)",
        (nombre, descripcion)
    )
    conn.commit()
    conn.close()

def insertar_carreras(nombre,descripcion):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Carreras (Nombre, Descripcion) VALUES (?, ?)",
        (nombre, descripcion)
    )
    conn.commit()
    conn.close()

def insetar_alumnos(nombre,carrera,matricula):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Alumnos (Nombre, Carrera, Matricula) VALUES (?, ?, ?)",
        (nombre, carrera, matricula)
    )
    conn.commit()
    conn.close()

def insertar_observacion(especie,idtecnica,tipomuestra,idtincion,coordenadas,origenmuestra,numeroimagen):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Observacion (Especie, IdTecnica, TipoMuestra, IdTincion, Coordenadas, OrigenMuestra, NumeroImagen) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (especie, idtecnica, tipomuestra, idtincion, coordenadas, origenmuestra, numeroimagen)
    )
    conn.commit()
    conn.close()

def consulta_carreras():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM Carreras")
    carreras = cursor.fetchall()
    return carreras

def consulta_alumnos():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM Alumnos")
    alumnos = cursor.fetchall()
    return alumnos



def consulta_roles():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM Roles")
    roles = cursor.fetchall()
    return roles


#Consulta para obtener datos hacia el treeview

def obtener_datos_laminilla():
    conn = sqlite3.connect("microdex.db")  # Reemplaza "ruta_a_tu_base_de_datos.db" con la ruta a tu archivo de base de datos
    cursor = conn.cursor()
    cursor.execute("SELECT IdLaminilla, NumeroDeLaminilla, TipoDeMuestra, Especie, Tincion, Observacion FROM Laminilla")
    datos_laminilla = cursor.fetchall()
    conn.close()
    return datos_laminilla

def insertar_tipomuestra(nombre,descripcion):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO TipoMuestra (Nombre, Descripcion) VALUES (?, ?)",
        (nombre, descripcion)
    )
    conn.commit()
    conn.close()

def consultar_tipomuestra():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM TipoMuestra")
    tipomuestra = cursor.fetchall()
    return tipomuestra

def insertar_alumno(nombre, carrera, matricula):
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Alumnos (Nombre, Carrera, Matricula) VALUES (?, ?, ?)",
        (nombre, carrera, matricula)
    )
    conn.commit()
    conn.close()

def consultar_observacion():
    conn = sqlite3.connect("microdex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Especie, Tecnica, TipoDeMuestra, Tincion, Coordenadas, OrigenDeMuestra, NumeroDeImagen FROM Observacion")
    observacion = cursor.fetchall()
    return observacion