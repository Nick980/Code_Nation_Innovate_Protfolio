#Activity 1
welcome = "Welcome to Code Nation"
text_length = len(welcome)

def welcome_check():
    if text_length%2==0:
        print(f"The legnth of the sentence < {welcome} > is {text_length} characters and this is an even number")
    else:
        print(f"The legnth of the sentence < {welcome} > is {text_length} characters and this is an odd number")

welcome_check()


#Activity 2
# import string
# alphabet_string = string.ascii_uppercase
# alphabet_list = list(alphabet_string)

# for i in alphabet_list:
#     print(i, end='  ')
# print("\n")

# def letter_num():
#     user_num = input("Please enter a number 1 to 26 to see its corrosponding letter:>   ")
#     user_num = int(user_num)
#     user_num -=1
#     if user_num >=0 and user_num <=26:
#         print(alphabet_list[user_num])
#     else:
#         print("Invalid entry, please try again")
#         letter_num()

# letter_num()

# #Activity 3
# space1 = "1"
# space2 = "2"
# space3 = "3"
# space4 = "4"
# space5 = "5"
# space6 = "6"
# space7 = "7"
# space8 = "8"
# space9 = "9"

# def drawgrid():
#     print(f"""
#     {space1}   |   {space2}   |   {space3}
# ------------------------
#     {space4}   |   {space5}   |   {space6}
# ------------------------
#     {space7}   |   {space8}   |   {space9}
# """)


# spaces_remaining = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# player_1_token = None
# player_2_token = None
# computer_token = None
# current_player = None
# player_move = None


# def opponent_select():
#     p2_cpu_or_real = input("Do you want to play against the <computer> or another <player> :>      ")
#     if p2_cpu_or_real == "computer":
#         player2 = "computer"
#     elif p2_cpu_or_real == "player":
#         player2 = "player"
#     else:
#         print("Invalid entry, please type computer or player")
#         opponent_select()

# def token_select():
#     player_token = input("Player 1, which token would you like to use, X or O:>     ")
#     player_token = player_token.upper()
#     if player_token == "X" or player_token == "O":
#         player_1_token = player_token
#     else:
#         print('Invalid entry, please type "X" or "O"')
#         token_select()

# def player_1_turn():
#     player_1_move = input("Player 1 please select an available slot:>       ")
#     if player_1_move in spaces_remaining:
#         player_1_move = int(player_1_move)
#         player_1_move +=1
#         space[player_1_move] = player_1_token
#     else:
#         print("Invalid entry, please select an available slot")
#         player_1_turn()

# print(spaces_remaining[5])

# # opponent_select()
# # print(player_2)
# # token_select()
# # print(player_1_token)
# # drawgrid()
# # player_1_turn()
