import random
from pokemon import *


class PokemonAgua(Pokemon):
    
    def __init__(self, nombre, ataque):
        super().__init__(nombre, "Agua", 100, ataque, 10)
    