import random

pokeneas = [
    {
        "id": 1,
        "nombre": "Flogón",
        "altura": "1.2 m",
        "habilidad": "Fuego",
        "imagen": "https://storage.cloud.google.com/pokeneas-imagenes_2/fuego.png",
        "frase": "Siempre adelante, nunca retroceder."
    },
    {
        "id": 2,
        "nombre": "Aquareon",
        "altura": "0.8 m",
        "habilidad": "Agua",
        "imagen": "https://storage.cloud.google.com/pokeneas-imagenes_2/aguaa.jfif",
        "frase": "El agua calma hasta el fuego más intenso."
    },
    {
        "id": 3,
        "nombre": "Ventisca",
        "altura": "1.5 m",
        "habilidad": "Viento",
        "imagen": "https://storage.cloud.google.com/pokeneas-imagenes_2/viento.jfif",
        "frase": "El viento nunca se detiene, aprende de él."
    },
    {
        "id": 4,
        "nombre": "Rocatus",
        "altura": "0.9 m",
        "habilidad": "Roca",
        "imagen": "https://storage.cloud.google.com/pokeneas-imagenes_2/roca.jfif",
        "frase": "La fortaleza está en la base."
    },
    {
        "id": 5,
        "nombre": "Electrion",
        "altura": "1.1 m",
        "habilidad": "Eléctrico",
        "imagen": "https://storage.cloud.google.com/pokeneas-imagenes_2/electrico.jfif",
        "frase": "La chispa más pequeña puede encender un gran fuego."
    },
    {
        "id": 6,
        "nombre": "Glacialis",
        "altura": "0.7 m",
        "habilidad": "Hielo",
        "imagen": "https://storage.cloud.google.com/pokeneas-imagenes_2/hielo.jfif",
        "frase": "La calma del hielo derrota la prisa."
    },
    {
        "id": 7,
        "nombre": "Umbrión",
        "altura": "1.4 m",
        "habilidad": "Oscuridad",
        "imagen": "https://storage.cloud.google.com/pokeneas-imagenes_2/oscuridad.jfif",
        "frase": "En la oscuridad, siempre hay una chispa de luz."
    }
]

def obtener_pokenea_aleatorio():
    return random.choice(pokeneas)
