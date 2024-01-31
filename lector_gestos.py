import time

class LectorGestos:
    @staticmethod
    def detectar_gesto():
        tiempo_simulacion = 10  # Simular durante los primeros 10 segundos

        for _ in range(tiempo_simulacion):
            time.sleep(1)  # Esperar 1 segundo
            print("Esperando para simular gestos...")

        # Simular gesto después de los 10 segundos
        print("¡Hola!")
        return "¡Hola!"
