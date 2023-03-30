import pandas as pd

def presentacion():
    print("Estos son los dos entrenadores que se enfrentarán:")
    # Presentamos los pokemones de los dos entrenadores
    datos1 = pd.read_csv('1_coach.csv')
    print("----------------------------------------datos del coach 1---------------------------")
    print(datos1)

    datos2 = pd.read_csv('2_coach.csv')
    print("----------------------------------------datos del coach 2---------------------------")
    print(datos2)


# Ahora vamos a guardar los datos de los pokemones en una lista

# COACH 1
with open('1_coach.csv', 'r') as file:
    datos = csv.reader(file)
    datos_coach1 = [tuple(pokemon) for pokemon in datos][1:]

pokemon1_coach1 = datos_coach1[0]
pokemon2_coach1 = datos_coach1[1]
pokemon3_coach1 = datos_coach1[2]


# COACH 2
with open('2_coach.csv', 'r') as file:
    datos = csv.reader(file)
    datos_coach2 = [tuple(pokemon) for pokemon in datos][1:]

pokemon1_coach2 = datos_coach2[0]
pokemon2_coach2 = datos_coach2[1]
pokemon3_coach2 = datos_coach2[2]







