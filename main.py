import random

class Pokemon:

    def __init__(self, name, elemental_type, level, power):
        self.name = name
        self.elemental_type = elemental_type
        self.level = level
        self.power = power
        self.current_health = level * 10

    def attack(self, pokemon):
        print("{} attacks {}...".format(self.name, pokemon.name))
        pokemon.defend(self.power)

    def defend(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        print("{} receives {} damage points.".format(self.name, damage))
        if self.current_health == 0:
            print("{} has been defeated.".format(self.name))

    def is_undefeated(self):
        return self.current_health > 0


class Coach:
    def __init__(self, name, pokemons):
        self.name = name
        self.pokemons = pokemons
        self.selected_pokemon = None

    def select_pokemon(self):
        
        if not self.pokemons:
            print(f"{self.name}, you have no Pokemons left!")
            return

        print(f"{self.name}, select a Pokemon:")
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i + 1}. {pokemon.name} (HP: {pokemon.current_hp}/{pokemon.hp})")

        selected_pokemon = None
        while not selected_pokemon:
            try:
                choice = int(input("Enter the number of the Pokemon: "))
                if not 1 <= choice <= len(self.pokemons):
                    raise ValueError
                selected_pokemon = self.pokemons[choice - 1]
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid number.")

        self.selected_pokemon = selected_pokemon
        print(f"{self.name} selected {self.selected_pokemon.name}!")
