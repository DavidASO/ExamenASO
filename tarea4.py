import logging
import psutil
import os

logger = None

def configurar_logger():
    global logger
    logger = logging.getLogger("espacio_logger")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    directorio_logs = f'/home/{os.getlogin()}/logs'
    os.makedirs(directorio_logs, exist_ok=True)
    archivo_log = os.path.join(directorio_logs, 'espacio.log')
    file_handler = logging.FileHandler(archivo_log)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

def analizar_espacio(particion="/"):
    global logger
    espacio = psutil.disk_usage(particion)
    porcentaje_uso = espacio.percent

    if porcentaje_uso > 80:
        logger.error(f"Espacio ocupado en '{particion}' es mayor que 80%: {porcentaje_uso}%")
    elif porcentaje_uso > 60:
        logger.warning(f"Espacio ocupado en '{particion}' es mayor que 60% y menor que 80%: {porcentaje_uso}%")
    else:
        logger.info(f"Espacio ocupado en '{particion}' es mayor que 0% y menor que 60%: {porcentaje_uso}%")

def ejecutar_tarea():
    directorio_logs = f'/home/{os.getlogin()}/logs'
    os.makedirs(directorio_logs, exist_ok=True)

    configurar_logger()

    analizar_espacio("/")
