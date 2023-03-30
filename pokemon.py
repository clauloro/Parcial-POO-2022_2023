from enum import Enum

class Arma(Enum):
    PUÑO = 1
    PATADA = 2
    CODAZO = 3
    CABEZAZO = 4


class Pokemon():
    ids_list =[]

    def __init__(self, id_pokemon, nombre, tipo_arma, puntos_salud, indice_ataque, indice_defensa):
        self.__id_pokemon = id_pokemon
        self.__nombre = nombre
        self.__tipo_arma = tipo_arma
        self.__puntos_salud = puntos_salud
        self.__indice_ataque = indice_ataque
        self.__indice_defensa = indice_defensa 

        if id_pokemon in Pokemon.lista_ids:
            raise ValueError("El ID del pokemon ya existe.")
        else:
            Pokemon.lista_ids.append(id_pokemon)
        if not (1<= puntos_salud <= 100):
            raise ValueError("Los puntos de salud deben estar entre 1 y 100.")
        if not (1<= indice_ataque <= 10):
            raise ValueError("El índice de ataque debe estar entre 1 y 10.")
        if not (1<= indice_defensa <= 10):
            raise ValueError("El índice de defensa debe estar entre 1 y 10.")

def __del__(self):
    Pokemon.lista_ids.remove(self.__id_pokemon)

def __str__(self):
    tipo_arma_nombre = self.__tipo_arma.name
    return f"El pokemon con ID {self.__id_pokemon}, nombre {self.__nombre}, arma {tipo_arma_nombre} y {self.__puntos_salud} puntos de salud."

def get_id_pokemon(self):
    return self.__id_pokemon

def get_nombre(self):
    return self.__nombre

def get_tipo_arma(self):
    return self.__tipo_arma

def get_indice_ataque(self):
    return self.__indice_ataque

def get_indice_defensa(self):
    return self.__indice_defensa

def set_puntos_salud(self, nuevos_puntos_salud):
    if not (1<= nuevos_puntos_salud <= 100):
        raise ValueError("Los puntos de salud deben estar entre 1 y 100.")
    self.__puntos_salud = nuevos_puntos_salud

def esta_vivo(self):
    return self.__puntos_salud > 0

def atacar(self, pokemon_a_atacar):
    puntos_ataque = self.__indice_ataque
    return pokemon_a_atacar.defenderse(puntos_ataque)

def defenderse(self, puntos_de_daño):
    puntos_defensa = self.__indice_defensa
    if puntos_defensa > puntos_de_daño:
        return False
    else: 
        daño = puntos_de_daño - puntos_defensa 
        nuevos_puntos_salud = self.__puntos_salud - daño
        if nuevos_puntos_salud < 0:
            self.__puntos_salud = 0
        else:
            self.__puntos_salud = nuevos_puntos_salud
        return True




def main():
#probar la clase
    pokemon1 = Pokemon(1, 'Bulbasaur', Arma.PUÑO, 90,7,5)
    pokemon2 = Pokemon(2, 'Charmander', Arma.PATADA, 80,8,4)
    print(pokemon1)
    print(pokemon2)
    pokemon1.atacar(pokemon2)
    print(pokemon2)
    pokemon2.atacar(pokemon1)
    print(pokemon1)


main()
