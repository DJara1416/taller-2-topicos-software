import random

pokeneas = [
    {
        "id": 1,
        "nombre": "Flogón",
        "altura": "1.2 m",
        "habilidad": "Fuego",
        "imagen": "https://storage.googleapis.com/pokeneas-imagenes/flogon.png",
        "frase": "Siempre adelante, nunca retroceder."
    },
    {
        "id": 2,
        "nombre": "Aquareon",
        "altura": "0.8 m",
        "habilidad": "Agua",
        "imagen": "https://storage.googleapis.com/pokeneas-imagenes/aquareon.png",
        "frase": "El agua calma hasta el fuego más intenso."
    },
    {
        "id": 3,
        "nombre": "Ventisca",
        "altura": "1.5 m",
        "habilidad": "Viento",
        "imagen": "https://storage.googleapis.com/pokeneas-imagenes/ventisca.png",
        "frase": "El viento nunca se detiene, aprende de él."
    },
    {
        "id": 4,
        "nombre": "Rocatus",
        "altura": "0.9 m",
        "habilidad": "Roca",
        "imagen": "https://storage.googleapis.com/pokeneas-imagenes/rocatus.png",
        "frase": "La fortaleza está en la base."
    },
    {
        "id": 5,
        "nombre": "Electrion",
        "altura": "1.1 m",
        "habilidad": "Eléctrico",
        "imagen": "https://storage.googleapis.com/pokeneas-imagenes/electrion.png",
        "frase": "La chispa más pequeña puede encender un gran fuego."
    },
    {
        "id": 6,
        "nombre": "Glacialis",
        "altura": "0.7 m",
        "habilidad": "Hielo",
        "imagen": "https://storage.googleapis.com/pokeneas-imagenes/glacialis.png",
        "frase": "La calma del hielo derrota la prisa."
    },
    {
        "id": 7,
        "nombre": "Umbrión",
        "altura": "1.4 m",
        "habilidad": "Oscuridad",
        "imagen": "https://storage.googleapis.com/pokeneas-imagenes/umbrion.png",
        "frase": "En la oscuridad, siempre hay una chispa de luz."
    }
]

def obtener_pokenea_aleatorio():
    return random.choice(pokeneas)
