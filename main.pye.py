import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from BaseDeDatos import *



def iniciar_sesion():
    matricula = entry_usuario.get()
    password = entry_contrasena.get()

    # Verificar las credenciales en la base de datos
    usuario = verificar_credenciales(matricula, password)

    if usuario is not None:
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        if 1 == usuario[0]:
            ventana_login.destroy()  # Cerrar la ventana de inicio de sesión
            mostrar_ventana_principal_admin()  # Mostrar la ventana principal
        else:
            ventana_login.destroy()  # Cerrar la ventana de inicio de sesión
            mostrar_ventana_principal()  # Mostrar la ventana principal
    else:
        messagebox.showerror("Inicio de sesión", "Credenciales incorrectas")

def mostrar_ventana_principal_admin():
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")

    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_principal, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    btn_menuadmi = tk.Button(ventana_principal, text="Menu", command=mostrar_ventana_menu)
    btn_filtrar = tk.Button(ventana_principal, text="Filtrar", command=aplicar_filtro)
    btn_crear = tk.Button(ventana_principal, text="Crear", command=abrir_formulario_laminillas)
    btn_treefil = tk.Button(ventana_principal, text="Filtrar Especie", command=lambda:(filtrar_datos()))
    tabla = ttk.Treeview(ventana_principal, columns=("Laminilla", "NumLaminilla", "TipoMuestra", "Especie", "Tincion","Observaciones"))
    tabla.column("#0", width=0, stretch=tk.NO)
    
    tabla.heading("Laminilla", text="id Laminilla")
    tabla.heading("NumLaminilla", text="#Laminilla")
    tabla.heading("TipoMuestra", text="Tipo de Muestra")
    tabla.heading("Especie", text="Especie")
    tabla.heading("Tincion", text="Tinción")
    tabla.heading("Observaciones", text="Observaciones")


    tabla.column("Laminilla", width=30)
    tabla.column("NumLaminilla", width=30)
    tabla.column("TipoMuestra", width=40)        
    tabla.column("Especie", width=30)    
    tabla.column("Tincion", width=30)
    tabla.column("Observaciones", width=50)
    # Insertar los datos en el Treeview
    datos_laminilla = obtener_datos_laminilla() 

    for datos in datos_laminilla:
        tabla.insert("", "end", values=datos)

    tabla.update()

    # Configurar el ancho y alto del Treeview
    ancho = 550
    alto = 400
    tabla.configure(height=alto)
    tabla.place(x=125, y=200, width=ancho, height=alto)

    # Etiquetas 
    btn_treefil.place(x= 150, y=110)

    label_tec = tk.Label(ventana_principal, text="Tipo de tecnica:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_tec.place(x= 320, y=110)

    label_tri = tk.Label(ventana_principal, text="Trincion:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_tri.place(x= 500, y=110)

    # Crear un Combobox

    tecnicas = consultar_tecnicas()
    tinciones = consultar_tinciones()

    entry_lami = ttk.Entry(ventana_principal)
    entry_lami.place(x=150, y=145)

    combotec = ttk.Combobox(ventana_principal,values = tecnicas)
    combotec.place(x=320, y=145)

    combotri = ttk.Combobox(ventana_principal, values = tinciones)
    combotri.place(x=500, y=145)


    btn_filtrar.place(x=550, y= 40)
    btn_crear.place(x=600, y= 40)
    btn_menuadmi.place(x=750, y=550)

    def filtrar_datos():
        especie_filtrada = entry_lami.get()
        tabla.delete(*tabla.get_children())
        datos_laminilla = obtener_datos_laminilla()
        for datos in datos_laminilla:
            if not especie_filtrada or datos[3] == especie_filtrada:
                tabla.insert("", "end", values=datos)
    

    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_principal.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_principal.resizable(False, False)  # Deshabilitar el cambio de tamaño

    ventana_principal.mainloop()

def mostrar_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")

    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_principal, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

   
    btn_filtrar = tk.Button(ventana_principal, text="Filtrar", command=aplicar_filtro)
    btn_crear = tk.Button(ventana_principal, text="Crear", command=abrir_formulario_laminillas)
    btn_treefil = tk.Button(ventana_principal, text="Filtrar Especie", command=lambda:(filtrar_datos()))
    tabla = ttk.Treeview(ventana_principal, columns=("Laminilla", "NumLaminilla", "TipoMuestra", "Especie", "Tincion","Observaciones"))
    tabla.column("#0", width=0, stretch=tk.NO)
    
    tabla.heading("Laminilla", text="id Laminilla")
    tabla.heading("NumLaminilla", text="#Laminilla")
    tabla.heading("TipoMuestra", text="Tipo de Muestra")
    tabla.heading("Especie", text="Especie")
    tabla.heading("Tincion", text="Tinción")
    tabla.heading("Observaciones", text="Observaciones")


    tabla.column("Laminilla", width=30)
    tabla.column("NumLaminilla", width=30)
    tabla.column("TipoMuestra", width=40)        
    tabla.column("Especie", width=30)    
    tabla.column("Tincion", width=30)
    tabla.column("Observaciones", width=50)
    # Insertar los datos en el Treeview
    datos_laminilla = obtener_datos_laminilla() 

    for datos in datos_laminilla:
        tabla.insert("", "end", values=datos)

    tabla.update()

    # Configurar el ancho y alto del Treeview
    ancho = 550
    alto = 400
    tabla.configure(height=alto)
    tabla.place(x=125, y=200, width=ancho, height=alto)

    # Etiquetas 
    btn_treefil.place(x= 150, y=110)

    label_tec = tk.Label(ventana_principal, text="Tipo de tecnica:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_tec.place(x= 320, y=110)

    label_tri = tk.Label(ventana_principal, text="Trincion:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_tri.place(x= 500, y=110)

    # Crear un Combobox

    tecnicas = consultar_tecnicas()
    tinciones = consultar_tinciones()

    entry_lami = ttk.Entry(ventana_principal)
    entry_lami.place(x=150, y=145)

    combotec = ttk.Combobox(ventana_principal,values = tecnicas)
    combotec.place(x=320, y=145)

    combotri = ttk.Combobox(ventana_principal, values = tinciones)
    combotri.place(x=500, y=145)


    btn_filtrar.place(x=550, y= 40)
    btn_crear.place(x=600, y= 40)

    def filtrar_datos():
        especie_filtrada = entry_lami.get()
        tabla.delete(*tabla.get_children())
        datos_laminilla = obtener_datos_laminilla()
        for datos in datos_laminilla:
            if not especie_filtrada or datos[3] == especie_filtrada:
                tabla.insert("", "end", values=datos)
    

    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_principal.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_principal.resizable(False, False)  # Deshabilitar el cambio de tamaño

    ventana_principal.mainloop()

def mostrar_ventana_registro():
    # Crear la ventana de registro
    ventana_registro = tk.Toplevel(ventana_login)
    ventana_registro.title("Registro de Usuario")


    # Configurar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/2.png")
    label_fondo = tk.Label(ventana_registro, image=imagen_fondo)
    label_fondo.pack()

    # Etiquetas y campos de entrada para el nombre, matrícula y contraseña
    label_nombre = tk.Label(ventana_registro, text="Nombre:", background="#193a68", font=("Arial", 18), foreground="White")
    entry_nombre = tk.Entry(ventana_registro)
    label_matricula = tk.Label(ventana_registro, text="Matrícula:", background="#193a68", font=("Arial", 18), foreground="White")
    entry_matricula = tk.Entry(ventana_registro)
    label_contrasena = tk.Label(ventana_registro, text="Contraseña:",  background="#193a68", font=("Arial", 18), foreground="White")
    entry_contrasena = tk.Entry(ventana_registro, show="*")
    label_rol = tk.Label(ventana_registro, text="Rol:")
    roles = consulta_roles()
    combo_rol = ttk.Combobox(ventana_registro, values=roles)

    # Posicionar las etiquetas y los campos de entrada en la ventana de registro
    label_nombre.place(x=300, y=150)
    entry_nombre.place(x=300, y=180)
    label_matricula.place(x=300, y=220)
    entry_matricula.place(x=300, y=250)
    label_contrasena.place(x=300, y=290)
    entry_contrasena.place(x=300, y=320)


    def crear_usuario():
        nombre = entry_nombre.get()
        matricula = entry_matricula.get()
        contrasena = entry_contrasena.get()
        rol = combo_rol.get()

        # Verificar si no se seleccionó un rol y asignar el valor predeterminado
        if not rol:
            rol = "2"

        # Validar que se hayan ingresado todos los campos
        if nombre and matricula and contrasena:
            # Insertar el usuario en la base de datos
            insertar_usuario(nombre, matricula, contrasena, rol)
            messagebox.showinfo("Registro", "Usuario creado exitosamente")
            ventana_registro.destroy()
        else:
            messagebox.showerror("Registro", "Por favor, ingresa todos los campos")


    # Botón para crear el usuario
    btn_crear = tk.Button(ventana_registro, text="Crear Usuario", command=crear_usuario)
    btn_crear.place(x=300, y=400)

    ventana_registro.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_registro.resizable(False, False)  # Deshabilitar el cambio de tamaño

    ventana_registro.mainloop()
    


def mostrar_ventana_olvidaste_contrasena():
    # Crear la ventana de recuperación de contraseña
    ventana_recuperar_contrasena = tk.Toplevel(ventana_login)
    ventana_recuperar_contrasena.title("Recuperación de Contraseña")

    # Etiquetas y campos de entrada para el nombre, matrícula y nueva contraseña
    label_nombre = tk.Label(ventana_recuperar_contrasena, text="Nombre:")
    entry_nombre = tk.Entry(ventana_recuperar_contrasena)
    label_matricula = tk.Label(ventana_recuperar_contrasena, text="Matrícula:")
    entry_matricula = tk.Entry(ventana_recuperar_contrasena)
    label_nueva_contrasena = tk.Label(ventana_recuperar_contrasena, text="Nueva Contraseña:")
    entry_nueva_contrasena = tk.Entry(ventana_recuperar_contrasena, show="*")

    # Posicionar las etiquetas y los campos de entrada en la ventana de recuperación de contraseña
    label_nombre.pack()
    entry_nombre.pack()
    label_matricula.pack()
    entry_matricula.pack()
    label_nueva_contrasena.pack()
    entry_nueva_contrasena.pack()

    def actualizar_contrasena():
        nombre = entry_nombre.get()
        matricula = entry_matricula.get()
        nueva_contrasena = entry_nueva_contrasena.get()

        # Validar que se hayan ingresado todos los campos
        if nombre and matricula and nueva_contrasena:
            # Actualizar la contraseña en la base de datos
            actualizar_contraseña(nombre, matricula, nueva_contrasena)
            messagebox.showinfo("Recuperación de Contraseña", "Contraseña actualizada exitosamente")
            ventana_recuperar_contrasena.destroy()
        else:
            messagebox.showerror("Recuperación de Contraseña", "Por favor, ingresa todos los campos")

    # Botón para actualizar la contraseña
    btn_actualizar = tk.Button(ventana_recuperar_contrasena, text="Actualizar Contraseña", command=actualizar_contrasena)
    btn_actualizar.pack()

def mostrar_ventana_menu():
    ventana_menu= tk.Toplevel()
    ventana_menu.title("Menu")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_menu, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Etiquetas del menú
    label_opcion1 = tk.Label(ventana_menu, text="Usuarios",  background="#0b3473", font=("Arial", 16), foreground="White")
    label_opcion2 = tk.Label(ventana_menu, text="Laminillas",  background="#0b3473", font=("Arial", 16), foreground="White")
    label_opcion3 = tk.Label(ventana_menu, text="Carreras",  background="#0b3473", font=("Arial", 16), foreground="White")
    label_opcion4 = tk.Label(ventana_menu, text="Tecnicas",  background="#0b3473", font=("Arial", 16), foreground="White")
    label_opcion5 = tk.Label(ventana_menu, text="Roles",     background="#0b3473", font=("Arial", 16), foreground="White")
    label_opcion6 = tk.Label(ventana_menu, text="Tinciones",  background="#0b3473", font=("Arial", 16), foreground="White")
    label_opcion7 = tk.Label(ventana_menu, text="Observacion",     background="#0b3473", font=("Arial", 16), foreground="White")

    # Botones del menú
    btn_accion1 = tk.Button(ventana_menu, text="Acceder", width=20, font=("Arial", 12), command=mostrar_ventana_Usuario123)
    btn_accion2 = tk.Button(ventana_menu, text="Acceder", width=20, font=("Arial", 12), command=abrir_formulario_laminillas)
    btn_accion3 = tk.Button(ventana_menu, text="Acceder", width=20, font=("Arial", 12), command=mostrar_ventana_carrera)
    btn_accion4 = tk.Button(ventana_menu, text="Acceder", width=20, font=("Arial", 12), command=mostrar_ventana_tecnica)
    btn_accion5 = tk.Button(ventana_menu, text="Acceder", width=20, font=("Arial", 12), command=mostrar_ventana_roles)
    btn_accion6 = tk.Button(ventana_menu, text="Acceder", width=20, font=("Arial", 12), command=mostrar_ventana_tincion)
    btn_accion7 = tk.Button(ventana_menu, text="Acceder", width=20, font=("Arial", 12), command=mostrar_ventana_observacion)


    # Posicionamiento de las etiquetas y los botones
    label_opcion1.place(x= 170, y=110)
    btn_accion1.place(x= 170, y=150)
    label_opcion2.place(x= 450, y=110)
    btn_accion2.place(x= 450, y=150)
    label_opcion3.place(x= 170, y=250)
    btn_accion3.place(x= 170, y=290)
    label_opcion4.place(x= 450, y=250)
    btn_accion4.place(x= 450, y=290)
    label_opcion5.place(x= 170, y=390)
    btn_accion5.place(x= 170, y=440)
    label_opcion6.place(x= 450, y=390)
    btn_accion6.place(x= 450, y=440)
    label_opcion7.place(x= 170, y=480)
    btn_accion7.place(x= 170, y=520)




    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_menu.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_menu.resizable(False, False)  # Deshabilitar el cambio de tamaño

    ventana_menu.mainloop()

def aplicar_filtro():
    combotec = combotec.get()
    combotri = combotri.get()



def abrir_formulario_laminillas():
    ventana_formulario = tk.Toplevel()
    ventana_formulario.title("Formulario para Laminillas")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_formulario, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Etiquetas

    label1 = ttk.Label(ventana_formulario, text="Numero de laminilla:",  background="#0b3473", font=("Arial", 16), foreground="White")
    label1.place(x= 150, y=150)

    label2 = ttk.Label(ventana_formulario, text="Especie:", background="#0b3473", font=("Arial", 16), foreground="White" )
    label2.place(x= 450, y=150)

    label4 = ttk.Label(ventana_formulario, text="Tincion:" ,  background="#0b3473", font=("Arial", 16), foreground="White")
    label4.place(x= 150, y=300)

    label3 = ttk.Label(ventana_formulario, text="Tipo de Muestra:" ,  background="#0b3473", font=("Arial", 16), foreground="White")
    label3.place(x=450, y=300)

    label5 = ttk.Label(ventana_formulario, text="Observaciones:" ,  background="#0b3473", font=("Arial", 16), foreground="White")
    label5.place(x= 150, y=400)

    tipomuestra = consultar_tipomuestra()    

    # Campos de entrada
    entry1 = ttk.Entry(ventana_formulario, width=20, font=("Arial", 12)) #Numero de laminilla
    entry1.place(x= 150, y=200)

    entry2 = ttk.Entry(ventana_formulario, width=20, font=("Arial", 12)) # Especie
    entry2.place(x= 450, y=200)

    tincion = consultar_tinciones()
    observacion = consultar_observacion()

    # Cuadros combinados
    combo1 = ttk.Combobox(ventana_formulario, values= tincion,  width=20, font=("Arial", 12)) # Tincion
    combo1.place(x= 150, y=350)

    combo2 = ttk.Combobox(ventana_formulario, values= tipomuestra,  width=20, font=("Arial", 12)) # Tipo Muestra
    combo2.place(x= 450, y=350)

    combo3 = ttk.Combobox(ventana_formulario, values= observacion, width=40, font=("Arial", 12)) # Observaciones
    combo3.place(x= 150, y= 440)
  
    def insertar_laminilla():
        numero_laminilla = entry1.get()
        tipo_muestra = combo2.get()
        especie = entry2.get()
        tincion = combo1.get()
        observacion = combo3.get()
        if numero_laminilla and tipo_muestra and especie and tincion and observacion:
            insertar_laminillas(numero_laminilla, tipo_muestra, especie, tincion, observacion)
            messagebox.showinfo(title="Laminilla", message="Laminilla guardada con éxito")
        else:
            messagebox.showinfo(title="Laminilla", message="Laminilla guardada con éxito")

    # Botón Guardar
    boton_guardar = ttk.Button(ventana_formulario, text="Guardar", command=insertar_laminilla)
    boton_guardar.place(x=350, y=500)

    ventana_formulario.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_formulario.resizable(False, False)  # Deshabilitar el cambio de tamaño   
    ventana_formulario.mainloop()




def mostrar_ventana_tecnica():
    ventana_tecnica= tk.Toplevel()
    ventana_tecnica.title("Tecnica")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_tecnica, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Etiquetas
    label1 = ttk.Label(ventana_tecnica, text="Tecnica", background="#0b3473", font=("Arial", 20), foreground="White")
    label1.place(x=250, y=90)
    
    label2 = ttk.Label(ventana_tecnica, text="Nombre", background="#0b3473", font=("Arial", 18), foreground="White")
    label2.place(x=250, y=150)
    
    label3 = ttk.Label(ventana_tecnica, text="Descripcion", background="#0b3473", font=("Arial", 18), foreground="White")
    label3.place(x=250, y=210)
    
    
    entry1 = ttk.Entry(ventana_tecnica, width=30)
    entry1.place(x=250, y=180)

    # Campo de comentarios
    comentarios = tk.Text(ventana_tecnica, width=40, height=10)
    comentarios.place(x=250, y=240)

    def crear_tecnica():
        nombre = entry1.get()
        descripcion = comentarios.get("1.0", tk.END)
        if nombre and descripcion:
            insertar_tecnica(nombre, descripcion)
            messagebox.showinfo(message="Carrera creada con éxito", title="Éxito")
            ventana_tecnica.destroy()
        else:
            messagebox.showerror(message="Faltan campos", title="Error")

    # Botón Guardar
    btn_guardar = tk.Button(ventana_tecnica, text="Guardar", command=crear_tecnica)
    btn_guardar.place(x=350, y=490)

    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_tecnica.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_tecnica.resizable(False, False)  # Deshabilitar el cambiventana_tecnica
    ventana_tecnica.mainloop()

def mostrar_ventana_tincion():
    ventana_tincion= tk.Toplevel()
    ventana_tincion.title("Tincion")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_tincion, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Etiquetas
    label1 = ttk.Label(ventana_tincion, text="Tincion", background="#0b3473", font=("Arial", 20), foreground="White")
    label1.place(x=250, y=90)
    
    label2 = ttk.Label(ventana_tincion, text="Nombre", background="#0b3473", font=("Arial", 18), foreground="White")
    label2.place(x=250, y=150)
    
    label3 = ttk.Label(ventana_tincion, text="Descripcion", background="#0b3473", font=("Arial", 18), foreground="White")
    label3.place(x=250, y=210)
    
    
    entry1 = ttk.Entry(ventana_tincion, width=30)
    entry1.place(x=250, y=180)

    # Campo de comentarios
    comentarios = tk.Text(ventana_tincion, width=40, height=10)
    comentarios.place(x=250, y=240)
    
    def crear_tincion():
        nombre = entry1.get()
        descripcion = comentarios.get("1.0", tk.END)
        if nombre and descripcion:
            insertar_tincion(nombre, descripcion)
            messagebox.showinfo(message="Carrera creada con éxito", title="Éxito")
            ventana_tincion.destroy()
        else:
            messagebox.showerror(message="Faltan campos", title="Error")

    # Botón Guardar
    btn_guardar = tk.Button(ventana_tincion, text="Guardar", command=crear_tincion)
    btn_guardar.place(x=350, y=490)


    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_tincion.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_tincion.resizable(False, False)  # Deshabilitar el cambiventana_tecnica
    ventana_tincion.mainloop()


def mostrar_ventana_alumno():
    ventana_alumno= tk.Toplevel()
    ventana_alumno.title("Formulario para Laminillas")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_alumno, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Etiquetas
    label1 = ttk.Label(ventana_alumno, text="Nombre:",  background="#0b3473", font=("Arial", 16), foreground="White")
    label1.place(x= 150, y=110)
    
    label2 = ttk.Label(ventana_alumno, text="Matricula",  background="#0b3473", font=("Arial", 16), foreground="White")
    label2.place(x= 150, y=200)
    
    label3 = ttk.Label(ventana_alumno, text="Carrera",  background="#0b3473", font=("Arial", 16), foreground="White")
    label3.place(x= 150, y=280)
    
    label4 = ttk.Label(ventana_alumno, text="Alumnos",  background="#0b3473", font=("Arial", 20), foreground="White")
    label4.place(x= 340, y=80)

    # Campos de entrada
    entry1 = ttk.Entry(ventana_alumno, width=40)
    entry1.place(x= 150, y=150)
    
    entry2 = ttk.Entry(ventana_alumno, width=40)
    entry2.place(x=150, y=240)
    
    entry3 = ttk.Entry(ventana_alumno, width=40)
    entry3.place(x=150, y=320)
    
    def crear_alumno():
        nombre = entry1.get()
        matricula = entry2.get()
        carrera = entry3.get()
        if nombre and matricula and carrera:
            insertar_alumno(nombre, matricula, carrera)
            messagebox.showinfo(message="Alumno creado con éxito", title="Éxito")
            ventana_alumno.destroy()
        else:
            messagebox.showerror(message="Faltan campos", title="Error")
    
    # Botón Guardar
    btn_guardar = tk.Button(ventana_alumno, text="Guardar", command=crear_alumno)
    btn_guardar.place(x=350, y=490)

    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_alumno.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_alumno.resizable(False, False)  # Deshabilitar el cambiventana_tecnica
    ventana_alumno.mainloop()

def mostrar_ventana_carrera():
    ventana_carrera= tk.Toplevel()
    ventana_carrera.title("Carrera")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_carrera, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Etiquetas
    label1 = ttk.Label(ventana_carrera, text="Nombre:",  background="#0b3473", font=("Arial", 16), foreground="White")
    label1.place(x= 150, y=110)
    
    label2 = ttk.Label(ventana_carrera, text="Descripcion",  background="#0b3473", font=("Arial", 16), foreground="White")
    label2.place(x= 150, y=200)
    
    
    
    label4 = ttk.Label(ventana_carrera, text="Carrera",  background="#0b3473", font=("Arial", 20), foreground="White")
    label4.place(x= 340, y=80)

    # Campos de entrada
    entry1 = ttk.Entry(ventana_carrera, width=40)
    entry1.place(x= 150, y=150)
    
    entry2 = ttk.Entry(ventana_carrera, width=40)
    entry2.place(x=150, y=240)
    
    def crear_carrera():
        nombre = entry1.get()
        descripcion = entry2.get()
        if nombre and descripcion:
            insertar_carreras(nombre, descripcion)
            messagebox.showinfo(message="Carrera creada con éxito", title="Éxito")
            ventana_carrera.destroy()
        else:
            messagebox.showerror(message="Faltan campos", title="Error")  
  
    
    # Botón Guardar
    btn_guardar = tk.Button(ventana_carrera, text="Guardar",command=crear_carrera)
    btn_guardar.place(x=350, y=490)

    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_carrera.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_carrera.resizable(False, False)  # Deshabilitar el cambiventana_tecnica
    ventana_carrera.mainloop()

def mostrar_ventana_roles():
    ventana_roles= tk.Toplevel()
    ventana_roles.title("Roles")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_roles, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Etiquetas
    label1 = ttk.Label(ventana_roles, text="Nombre:",  background="#0b3473", font=("Arial", 16), foreground="White")
    label1.place(x= 150, y=110)
    
    label2 = ttk.Label(ventana_roles, text="Descripcion",  background="#0b3473", font=("Arial", 16), foreground="White")
    label2.place(x= 150, y=200)
    
    
    
    label4 = ttk.Label(ventana_roles, text="Roles",  background="#0b3473", font=("Arial", 20), foreground="White")
    label4.place(x= 340, y=80)

    # Campos de entrada
    entry1 = ttk.Entry(ventana_roles, width=40)
    entry1.place(x= 150, y=150)
    
    entry2 = ttk.Entry(ventana_roles, width=40)
    entry2.place(x=150, y=240)
    
    def crear_roles():
        nombre = entry1.get()
        descripcion = entry2.get()
        if nombre and descripcion:
            insertar_roles(nombre, descripcion)
            messagebox.showinfo(message="Rol creado con éxito", title="Éxito")
            ventana_roles.destroy()
        else:
            messagebox.showerror(message="Faltan campos", title="Error")
    
    # Botón Guardar
    btn_guardar = tk.Button(ventana_roles, text="Guardar", command=crear_roles)
    btn_guardar.place(x=350, y=490)

    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_roles.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_roles.resizable(False, False)  # Deshabilitar el cambiventana_tecnica
    ventana_roles.mainloop()

def mostrar_ventana_Usuario123():
    ventana_Usuario1= tk.Toplevel()
    ventana_Usuario1.title("Usuario")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_Usuario1, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

     # Etiquetas
    label1 = ttk.Label(ventana_Usuario1, text="NOMBRE",  background="#0b3473", font=("Arial", 16), foreground="White")
    label1.place(x=150, y=130)
    
    label2 = ttk.Label(ventana_Usuario1, text="PASSWORD",  background="#0b3473", font=("Arial", 16), foreground="White")
    label2.place(x=150, y=200)
    
    label3 = ttk.Label(ventana_Usuario1, text="MATRICULA",  background="#0b3473", font=("Arial", 16), foreground="White")
    label3.place(x=150, y=270)
    
    label4 = ttk.Label(ventana_Usuario1, text="ROL",  background="#0b3473", font=("Arial", 16), foreground="White")
    label4.place(x=150, y=340)
    
    # Campos de entrada
    entry1 = ttk.Entry(ventana_Usuario1, width=30)
    entry1.place(x=150, y=160)
    
    entry2 = ttk.Entry(ventana_Usuario1, width=30)
    entry2.place(x=150, y=300)
    
    # Campo de contraseña
    entry_password = ttk.Entry(ventana_Usuario1, show="*", width=30)
    entry_password.place(x=150, y=230)
    
    roles = consulta_roles()
    # Cuadro combinado
    combo1 = ttk.Combobox(ventana_Usuario1, values=roles, width=30)
    combo1.place(x=150, y=370)
   
    def crear_usuario():
        nombre = entry1.get()
        password = entry_password.get()
        matricula = entry2.get()
        rol = combo1.get()
        if nombre and password and matricula and rol:
            insertar_usuario(nombre, password, matricula, rol)
            messagebox.showinfo(message="Usuario creado con éxito", title="Éxito")
            ventana_Usuario1.destroy()
        else:
            messagebox.showerror(message="Faltan campos", title="Error")

    # Botón Guardar
    btn_guardar = tk.Button(ventana_Usuario1, text="Guardar", command=crear_usuario)
    btn_guardar.place(x=350, y=490)

    labeltitulo = ttk.Label(ventana_Usuario1, text="Carrera",  background="#0b3473", font=("Arial", 20), foreground="White")
    labeltitulo.place(x= 340, y=80)

    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_Usuario1.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_Usuario1.resizable(False, False)  # Deshabilitar el cambiventana_tecnica
    ventana_Usuario1.mainloop()


def mostrar_ventana_observacion():
    ventana_obser1= tk.Toplevel()
    ventana_obser1.title("Observacion")
    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="img/1.png")

    # Crear un Label con la imagen de fondo y colocarlo en la ventana
    label_fondo = tk.Label(ventana_obser1, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)


    #Mas Labels
    label_Origen = tk.Label(ventana_obser1, text="Origen de Muestra:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Origen.place(x=150, y=110)

    label_Muestra = tk.Label(ventana_obser1, text="Tipo de Muestra:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Muestra.place(x=150, y=170)

    label_Especie = tk.Label(ventana_obser1, text="Especie:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Especie.place(x=450, y=170)

    label_Laminilla = tk.Label(ventana_obser1, text="Laminilla:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Laminilla.place(x=150, y=240)

    label_Coordenada = tk.Label(ventana_obser1, text="Coordenada:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Coordenada.place(x=450, y=230)

    label_Tecnica = tk.Label(ventana_obser1, text="Tecnica:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Tecnica.place(x=150, y=310)

    label_Tincion = tk.Label(ventana_obser1, text="Tincion:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Tincion.place(x=330, y=310)

    label_Aumento = tk.Label(ventana_obser1, text="Aumento:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_Aumento.place(x=490, y=310)

    label_numeroimg = tk.Label(ventana_obser1, text="Numero de Imagen:", background="#0b3473", font=("Arial", 16), foreground="White")
    label_numeroimg.place(x=150, y=390)

    # Campos de entrada
    entry_Origen = tk.Entry(ventana_obser1)
    entry_Origen.place(x=150, y=140)

    entry_Muestra = tk.Entry(ventana_obser1)
    entry_Muestra.place(x=150, y=200)

    entry_Especie = tk.Entry(ventana_obser1)
    entry_Especie.place(x=450, y=200)


    entry_Coordenada = tk.Entry(ventana_obser1)
    entry_Coordenada.place(x=450, y=270)

    entry_aumento = tk.Entry(ventana_obser1)
    entry_aumento.place(x=490, y=350)

    entry_numeroimg = tk.Entry(ventana_obser1)
    entry_numeroimg.place(x=150, y=420)

    tipomuestra = consultar_tipomuestra()
    laminilla = consultar_laminillas()
    tecnica = consultar_tecnicas()
    tincion = consultar_tinciones()

    combo1 = ttk.Combobox(ventana_obser1, values=tipomuestra, width=30)
    combo1.place(x=150, y=200)

    combo2 = ttk.Combobox(ventana_obser1, values=laminilla, width=30)
    combo2.place(x=150, y=270)

    combo3 = ttk.Combobox(ventana_obser1, values=tecnica, width=16)
    combo3.place(x=150, y=340)

    combo4 = ttk.Combobox(ventana_obser1, values=tincion, width=16)
    combo4.place(x=330, y=340)

    def crear_observacion():
        origen = entry_Origen.get()
        muestra = entry_Muestra.get()
        especie = entry_Especie.get()
        coordenada = entry_Coordenada.get()
        tecnica = combo3.get()
        tincion = combo4.get()
        aumento = entry_aumento.get()
        numeroimg = entry_numeroimg.get()
        if origen and muestra and especie and coordenada and tecnica and tincion and aumento and numeroimg:
            insertar_observacion(origen, muestra, especie, coordenada, tecnica, tincion, aumento, numeroimg)
            messagebox.showinfo(message="Observación creada con éxito", title="Éxito")
            ventana_obser1.destroy()
        else:
            messagebox.showerror(message="Faltan campos", title="Error")
    # Botón Guardar
    btn_guardar = tk.Button(ventana_obser1, text="Guardar" , command=crear_observacion)
    btn_guardar.place(x=350, y=490)
    
    # Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
    ventana_obser1.geometry("800x600")  # Establecer las dimensiones deseadas
    ventana_obser1.resizable(False, False)  # Deshabilitar el cambiventana_tecnica
    ventana_obser1.mainloop()






































# Crear la ventana principal de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Microdex")

# Cargar la imagen de fondo
imagen_fondo = Image.open("img/FondoLogin.png")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu propia imagen
imagen_fondo = imagen_fondo.resize((800, 600))  # Ajusta el tamaño de la imagen según tus necesidades
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget Label para mostrar la imagen de fondo
label_fondo = tk.Label(ventana_login, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

label_usuario = tk.Label(ventana_login, text="Matricula", font=("Arial", 18), background="#083c71", foreground="White" )
entry_usuario = tk.Entry(ventana_login, width=20, font=("Arial", 12))   

label_contrasena = tk.Label(ventana_login, text="Contraseña", background="#083c71", font=("Arial", 18), foreground="White")
entry_contrasena = tk.Entry(ventana_login, show="*", width=20, font=("Arial", 12))

btn_olvidarcontra = tk.Button(ventana_login, text="¿Olvidaste tu contraseña?", background="#083c71", font=("Arial", 10), foreground="White", command=mostrar_ventana_olvidaste_contrasena) #Otra funcion

btn_login = tk.Button(ventana_login, text="Iniciar sesión", background="#fbbe05", font=("Arial", 10), foreground="White", command=iniciar_sesion)
btn_registrar = tk.Button(ventana_login, text="Resgistrarse", background="#fbbe05", font=("Arial",10), foreground="White", command=mostrar_ventana_registro) #Aqui va otra funcion


# Colocar los widgets de usuario y contraseña sobre la imagen de fondo
label_usuario.place(x=30, y=180)
entry_usuario.place(x=30, y=220)
label_contrasena.place(x=30, y=270)
entry_contrasena.place(x=30, y=310)
btn_login.place(x=30, y=390)
btn_registrar.place(x=120, y=390)
btn_olvidarcontra.place(x= 35, y=350)

# Establecer dimensiones y deshabilitar la posibilidad de cambiar el tamaño de la ventana
ventana_login.geometry("800x600")  # Establecer las dimensiones deseadas
ventana_login.resizable(False, False)  # Deshabilitar el cambio de tamaño

ventana_login.mainloop()