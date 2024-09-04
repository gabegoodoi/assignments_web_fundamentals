'''
Task 2: Fetching Data from the Pokémon API

1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).

2. Extract and print the name and abilities of the Pokémon.

Expected Outcome: The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

Task 3: Analyzing and Displaying Data

1. Modify the script to fetch data for three different Pokémon.

2. Create a function to calculate and return the average weight of these Pokémon.

3. Print the names, abilities, and average weight of the three Pokémon. **Code Example:**

def fetch_pokemon_data(pokemon_name):
    return #json response

def calculate_average_weight(pokemon_list):
    return #average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
Expected Outcome: The script should display the names and abilities of the three chosen Pokémon and their average weight. The function should correctly calculate and return the average weight based on the data fetched from the API. 
'''

import requests

def average_weight(sum_weight, pokemon_names):
    print(f"\nAverage weight of {pokemon_names[0]}, {pokemon_names[1]}, & {pokemon_names[2]}: {round((sum_weight/len(pokemon_names)), 1)} units\n")


def whose_that_pokemon():
    pokemon = []
    pokemon_names = []
    sum_weight = 0
    while len(pokemon) < 3:
        pokemon.append(input("Search pokem by name or number: ").lower())

    for i in range(len(pokemon)):
        poke_api = f"https://pokeapi.co/api/v2/pokemon/{pokemon[i]}"
        response = requests.get(poke_api)
        pokemon_json = response.json()

        name = pokemon_json.get("name")
        pokemon_names.append(name.title())
        abilities = pokemon_json.get("abilities")
        print(f"\nName: {name.title()}\nAbilities:")
        for item in abilities:
            print(f"- {item['ability']['name'].title()}")
    
        sum_weight += pokemon_json.get("weight")

    return sum_weight, pokemon_names    


# sum_weight, pokemon_names = whose_that_pokemon()

# average_weight(sum_weight, pokemon_names)