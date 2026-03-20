import json

data= [
  {
    "name": {
      "english": "Pikachu"
    },
    "level": 25,
    "type": [
      "Electric"
    ],
    "base": {
      "HP": 35,
      "Attack": 55,
      "Defense": 40,
      "Sp. Attack": 50,
      "Sp. Defense": 50,
      "Speed": 90
    }
  },
  {
    "name": {
      "english": "Charmander"
    },
    "level": 15,
    "type": [
      "Fire"
    ],
    "base": {
      "HP": 39,
      "Attack": 52,
      "Defense": 43,
      "Sp. Attack": 60,
      "Sp. Defense": 50,
      "Speed": 65
    }
  },
  {
    "name": {
      "english": "Squirtle"
    },
    "level": 18,
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
  },
{
    "name": {
      "english": "Snorlax"
    },
    "level": 200,
    "type": [
      "Water"
    ],
    "base": {
      "HP": 100,
      "Attack": 60,
      "Defense": 55,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 45
    }
  }
]



def import_pokemon(data,input_file):
    with open(input_file,'w') as file:
       json.dump(data,file, indent=4)
       print(f"Archivo {input_file} creado correctamente")


# def leer_json(nombre_archivo):
#     try:
#         with open(nombre_archivo, 'r', encoding='utf-8') as f:
#             datos = json.load(f)
#             return datos
#     except FileNotFoundError:
#         return "Archivo no encontrado"
            
import_pokemon(data,'pokemon.json')


