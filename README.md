La función principal de herramientas como el buscador en el PDF y los demás métodos en la suite de seguridad es proporcionar al usuario la capacidad de realizar operaciones específicas sin revelar información sensible a otras personas. Aquí hay una breve descripción de cada una de estas funciones:

### Buscador en el PDF (BuscadorPDFs):

Permite al usuario buscar una palabra específica dentro de un documento PDF.
La búsqueda se realiza sin revelar la palabra clave o el contenido del PDF a otras personas que puedan estar observando.

### Lector de Gestos (LectorGestos):

Detecta gestos realizados por el usuario, como un saludo o cualquier gesto personalizado que haya sido implementado.
Puede utilizarse para la interacción del usuario sin revelar la información específica sobre el gesto realizado.

### Lector de Parpadeos (LectorParpadeos):

Detecta patrones de parpadeo del usuario.
Puede utilizarse para proporcionar una forma de interacción sin revelar detalles específicos sobre el patrón de parpadeo.

### Encriptador (Encriptador):

Proporciona funciones de encriptación y desencriptación para mensajes.
La encriptación se realiza de manera que solo el usuario que conoce la clave secreta puede desencriptar el mensaje.
Estas herramientas están diseñadas para brindar privacidad y seguridad al usuario, permitiéndole realizar ciertas operaciones sin divulgar información sensible a terceros. La idea es que el usuario tenga el control y la conciencia de sus acciones sin comprometer la seguridad de sus datos.

El lector de gestos y el lector de parpadeo son simulados para mostrar la idea , un ejemplo para implementar esos programas seria el siguiente:

```python
import cv2
import mediapipe as mp
import dlib

# Inicializar el módulo de MediaPipe para el seguimiento de gestos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inicializar el detector de parpadeos de dlib
detector_parapdeos = dlib.get_frontal_face_detector()
predictor_parapdeos = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a escala de grises para el detector de parpadeos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar parpadeos usando dlib
    faces = detector_parapdeos(gray)
    for face in faces:
        landmarks = predictor_parapdeos(gray, face)
        left_eye_ratio = ...
        right_eye_ratio = ...
        # Calcular la relación de apertura de los ojos y determinar si parpadean

    # Detectar gestos de la mano usando MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Realizar acciones basadas en la posición de los landmarks de la mano
            # Ejemplo: Identificar gestos como abrir/cerrar la mano, etc.

    # Mostrar el resultado
    cv2.imshow("Lector de Gestos y Parpadeos", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Presionar la tecla 'Esc' para salir
        break

cap.release()
cv2.destroyAllWindows()

```
Obviamente para quien quiera probarlo debe instalar las siguientes dependencias:

`pip install mediapipe dlib`

Continuando con el programa simulando estas cuestiones, la salida seria la siguiente en un lapso de 1 minuto:

    Mensaje Encriptado: b'gAAAAABluZ_jqpp6NHj7wl8_ugVWhU4me9GrfuMNJud_Wyx-m5TEy3bryRbAf1beH9bjIuWFV9CSvensV5KBdXRJFW7Upd-BB_xbyUeYYXUODNU52g-0k7A31an_exdV-5Fk-wrSUhrH'
    Mensaje Desencriptado: Hola, esto es un mensaje secreto
    Coincidencias en el PDF:
    Coincidencia en la página 1
    Coincidencia en la página 2
    Coincidencia en la página 3
    Coincidencia en la página 4
    Coincidencia en la página 5
    Coincidencia en la página 6
    Coincidencia en la página 7
    Coincidencia en la página 8
    Coincidencia en la página 9
    Coincidencia en la página 10
    Coincidencia en la página 11
    Coincidencia en la página 12
    Coincidencia en la página 13
    Coincidencia en la página 14
    Coincidencia en la página 15
    Coincidencia en la página 16
    Coincidencia en la página 17
    Coincidencia en la página 18
    Coincidencia en la página 19
    Coincidencia en la página 20
    Coincidencia en la página 21
    Coincidencia en la página 22
    Coincidencia en la página 23
    Coincidencia en la página 24
    Coincidencia en la página 25
    Coincidencia en la página 26
    Coincidencia en la página 27
    Coincidencia en la página 28
    Coincidencia en la página 29
    Coincidencia en la página 30
    Coincidencia en la página 31
    Coincidencia en la página 32
    Coincidencia en la página 33
    Coincidencia en la página 34
    Coincidencia en la página 35
    Coincidencia en la página 36
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    Esperando para simular gestos...
    ¡Hola!
    ¡Hola!
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    Esperando para simular parpadeos...
    ¡Parpadeo rápido!
    ¡Parpadeo rápido!


------------

### fin...
