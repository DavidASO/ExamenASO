import psutil

def obtener_porcentaje_uso(particion):
    try:
        espacio = psutil.disk_usage(particion)
        porcentaje_uso = espacio.percent
        return porcentaje_uso
    except Exception as e:
        return str(e)

def mostrar_porcentajes():
    particiones = ["/dev/sda1", "/dev/sdb1"]
    for particion in particiones:
        porcentaje = obtener_porcentaje_uso(particion)
        if isinstance(porcentaje, (float, int)):
            print(f"{particion} {porcentaje:.1f}%")
        else:
            print(f"{particion} Error: {porcentaje}")

if __name__ == "__main__":
    mostrar_porcentajes()
