import mysql.connector

def conectar():
  try:
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="ventas_2025"
    )
    print("Conexión exitosa a la base de datos.")
    return db
  except mysql.connector.Error as e:
    print(e)
    return None

def ejecutar_consulta(conexion, consulta):
  if conexion is None:
    return None

  try:
    mycursor = conexion.cursor()
    mycursor.execute(consulta)
    resultados = mycursor.fetchall()
    return resultados
  except mysql.connector.Error as err:
    print(f"Error al ejecutar la consulta: {err}")
    return None

def cerrar_conexion(conexion):
  if conexion:
    conexion.close()
    print("Conexión cerrada.")



if conexion:
  consulta = "SELECT * FROM clientes"  # Reemplaza 'clientes' con tu tabla
  resultados = ejecutar_consulta(conexion, consulta)

  if resultados:
    for fila in resultados:
      print(fila)

  cerrar_conexion(conexion)
  
conexion = conectar()
def menu(conexion):
    print("---GESTION CLIENTES---")
    print("1. crear clientes")
    print("2. ver clientes")
    print("3. actualizar clientes")
    print("4. eliminar clientes")
    print("5. salir")
    while True:
        opcion = int(input("Ingresa la opcion: "))
        match opcion:
          case 1:
            consulta = ""
            pass
          case 2:
            consulta = "SELECT FOR "
            pass
          case 3:
            consulta = ""
            pass
          case 4:
            consulta = ""
            pass
          case 5:
            break
          
menu(conexion)
