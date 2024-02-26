import os

def crear_carpetas_y_ficheros():
    for i in range(1, 6):
        carpeta = f'folder{i}'
        os.makedirs(carpeta, exist_ok=True)

        for j in range(1, 11):
            nombre_fichero = f'{carpeta}/fichero{j}.txt'
            contenido = f'Este es el contenido del fichero {j}\n'

            with open(nombre_fichero, 'w') as archivo:
                archivo.write(contenido)

if __name__ == "__main__":
    for _ in range(5):
        crear_carpetas_y_ficheros()

