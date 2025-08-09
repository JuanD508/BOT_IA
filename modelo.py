from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import random

def detect_dog(img):
    np.set_printoptions(suppress=True)

    # Carga del modelo y etiquetas
    model = load_model("/content/keras_model.h5", compile=False)
    class_names = open("/content/labels.txt").readlines()

    # Preprocesamiento de la imagen
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(img).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    clase = class_name[2:].strip()

    # Datos curiosos por especie
    datos_curiosos = {
        "Pastor alemán": [
            "un perro cariñoso con la familia y fácil de entrenar."
        ],
        "Bulldog": [
            "conocido por su apariencia robusta, su personalidad amigable y su lealtad"
        ],
        "Golden retriever": [
            "conocido por su inteligencia, lealtad y naturaleza amigable.",
            "excelente perro de terapia y servicio."
        ],
        "Husky siberiano": [
            "famoso por su resistencia, belleza y personalidad amigable.",
            "conocido por su capacidad para correr largas distancias, su pelaje resistente al frío, y sus ojos azules o de distintos colores."
        ],
        "Beagle":[
            "conocido por su agudo sentido del olfato, su energía y su naturaleza sociable.",
            "un perro de caza por excelencia, y su capacidad para rastrear es legendaria."
        ],
        "Poodle":[
             "originario de Alemania y no de Francia, como muchos creen.",
             "conocidos como Caniches en algunas partes."
        ],
        "Chihuahua ":[
            "famoso por ser la raza de perro más pequeña del mundo y por su gran personalidad.",
            "conocido por ser leal, valient y tener un fuerte apego a sus dueños."
        ],
        "Dachshund":[
            "mayor conocido como el perro salchicha.",
            "conocido por su cuerpo alargado y patas cortas, y fueron criados originalmente para cazar tejones."
        ],
        "Border collie":[
            "conocido por su alta inteligencia y energía, siendo una de las razas más inteligentes.",
            "pastor por naturaleza, pero también se destacan en deportes como el agility y el rescate.",
            "habilidoso para aprender y obedecer órdenes."
        ],
        "Boyero de Berna":[
            "un perro grande, robusto y hermoso.",
            "conocido por su carácter dulce y cariñoso, especialmente con los niños.",
            "leal, paciente y disfruta de la compañía de su familia."
        ]
    }

    # Mostrar resultado
    if confidence_score >= 0.70:
      print("Este perro es un:", clase)
      print("Estamos seguros un:", confidence_score * 100, "%")
      if clase in datos_curiosos:
        dato = random.choice(datos_curiosos[clase])
        print("Este perro es", dato)
      else:
          print("No hay datos curiosos disponibles para esta raza.")
    else:
      print("Cremos que tu perro es criollo")
