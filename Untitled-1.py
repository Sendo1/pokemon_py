import random
class pokemonx:
    pokemon = "Pokemon"
    
    def __init__(self, nombre, daño, HP, velocidad):      #sumar caracteristicas
        self.nombre = nombre 
        self.daño = daño
        self.HP = HP
        self.velocidad = velocidad
        
    def atacar(self, enemigo):
        if self.HP<= 0:
            print(f"""{self.nombre} no tiene suficiente vitalidad para atacar.
                ...""")
            return
        elif enemigo.HP <=0:
            print(f"{enemigo.nombre} esta debilitado y no puede seguir en combate")
            return
        else:
            enemigo.HP -= self.daño
            print(f"{enemigo.nombre} ha sufrido daño... su vida actual es de {enemigo.HP}...")
        print("...")
    def huir(self):
        print(f"{self.nombre} ha huido con exito!!")
pokemones = {
    1: {"nombre": "Bulbasaur", "tipo": ["Planta", "Veneno"], "estadisticas": {"HP": 45, "Ataque": 49, "Defensa": 49, "Ataque Especial": 65, "Defensa Especial": 65, "Velocidad": 45}},
    2: {"nombre": "Ivysaur", "tipo": ["Planta", "Veneno"], "estadisticas": {"HP": 60, "Ataque": 62, "Defensa": 63, "Ataque Especial": 80, "Defensa Especial": 80, "Velocidad": 60}},
    3: {"nombre": "Venusaur", "tipo": ["Planta", "Veneno"], "estadisticas": {"HP": 80, "Ataque": 82, "Defensa": 83, "Ataque Especial": 100, "Defensa Especial": 100, "Velocidad": 80}},
    4: {"nombre": "Charmander", "tipo": ["Fuego"], "estadisticas": {"HP": 39, "Ataque": 52, "Defensa": 43, "Ataque Especial": 60, "Defensa Especial": 50, "Velocidad": 65}},
    5: {"nombre": "Charmeleon", "tipo": ["Fuego"], "estadisticas": {"HP": 58, "Ataque": 64, "Defensa": 58, "Ataque Especial": 80, "Defensa Especial": 65, "Velocidad": 80}},
    6: {"nombre": "Charizard", "tipo": ["Fuego", "Volador"], "estadisticas": {"HP": 78, "Ataque": 84, "Defensa": 78, "Ataque Especial": 109, "Defensa Especial": 85, "Velocidad": 100}},
    7: {"nombre": "Squirtle", "tipo": ["Agua"], "estadisticas": {"HP": 44, "Ataque": 48, "Defensa": 65, "Ataque Especial": 50, "Defensa Especial": 64, "Velocidad": 43}},
    8: {"nombre": "Wartortle", "tipo": ["Agua"], "estadisticas": {"HP": 59, "Ataque": 63, "Defensa": 80, "Ataque Especial": 65, "Defensa Especial": 80, "Velocidad": 58}},
    9: {"nombre": "Blastoise", "tipo": ["Agua"], "estadisticas": {"HP": 79, "Ataque": 83, "Defensa": 100, "Ataque Especial": 85, "Defensa Especial": 105, "Velocidad": 78}},
    10: {"nombre": "Caterpie", "tipo": ["Bicho"], "estadisticas": {"HP": 45, "Ataque": 30, "Defensa": 35, "Ataque Especial": 20, "Defensa Especial": 20, "Velocidad": 45}},
    11: {"nombre": "Metapod", "tipo": ["Bicho"], "estadisticas": {"HP": 50, "Ataque": 20, "Defensa": 55, "Ataque Especial": 25, "Defensa Especial": 25, "Velocidad": 30}},
    12: {"nombre": "Butterfree", "tipo": ["Bicho", "Volador"], "estadisticas": {"HP": 60, "Ataque": 45, "Defensa": 50, "Ataque Especial": 90, "Defensa Especial": 80, "Velocidad": 70}},
    13: {"nombre": "Weedle", "tipo": ["Bicho", "Veneno"], "estadisticas": {"HP": 40, "Ataque": 35, "Defensa": 30, "Ataque Especial": 20, "Defensa Especial": 20, "Velocidad": 50}},
    14: {"nombre": "Kakuna", "tipo": ["Bicho", "Veneno"], "estadisticas": {"HP": 45, "Ataque": 25, "Defensa": 50, "Ataque Especial": 25, "Defensa Especial": 25, "Velocidad": 35}},
    15: {"nombre": "Beedrill", "tipo": ["Bicho", "Veneno"], "estadisticas": {"HP": 65, "Ataque": 90, "Defensa": 40, "Ataque Especial": 45, "Defensa Especial": 80, "Velocidad": 75}},
    16: {"nombre": "Pidgey", "tipo": ["Normal", "Volador"], "estadisticas": {"HP": 40, "Ataque": 45, "Defensa": 40, "Ataque Especial": 35, "Defensa Especial": 35, "Velocidad": 56}},
    17: {"nombre": "Pidgeotto", "tipo": ["Normal", "Volador"], "estadisticas": {"HP": 63, "Ataque": 60, "Defensa": 55, "Ataque Especial": 50, "Defensa Especial": 50, "Velocidad": 71}},
    18: {"nombre": "Pidgeot", "tipo": ["Normal", "Volador"], "estadisticas": {"HP": 83, "Ataque": 80, "Defensa": 75, "Ataque Especial": 70, "Defensa Especial": 70, "Velocidad": 101}},
    19: {"nombre": "Rattata", "tipo": ["Normal"], "estadisticas": {"HP": 30, "Ataque": 56, "Defensa": 35, "Ataque Especial": 25, "Defensa Especial": 35, "Velocidad": 72}},
    20: {"nombre": "Raticate", "tipo": ["Normal"], "estadisticas": {"HP": 55, "Ataque": 81, "Defensa": 60, "Ataque Especial": 50, "Defensa Especial": 70, "Velocidad": 97}},
    21: {"nombre": "Spearow", "tipo": ["Normal", "Volador"], "estadisticas": {"HP": 40, "Ataque": 60, "Defensa": 30, "Ataque Especial": 31, "Defensa Especial": 31, "Velocidad": 70}},
    22: {"nombre": "Fearow", "tipo": ["Normal", "Volador"], "estadisticas": {"HP": 65, "Ataque": 90, "Defensa": 65, "Ataque Especial": 61, "Defensa Especial": 61, "Velocidad": 100}},
    23: {"nombre": "Ekans", "tipo": ["Veneno"], "estadisticas": {"HP": 35, "Ataque": 60, "Defensa": 44, "Ataque Especial": 40, "Defensa Especial": 54, "Velocidad": 55}},
    24: {"nombre": "Arbok", "tipo": ["Veneno"], "estadisticas": {"HP": 60, "Ataque": 95, "Defensa": 69, "Ataque Especial": 65, "Defensa Especial": 79, "Velocidad": 80}},
    25: {"nombre": "Pikachu", "tipo": ["Eléctrico"], "estadisticas": {"HP": 35, "Ataque": 55, "Defensa": 40, "Ataque Especial": 50, "Defensa Especial": 50, "Velocidad": 90}},
    26: {"nombre": "Raichu", "tipo": ["Eléctrico"], "estadisticas": {"HP": 60, "Ataque": 90, "Defensa": 55, "Ataque Especial": 90, "Defensa Especial": 80, "Velocidad": 110}},
    27: {"nombre": "Sandshrew", "tipo": ["Tierra"], "estadisticas": {"HP": 50, "Ataque": 75, "Defensa": 85, "Ataque Especial": 20, "Defensa Especial": 30, "Velocidad": 40}},
    28: {"nombre": "Sandslash", "tipo": ["Tierra"], "estadisticas": {"HP": 75, "Ataque": 100, "Defensa": 110, "Ataque Especial": 45, "Defensa Especial": 55, "Velocidad": 65}},
    29: {"nombre": "Nidoran♀", "tipo": ["Veneno"], "estadisticas": {"HP": 55, "Ataque": 47, "Defensa": 52, "Ataque Especial": 40, "Defensa Especial": 40, "Velocidad": 41}},
    30: {"nombre": "Nidorina", "tipo": ["Veneno"], "estadisticas": {"HP": 70, "Ataque": 62, "Defensa": 67, "Ataque Especial": 55, "Defensa Especial": 55, "Velocidad": 56}}
}

pokemon_del_jugador = random.choice(list(pokemones.values()))
pokemon_enemigo = random.choice(list(pokemones.values()))

while True:
    if pokemon_del_jugador == pokemon_enemigo:
        pokemon_del_jugador = random.choice(list(pokemones.values()))
    else:
        break

print(f"Tu pokemon incial es {pokemon_del_jugador["nombre"]} y te tocara pelear contra {pokemon_enemigo["nombre"]} ")


#hacer un def con la accion de pegar, y que lleve a los ataques del pokemon se impriman las opciones y que el usuario tenga un input para elegir el ataque...



