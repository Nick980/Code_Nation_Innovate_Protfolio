# dict_of_films = {
#     "Sicario":2008,
#     "Arrival":2011,
#     "Dune":2020,
#     "Enemy":2019    
# }

# will_dict = {
#     "tired": True,
#     "hungry": False,
#     "exercise_time_day": 20,
#     "homework": "look at PEP 0484",
#     "chores": "clean kitchen"
# }

# will_dict

#Activity 1

# pet_dictionary = {
#     "cat1": {
#         "name": "Merlin",
#         "color": "Black",
#         "nickname": "Murderer",
#         "fav_food": "Chicken",
#         "meow_sound": "meow"
#         },
#     "cat2": {
#         "name": "Milo",
#         "color": "Black",
#         "nickname": "The Blob",
#         "fav_food": "EVERYTHING",
#         "meow_sound": "meeeh"
#         },
#     "dog1": {
#         "name": "Alfie",
#         "color": "Brown/White",
#         "nickname": "Fluff",
#         "fav_food": "Chicken",
#         "woof_sound": "Woof"
#         },
#     }

# print(pet_dictionary["cat1"]["fav_food"])

# del pet_dictionary["cat1"]["fav_food"]

# pet_dictionary["cat1"]["fav_food"] = "Mouse"

# print(pet_dictionary["cat1"]["fav_food"])

#Activity 2

country_dict = {
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome"
}

country_dict.setdefault("Ireland", "Dublin")
country_dict.setdefault("Ukraine", "Kyiv")

for i, value in country_dict.items():
    print(i, ' : ', value)