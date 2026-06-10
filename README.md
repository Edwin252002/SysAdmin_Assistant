
# 🖥️ SysAdmin Assistant

Este proyecto es una herramienta de administración de sistemas automatizada que ofrece dos interfaces de usuario: una versión visual e interactiva construida con **CustomTkinter** (`app.py`) y una versión ligera para la terminal de comandos (`main.py`). Permite monitorear recursos de hardware, gestionar procesos y automatizar tareas comunes de archivos.

## Arquitectura del Proyecto

El proyecto está diseñado para ser flexible, ofreciendo dos puntos de acceso independientes según las necesidades del usuario:

* **Interfaz Gráfica (`app.py`)**: Utiliza programación dirigida por eventos con hilos (`threading`) para evitar que la interfaz visual se congele al realizar tareas pesadas de monitoreo de hardware.
* **Interfaz de Consola (`main.py`)**: Estructura basada en un bucle de control directo en terminal, ideal para entornos de servidores o accesos rápidos vía SSH donde no se dispone de un entorno gráfico.
* **Módulos del Sistema**: Ambas versiones consumen las API del sistema operativo a través de `psutil` y librerías nativas para interactuar con el almacenamiento, memoria y procesador de forma segura.

---

## Tecnologías Utilizadas

* **Librerías Visuales:** CustomTkinter (Interfaz de usuario moderna en modo oscuro).
* **Monitoreo de Sistema:** `psutil` (Estadísticas de CPU, memoria RAM y procesos activos).
* **Gestión de Archivos:** `shutil`, `os` y `pathlib` (Automatización de backups y ordenamiento de directorios).
* **Core de Python:** `platform`, `socket` y `getpass` (Recolección de metadatos del entorno y red local).

---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
https://github.com/Edwin252002/SysAdmin_Assistant.git
```
### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```
---
## Ejecucion
```
python app.py
```
---
## Funcionaldades Principales
| Componente / Función | Entrada Requerida | Descripción |
| --- | --- | --- |
| **Información del Sistema** | Ninguna | Muestra metadatos del equipo, sistema operativo, IP local y estado de RAM/Disco. |
| **Monitor de Procesos** | Ninguna | Lista los procesos activos del sistema detallando su PID, nombre y consumo de recursos. |
| **Organizar Archivos** | Ruta de carpeta destino | Clasifica automáticamente archivos sueltos en carpetas según su extensión (PDF, WORD, IMÁGENES, etc.). |
| **Copia de Seguridad** | Carpeta origen y destino | Duplica de forma segura el contenido de un directorio origen hacia una ruta de respaldo. |
| **Generar Reporte** | Ninguna | Exporta un informe detallado con el estado del hardware y la lista de procesos a un archivo `.txt`. |
---

## Estructura de Archivos
.  
├── app.py              # Aplicación con interfaz gráfica (CustomTkinter).  
├── main.py             # Aplicación para consola/terminal clásica.  
├── requirements.txt    # Dependencias de librerías externas requeridas.  
└── Reporte_Sistema.txt # Reporte plano generado por las funciones de auditoría.  
