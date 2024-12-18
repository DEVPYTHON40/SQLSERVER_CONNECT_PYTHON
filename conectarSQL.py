import pyodbc  # Importa pyodbc para manejar la conexión y consultas con SQL Server
import tkinter as tk  # Importa Tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa messagebox para mostrar mensajes emergentes (errores o confirmaciones)

# Configuración de la conexión a SQL Server
server = 'DESKTOP-1O6VQNV'  # Nombre del servidor de SQL Server (ajústalo según tu configuración)
database = 'CentroMedico'   # Nombre de la base de datos que usarás en SQL Server

# Función para enviar datos a la tabla Medico
def enviar_datos():
    nombre = entry_nombre.get()  # Captura el valor ingresado en el campo 'Nombre'
    apellido = entry_apellido.get()  # Captura el valor ingresado en el campo 'Apellido'

    # Validar que los campos no estén vacíos
    if not nombre or not apellido:
        messagebox.showerror("Error", "Tdos los campos son obligatorios.")  # Muestra un error si algún campo está vacío
        return

    try:
        # Conexión a SQL Server
        connection = pyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"  # Conexión con autenticación integrada
        )
        cursor = connection.cursor()  # Crea un cursor para ejecutar consultas SQL

        # Insertar datos en la tabla Medico usando parámetros
        query = "INSERT INTO Medico (Nombre, Apellido) VALUES (?, ?)"  # Sentencia SQL parametrizada
        cursor.execute(query, (nombre, apellido))  # Ejecuta la consulta con los datos del formulario
        connection.commit()  # Confirma los cambios en la base de datos

        # Mostrar mensaje de éxito al usuario
        messagebox.showinfo("Éxito", "Datos enviados correctamente.")

        # Limpiar los campos del formulario
        entry_nombre.delete(0, tk.END)  # Borra el campo de nombre
        entry_apellido.delete(0, tk.END)  # Borra el campo de apellido

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

    except pyodbc.Error as e:  # Captura errores durante la conexión o ejecución
        messagebox.showerror("Error", f"Error al conectar o insertar datos: {e}")  # Muestra el error al usuario

# Función para consultar y mostrar los datos de la tabla Medico
def mostrar_datos():
    try:
        # Conexión a SQL Server
        connection = pyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"  # Conexión con autenticación integrada
        )
        cursor = connection.cursor()  # Crea un cursor para ejecutar consultas SQL

        # Consulta para obtener todos los datos de la tabla Medico
        query = "SELECT * FROM Medico"  # Sentencia SQL para obtener todos los registros
        cursor.execute(query)  # Ejecuta la consulta
        rows = cursor.fetchall()  # Recupera todos los resultados

        # Mostrar resultados en la consola
        print("Datos de la tabla Medico:")  # Encabezado
        for row in rows:  # Itera por cada fila obtenida
            print(row)  # Imprime la fila completa

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

    except pyodbc.Error as e:  # Captura errores durante la conexión o consulta
        print("Error al consultar los datos:", e)  # Imprime el error en la consola

# Función para actualizar datos de la tabla Medico
def actualizar_datos():
    id_medico = entry_id.get()  # Captura el valor ingresado en el campo 'ID'
    nombre = entry_nombre.get()  # Captura el valor ingresado en el campo 'Nombre'
    apellido = entry_apellido.get()  # Captura el valor ingresado en el campo 'Apellido'

    # Validar que los campos no estén vacíos
    if not id_medico or not nombre or not apellido:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")  # Muestra un error si algún campo está vacío
        return

    try:
        # Conexión a SQL Server
        connection = pyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"  # Conexión con autenticación integrada
        )
        cursor = connection.cursor()  # Crea un cursor para ejecutar consultas SQL

        # Sentencia SQL para actualizar los datos de un médico por su ID
        query = "UPDATE Medico SET Nombre = ?, Apellido = ? WHERE idMedico = ?"  # Sentencia SQL para actualizar
        cursor.execute(query, (nombre, apellido, id_medico))  # Ejecuta la consulta con los datos del formulario
        connection.commit()  # Confirma los cambios en la base de datos

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Datos actualizados correctamente.")

        # Limpiar los campos del formulario
        entry_id.delete(0, tk.END)  # Borra el campo de ID
        entry_nombre.delete(0, tk.END)  # Borra el campo de nombre
        entry_apellido.delete(0, tk.END)  # Borra el campo de apellido

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

    except pyodbc.Error as e:  # Captura errores durante la conexión o ejecución
        messagebox.showerror("Error", f"Error al conectar o actualizar datos: {e}")  # Muestra el error al usuario

# Función para eliminar datos de la tabla Medico
def eliminar_datos():
    id_medico = entry_id.get()  # Captura el valor ingresado en el campo 'ID'

    # Validar que el campo no esté vacío
    if not id_medico:
        messagebox.showerror("Error", "El campo 'ID' es obligatorio.")  # Muestra un error si el campo está vacío
        return

    try:
        # Conexión a SQL Server
        connection = pyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"  # Conexión con autenticación integrada
        )
        cursor = connection.cursor()  # Crea un cursor para ejecutar consultas SQL

        # Sentencia SQL para eliminar un médico por su ID
        query = "DELETE FROM Medico WHERE idMedico = ?"  # Sentencia SQL para eliminar
        cursor.execute(query, (id_medico,))  # Ejecuta la consulta con el ID del médico
        connection.commit()  # Confirma los cambios en la base de datos

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Datos eliminados correctamente.")

        # Limpiar los campos del formulario
        entry_id.delete(0, tk.END)  # Borra el campo de ID
        entry_nombre.delete(0, tk.END)  # Borra el campo de nombre
        entry_apellido.delete(0, tk.END)  # Borra el campo de apellido

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

    except pyodbc.Error as e:  # Captura errores durante la conexión o ejecución
        messagebox.showerror("Error", f"Error al conectar o eliminar datos: {e}")  # Muestra el error al usuario

# Crear la interfaz gráfica
root = tk.Tk()  # Crea una ventana principal con Tkinter
root.title("Formulario CRUD Medico")  # Título de la ventana
root.geometry("400x400")  # Define el tamaño de la ventana

# Etiqueta y campo para el ID del Médico
label_id = tk.Label(root, text="ID del Médico:")
label_id.pack(pady=5)
entry_id = tk.Entry(root, width=30)  # Campo para ingresar el ID
entry_id.pack(pady=5)

# Etiqueta y campo para el nombre
label_nombre = tk.Label(root, text="Nombre del Médico:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root, width=30)  # Campo para ingresar el nombre
entry_nombre.pack(pady=5)

# Etiqueta y campo para el apellido
label_apellido = tk.Label(root, text="Apellido del Médico:")
label_apellido.pack(pady=5)
entry_apellido = tk.Entry(root, width=30)  # Campo para ingresar el apellido
entry_apellido.pack(pady=5)

# Botón para enviar datos
btn_enviar = tk.Button(root, text="Enviar Datos", command=enviar_datos, width=20, height=2)
btn_enviar.pack(pady=10)

# Botón para mostrar datos en consola
btn_mostrar = tk.Button(root, text="Mostrar Datos en Consola", command=mostrar_datos, width=20, height=2)
btn_mostrar.pack(pady=10)

# Botón para eliminar datos
btn_eliminar = tk.Button(root, text="Eliminar Datos", command=eliminar_datos, width=20, height=2)
btn_eliminar.pack(pady=10)

# Botón para actualizar datos
btn_actualizar = tk.Button(root, text="Actualizar Datos", command=actualizar_datos, width=20, height=2)
btn_actualizar.pack(pady=10)

# Iniciar la aplicación
root.mainloop()  # Inicia el bucle principal de la interfaz gráfica
