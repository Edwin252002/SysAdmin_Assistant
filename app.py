
import customtkinter as ctk
from tkinter import messagebox, filedialog
import platform, getpass, socket, psutil, shutil
import os
from pathlib import Path
from datetime import datetime
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
import threading
import time

app=ctk.CTk()
app.title("SYSADMIN ASSISTANT")
app.geometry("700x500")

title=ctk.CTkLabel(app,text="SYSADMIN ASSISTANT",font=("Arial",30,"bold"))
title.pack(pady=20)

def sistema():
    mem=psutil.virtual_memory()
    disk=shutil.disk_usage("/")
    try:
        ip=socket.gethostbyname(socket.gethostname())
    except:
        ip="No disponible"
    txt=f"""Equipo: {platform.node()}
Usuario: {getpass.getuser()}
Sistema: {platform.system()}
Versión: {platform.version()}
Arquitectura: {platform.machine()}
IP: {ip}
CPU: {psutil.cpu_percent(interval=1)} %
RAM Total: {round(mem.total/1024**3,2)} GB
RAM Libre: {round(mem.available/1024**3,2)} GB
Disco Libre: {round(disk.free/1024**3,2)} GB"""
    messagebox.showinfo("Información del Sistema",txt)

def procesos():

    texto = ""

    texto += "{:<10}{:<35}{:<10}{:<10}\n".format(
        "PID",
        "NOMBRE",
        "CPU%",
        "RAM%"
    )

    texto += "-"*70 + "\n"

    contador = 0

    for p in psutil.process_iter(
        ['pid','name','cpu_percent','memory_percent']
    ):

        try:

            texto += "{:<10}{:<35}{:<10}{:<10}\n".format(

                p.info['pid'],

                str(p.info['name'])[:30],

                p.info['cpu_percent'],

                round(
                    p.info['memory_percent'],
                    2
                )

            )

            contador += 1

            if contador >= 40:
                break

        except:
            pass

    messagebox.showinfo(
        "Monitor de Procesos",
        texto
    )

def organizar():

    carpeta = filedialog.askdirectory(
        title="Seleccione una carpeta"
    )

    if carpeta == "":
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
        ".gif":"IMAGENES",
        ".mp4":"VIDEOS",
        ".avi":"VIDEOS",
        ".mkv":"VIDEOS"

    }

    cantidad = 0

    for archivo in os.listdir(carpeta):

        ruta = os.path.join(carpeta, archivo)

        if os.path.isfile(ruta):

            extension = Path(archivo).suffix.lower()

            destino = categorias.get(extension, "OTROS")

            carpeta_destino = os.path.join(
                carpeta,
                destino
            )

            os.makedirs(
                carpeta_destino,
                exist_ok=True
            )

            shutil.move(
                ruta,
                os.path.join(
                    carpeta_destino,
                    archivo
                )
            )

            cantidad += 1

    messagebox.showinfo(
        "Proceso terminado",
        f"Se organizaron {cantidad} archivos correctamente."
    )

def backup():

    origen = filedialog.askdirectory(
        title="Seleccione la carpeta origen"
    )

    if origen == "":
        return

    destino = filedialog.askdirectory(
        title="Seleccione la carpeta destino"
    )

    if destino == "":
        return

    cantidad = 0

    for archivo in os.listdir(origen):

        ruta = os.path.join(origen, archivo)

        if os.path.isfile(ruta):

            try:

                shutil.copy2(
                    ruta,
                    os.path.join(destino, archivo)
                )

                cantidad += 1

            except:
                pass

    messagebox.showinfo(
        "Copia de Seguridad",
        f"Se copiaron {cantidad} archivos correctamente."
    )

def reporte():

    memoria = psutil.virtual_memory()

    archivo = "Reporte_Sistema.txt"

    with open(archivo, "w", encoding="utf-8") as f:
        fecha = datetime.now()

        f.write(f"Fecha: {fecha.strftime('%d/%m/%Y')}\n")
        f.write(f"Hora: {fecha.strftime('%H:%M:%S')}\n\n")

        f.write("=====================================\n")
        f.write("      SYSADMIN ASSISTANT\n")
        f.write("=====================================\n\n")

        f.write(f"Equipo: {platform.node()}\n")
        f.write(f"Usuario: {getpass.getuser()}\n")
        f.write(f"Sistema: {platform.system()}\n")
        f.write(f"Versión: {platform.version()}\n")
        f.write(f"Arquitectura: {platform.machine()}\n")

        try:
            ip = socket.gethostbyname(socket.gethostname())
        except:
            ip = "No disponible"

        f.write(f"IP: {ip}\n")
        f.write(f"CPU: {psutil.cpu_percent(interval=1)} %\n")
        f.write(f"RAM Total: {round(memoria.total/1024**3,2)} GB\n")
        f.write(f"RAM Libre: {round(memoria.available/1024**3,2)} GB\n\n")

        f.write("=========== PROCESOS ===========\n\n")

        for p in psutil.process_iter(['pid','name']):

            try:
                f.write(f"{p.info['pid']} - {p.info['name']}\n")
            except:
                pass

    messagebox.showinfo(
        "Reporte",
        "Reporte generado correctamente.\n\nSe guardó como:\nReporte_Sistema.txt"
    )
for text,cmd in [
    ("Información del Sistema",sistema),
    ("Monitor de Procesos",procesos),
    ("Organizar Archivos",organizar),
    ("Copia de Seguridad",backup),
    ("Generar Reporte",reporte),
]:
    ctk.CTkButton(app,text=text,width=300,height=40,command=cmd).pack(pady=10)

ctk.CTkButton(app,text="Salir",width=300,height=40,fg_color="red",command=app.destroy).pack(pady=20)

app.mainloop()
