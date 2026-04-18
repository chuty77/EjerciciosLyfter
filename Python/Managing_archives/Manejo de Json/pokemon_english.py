import json



poke_file= "pokemons.json"

pokemons= [
    {
        "name": {"english": "Pikachu"},
        "level": 25,
        "type": ["Electric"],
        "base": {
            "HP": 35, "Attack": 55, "Defense": 40,
            "Sp. Attack": 50, "Sp. Defense": 50, "Speed": 90
        }
    },
    {
        "name": {"english": "Charmander"},
        "level": 15,
        "type": ["Fire"],
        "base": {
            "HP": 39, "Attack": 52, "Defense": 43,
            "Sp. Attack": 60, "Sp. Defense": 50, "Speed": 65
        }
    },
    {
        "name": {"english": "Squirtle"},
        "level": 18,
        "type": ["Water"],
        "base": {
            "HP": 44, "Attack": 48, "Defense": 65,
            "Sp. Attack": 50, "Sp. Defense": 64, "Speed": 43
        }
    },
    {
        "name": {"english": "Snorlax"},
        "level": 200,
        "type": ["Water"],
        "base": {
            "HP": 100, "Attack": 60, "Defense": 55,
            "Sp. Attack": 50, "Sp. Defense": 64, "Speed": 45
        }
    }
]

#1 Read the file

with open(poke_file,'w',encoding='utf-8')as f:
    json.dump(pokemons,f,indent=4)
    print(f"The archive {poke_file} has been saved")


#2 Load the file
with open(poke_file,'r',encoding='utf-8')as f:
 data= json.load(f)
print(f"Data was loaded with {len(data)} pokemons")


#3 Write new data
print("-----------Enter the new pokemon----------------")

name= input("Name:")
level= int(input("Level:"))
type= input("Type, example (Electric,Fire,Water): ")


#3 Add stats
hp= int(input("HP: "))
Attack = int(input("Attack: "))
Defense = int(input("Defense: "))
Sp_Attack  = int(input("Sp. Attack: "))
Sp_Defense = int(input("Sp. Defense: "))
Speed = int(input("Speed: "))


new_pokemon = {
   "name": {"english": name},
        "level": level,
        "type": [type],
        "base": {
            "HP": hp, "Attack": Attack, "Defense": Defense,
            "Sp. Attack": Sp_Attack, "Sp. Defense": Sp_Defense, "Speed": Speed}
}


#4 Add the new pokemon
data.append(new_pokemon)
with open(poke_file,'w',encoding='utf-8')as f:
   json.dump(data,f,indent=4)
   print(f"The new pokemon called {name} was added to the json file and we have now {len(data)}")

