from enum import Enum

class Weapon(Enum):
    PUNCH = 1
    KICK = 2
    ELBOW = 3
    HEADBUTT = 4


class Pokemon():
    ids_list =[]

    def __init__(self, pokemon_id, name, weapon_type, health_points, attack_index, defense_index):
        self.__pokemon_id = pokemon_id
        self.__name = name
        self.__weapon_type = weapon_type
        self.__health_points = health_points
        self.__attack_index = attack_index
        self.__defense_index = defense_index 

        if pokemon_id in Pokemon.ids_list:
            raise ValueError("pokemon ID already exists.")
        else:
            Pokemon.ids_list.append(pokemon_id)
        if not (1<= health_points <= 100):
            raise ValueError(" Health points should be between 1 and 100.")
        if not (1<= attack_index <= 10):
            raise ValueError("Attack index should be between 1 and 10")
        if not (1<= defense_index <= 10):
            raise ValueError("Defense index should be between 1 and 10.")
    def __del__(self):
        Pokemon.ids_list.remove(self.__pokemon_id)
    
    def __str__(self):
        weapon_name = self.__weapon_type.name
        return f"Pokemon ID {self.__pokemon_id} with name {self.__name} has as weapon {weapon_name} and health {self.__health_points}."
    
    def get_pokemon_id(self):
        return self.__pokemon_id
    
    def get_name(self):
        return self.__name
    
    def get_weapon_type(self):
        return self.__weapon_type
    
    def get_attack_index(self):
        return self.__attack_index
    
    def get_defense_index(self):
        return self.__defense_index
    
    def set_health_points(self, new_health_points):
        if not (1<= new_health_points <= 100):
            raise ValueError("Health points should be  between 1 and 100.")
        self.__health_points = new_health_points
    
    def is_alive(self):
        return self.__health_points > 0
    
    def fight_attack(self, pokemon_to_attack):
        attack_points = self.__attack_index
        return pokemon_to_attack.fight_defense(attack_points)
    
    def fight_defense(self, points_of_damage):
        defense_points = self.__defense_index
        if defense_points > points_of_damage:
            return False
        else: 
            damage = points_of_damage - defense_points 
            new_health_points = self.__health_points - damage
            if new_health_points < 0:
                self.__health_points = 0
            else:
                self.__health_points = new_health_points
            return True



def main():
#probar la clase
    pokemon1 = Pokemon(1, 'Bulbasaur', Weapon.PUNCH, 90,7,5)
    pokemon2 = Pokemon(2, 'Charmander', Weapon.KICK, 80,8,4)
    print(pokemon1)
    print(pokemon2)
    pokemon1.fight_attack(pokemon2)
    print(pokemon2)
    pokemon2.fight_attack(pokemon1)
    print(pokemon1)


main()
