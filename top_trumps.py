import random
import requests
from pprint import pprint
from datetime import datetime


# 1. Generate a random number between 1 and 151 to use as the Pokemon ID number
# 2. Using the Pokemon API get a Pokemon based on its ID number
# 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight
def get_stats_of_random_pokemon():
    random_id = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_id)
    pokemon_data = requests.get(url).json()
    pokemon_stats = {
        "id": pokemon_data["id"],
        "name": pokemon_data["name"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"],
        "order": pokemon_data["order"],
        "base_experience": pokemon_data["base_experience"]
    }
    return pokemon_stats

print(get_stats_of_random_pokemon())


# 4. Get a random Pokemon for the player and another for their opponent
# 5. Ask the user which stat they want to use (id, height or weight)
# 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

def selection_of_pokemon_and_compare_stats():
    player_pokemon = get_stats_of_random_pokemon()
    opponent_pokemon = get_stats_of_random_pokemon()
    print("You were given {} pokemon".format(player_pokemon["name"]))
    print("Opponent were given {} pokemon".format(opponent_pokemon["name"]))
    stat = input("Which stat do you want to use? (id, height, weight, order, base_experience)")
    player_pokemon_stat = player_pokemon[stat]
    opponent_pokemon_stat = opponent_pokemon[stat]
    if player_pokemon_stat > opponent_pokemon_stat:
        print("Player won")
    elif player_pokemon_stat < opponent_pokemon_stat:
        print("Opponent won")
    else:
        print("Match Draw")
    input("Required task finish here, Press Enter to continue")

selection_of_pokemon_and_compare_stats()

def play_rounds():
    player_winning_count = 0
    opponent_winning_count = 0
    list_of_stats = ["id", "name", "height", "weight", "order", "base_experience"]
    rounds = int(input("How many rounds you want to play?"))
    for each in range(rounds):
        player_pokemon_stats1 = get_stats_of_random_pokemon()
        player_pokemon_stats2 = get_stats_of_random_pokemon()
        player_pokemon_stats3 = get_stats_of_random_pokemon()
        player_pokemon_lists = [player_pokemon_stats1["name"], player_pokemon_stats2["name"], player_pokemon_stats3["name"]]
        pokemon_choice = input("Please select pokemon from the list: {}".format(player_pokemon_lists))
        print("You have selected {} pokemon".format(pokemon_choice))
        opponent_pokemon_stats = get_stats_of_random_pokemon()
        print("Opponent has selected {} pokemon".format(opponent_pokemon_stats["name"]))
        print("If even number comes then player can decide stat and if odd number comes then opponent can decide stat.")
        input("Press Enter to continue")
        random_number = random.randint(1, 10)
        if random_number % 2 == 0:
            stat = input("We got Even number, please enter which stat do you want to use? (id, height, weight, order, base_experience)")
        else:
            stat = random.choice(list_of_stats)
            print("We got Odd number, Opponent has chose {} stat".format(stat))
        player_pokemon_stats = None
        if player_pokemon_stats1["name"] == pokemon_choice:
            player_pokemon_stats = player_pokemon_stats1
        elif player_pokemon_stats2["name"] == pokemon_choice:
            player_pokemon_stats = player_pokemon_stats2
        elif player_pokemon_stats3["name"] == pokemon_choice:
            player_pokemon_stats = player_pokemon_stats3
        else:
            pass
        if player_pokemon_stats[stat] > opponent_pokemon_stats[stat]:
            player_winning_count = player_winning_count + 1
            print("-" * 100)
            print("Player won this round")
            print("-" * 100)
        elif player_pokemon_stats[stat] < opponent_pokemon_stats[stat]:
            opponent_winning_count = opponent_winning_count + 1
            print("-" * 100)
            print("Opponent won this round")
            print("-" * 100)
        else:
            print("-" * 100)
            print("Both stats are same, this round is draw")
            print("-" * 100)
    if player_winning_count > opponent_winning_count:
        result = "Player won the game with {} rounds out of {} rounds".format(player_winning_count, rounds).upper()
        print(result)
    elif player_winning_count < opponent_winning_count:
        result = "Opponent won the game with {} rounds out of {} rounds".format(opponent_winning_count, rounds).upper()
        print(result)
    else:
        result = "Match draw as Player won {} rounds and Opponent won {} rounds".format(player_winning_count, opponent_winning_count).upper()
        print(result)
    return result


#print(play_rounds())

def play_round_and_store_result_into_file():
    now = datetime.now()
    current_time = now.strftime("%d-%m-%y %H:%M:%S")
    game_result = play_rounds()
    with open("game_result.txt", "a") as txt_file:
        txt_file.write(str(current_time))
        txt_file.write("\t")
        txt_file.write(game_result)
        txt_file.write("\n")

play_round_and_store_result_into_file()

