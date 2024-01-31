import time

class LectorParpadeos:
    @staticmethod
    def detectar_parpadeo():
        tiempo_simulacion = 10  # Simular durante los primeros 10 segundos

        for _ in range(tiempo_simulacion):
            time.sleep(1)  # Esperar 1 segundo
            print("Esperando para simular parpadeos...")

        # Simular parpadeo rápido después de los 10 segundos
        print("¡Parpadeo rápido!")
        return "¡Parpadeo rápido!"
