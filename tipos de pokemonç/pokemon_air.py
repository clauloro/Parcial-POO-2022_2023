import random
from pokemon import *


        
class PokemonAire(Pokemon):
    
    def __init__(self, nombre, defensa):
        super().__init__(nombre, "Aire", 100, 10, defensa)
        
    def fight(self, pokemon_rival):
        if random.randint(1, 100) <= 50:
            print("El ataque de {} no afectó a {}.".format(self.nombre, pokemon_rival.nombre))
            return
        if self.tipo == "Aire" and pokemon_rival.tipo == "Agua":
            pokemon_rival.vida -= self.ataque * 2 - pokemon_rival.defensa
        else:
            pokemon_rival.vida -= self.ataque - pokemon_rival.defensa
    
