import os
import platform
import socket
import getpass
import shutil
import psutil
from pathlib import Path
from datetime import datetime

def info_sistema():

    print("\n========== INFORMACIÓN DEL SISTEMA ==========\n")

    print("Equipo:", platform.node())
    print("Usuario:", getpass.getuser())
    print("Sistema Operativo:", platform.system())
    print("Versión:", platform.version())
    print("Arquitectura:", platform.machine())

    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = "No disponible"

    print("IP:", ip)

    memoria = psutil.virtual_memory()

    print("\n------ MEMORIA ------")
    print(f"RAM Total: {round(memoria.total/1024**3,2)} GB")
    print(f"RAM Usada: {round(memoria.used/1024**3,2)} GB")
    print(f"RAM Libre: {round(memoria.available/1024**3,2)} GB")

    print("\n------ CPU ------")
    print("Uso CPU:", psutil.cpu_percent(interval=1), "%")

    disco = shutil.disk_usage("/")

    print("\n------ DISCO ------")
    print(f"Total: {round(disco.total/1024**3,2)} GB")
    print(f"Usado: {round(disco.used/1024**3,2)} GB")
    print(f"Libre: {round(disco.free/1024**3,2)} GB")


def procesos():

    print("\n========== PROCESOS ==========\n")

    print("{:<8}{:<35}{:<10}".format("PID","NOMBRE","RAM %"))

    for p in psutil.process_iter(['pid','name','memory_percent']):

        try:
            print("{:<8}{:<35}{:<10.2f}".format(
                p.info['pid'],
                str(p.info['name'])[:30],
                p.info['memory_percent']
            ))

        except:
            pass


def organizar():

    carpeta = input("\nRuta de la carpeta:\n")

    if not os.path.exists(carpeta):
        print("Carpeta no existe")
        return

    categorias = {
        ".pdf":"PDF",
        ".doc":"WORD",
        ".docx":"WORD",
        ".xls":"EXCEL",
        ".xlsx":"EXCEL",
        ".jpg":"IMAGENES",
        ".jpeg":"IMAGENES",
        ".png":"IMAGENES",
        ".mp4":"VIDEOS",
        ".avi":"VIDEOS"
    }

    for archivo in os.listdir(carpeta):

        ruta = os.path.join(carpeta,archivo)

        if os.path.isfile(ruta):

            ext = Path(archivo).suffix.lower()

            destino = categorias.get(ext,"OTROS")

            nueva = os.path.join(carpeta,destino)

            os.makedirs(nueva,exist_ok=True)

            shutil.move(ruta,os.path.join(nueva,archivo))

    print("\nArchivos organizados correctamente.")


def backup():

    origen = input("\nCarpeta origen:\n")
    destino = input("Carpeta destino:\n")

    if not os.path.exists(origen):
        print("Origen inválido")
        return

    os.makedirs(destino,exist_ok=True)

    total = 0

    for archivo in os.listdir(origen):

        ruta = os.path.join(origen,archivo)

        if os.path.isfile(ruta):

            shutil.copy2(ruta,destino)
            total += 1

    ahora = datetime.now()

    print("\nBackup realizado")
    print("Fecha:",ahora.strftime("%d/%m/%Y"))
    print("Hora:",ahora.strftime("%H:%M:%S"))
    print("Archivos copiados:",total)


def reporte():

    memoria = psutil.virtual_memory()

    archivo = "reporte.txt"

    with open(archivo,"w",encoding="utf8") as f:

        f.write("REPORTE DEL SISTEMA\n")
        f.write("====================\n\n")

        f.write(f"Equipo: {platform.node()}\n")
        f.write(f"Usuario: {getpass.getuser()}\n")
        f.write(f"Sistema: {platform.system()}\n")
        f.write(f"Version: {platform.version()}\n")
        f.write(f"CPU: {psutil.cpu_percent()} %\n")
        f.write(f"RAM Total: {round(memoria.total/1024**3,2)} GB\n")
        f.write(f"RAM Libre: {round(memoria.available/1024**3,2)} GB\n")
        f.write("\nProcesos:\n\n")

        for p in psutil.process_iter(['pid','name']):

            try:
                f.write(f"{p.info['pid']} - {p.info['name']}\n")
            except:
                pass

    print("\nReporte generado:",archivo)


while True:

    print("""
==============================
SYSADMIN ASSISTANT
==============================

1. Información del sistema

2. Monitor de procesos

3. Organizar archivos

4. Copia de seguridad

5. Generar reporte

6. Salir

""")

    op = input("Seleccione una opción: ")

    if op == "1":
        info_sistema()

    elif op == "2":
        procesos()

    elif op == "3":
        organizar()

    elif op == "4":
        backup()

    elif op == "5":
        reporte()

    elif op == "6":
        print("Hasta luego")
        break

    else:
        print("Opción inválida")