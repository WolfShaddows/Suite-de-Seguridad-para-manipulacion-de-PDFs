# main_app.py
from encriptador import Encriptador
from buscador_pdfs import BuscadorPDFs
from lector_gestos import LectorGestos
from lector_parpadeos import LectorParpadeos

def main():
    # Ejemplo de uso de la Suite de Herramientas de Seguridad
    mensaje_original = "Hola, esto es un mensaje secreto"

    # Encriptación
    encriptador = Encriptador()
    mensaje_encriptado, clave_secreta = encriptador.encriptar(mensaje_original)
    print(f"Mensaje Encriptado: {mensaje_encriptado}")

    # Desencriptación
    mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado, clave_secreta)
    print(f"Mensaje Desencriptado: {mensaje_desencriptado}")

    # Búsqueda en PDF
    archivo_pdf = 'hydro trad.pdf'
    # Reemplaza con tu PDF
    palabra_a_buscar = 'hidrógeno'
    buscador = BuscadorPDFs()
    coincidencias = buscador.buscar_palabra(archivo_pdf, palabra_a_buscar)
    print("Coincidencias en el PDF:")
    for coincidencia in coincidencias:
        print(coincidencia)

    # Detección de Gestos
    gesto_detectado = LectorGestos.detectar_gesto()
    print(gesto_detectado)

    # Detección de Parpadeos
    parpadeo_detectado = LectorParpadeos.detectar_parpadeo()
    print(parpadeo_detectado)

if __name__ == "__main__":
    main()
