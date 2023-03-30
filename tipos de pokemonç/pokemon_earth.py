import random
from pokemon import *

class PokemonTierra(Pokemon):
    
    def __init__(self, nombre, defensa):
        super().__init__(nombre, "Tierra", 100, 10, defensa)
        
