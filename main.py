from art import logo
from art import vs
import random
from game_data import data
from os import system

score = 0

game_on = True
while game_on:
    system("clear")

    first_dictionary = {}
    second_dictionary = {}
    first_comparison = ''
    second_comparison = ''
    first_description = ''
    second_description = ''
    first_location = ''
    second_location = ''
    first_follower_count = 0
    second_follower_count = 0

    for key in data[random.randint(0, len(data) - 1)]:

        first_dictionary = data[random.randint(0, len(data)) - 1]
        first_comparison = first_dictionary["name"]
        first_description = first_dictionary["description"]
        first_location = first_dictionary["country"]
        first_follower_count = first_dictionary["follower_count"]

        second_dictionary = data[random.randint(0, len(data)) - 1]
        second_comparison = second_dictionary["name"]
        second_description = second_dictionary["description"]
        second_location = second_dictionary["country"]
        second_follower_count = second_dictionary["follower_count"]

        if second_comparison == first_comparison:
            second_dictionary = data[random.randint(0, len(data))]

    print(logo)
    print(f"Compare A: {first_comparison}, a {first_description}, from {first_location}.")
    print(vs)
    print(f"Against B: {second_comparison}, a {second_description}, from {second_location}.")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if first_follower_count > second_follower_count and user_guess == 'A':
        score += 1
        print(f"You're right! Current score: {score}")
    elif first_follower_count < second_follower_count and user_guess == 'B':
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry that's wrong. Final score {score}")
        game_on = False
        system("clear")
