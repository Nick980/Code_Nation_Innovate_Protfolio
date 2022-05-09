#Activity 1

# def start_program():
#     user_input = None
#     user_input = input("Please enter you telephone number:>           ")
#     try:
#         user_input = int(user_input)
#         print(f"Thank you, you entered the following number: 0{user_input}")
#     except:
#         print("Error: Please enter your phone number using only numerical characters")
#         start_program()

# start_program()

#Activity 2 

cast_members = ["Bill Murray as Dr. Peter Venkman", "Dan Aykroyd as Dr. Raymond Stantz", "Sigourney Weaver as Dana Barrett", "Harold Ramis as Dr. Egon Spengler", "Rick Moranis as Louis Tully", "Annie Potts as Janine Melnitz", "William Atherton as Walter Peck", "Ernie Hudson as Winston Zeddemore", "David Margulies as Mayor"]

movie_quotes = ["Dr. Raymond Stantz: Everything was fine with our system until the power grid was shut off by dickless here", "Winston Zeddemore: Ray, when someone asks you if you're a god, you say \"YES\"!", "Dr. Peter Venkman: We came, we saw, we kicked its ass!", "Dr. Peter Venkman: Human sacrifice, dogs and cats living together... MASS HYSTERIA!", "Dr. Peter Venkman: Human sacrifice, dogs and cats living together... MASS HYSTERIA!"] 

def cast_mem():
    user_selection = input("Would you like to see a list of actors? (Yes/No)")
    if user_selection == "Yes":
        for i in cast_members:
            print(i)
    else:
        return

print("Welcome to the Ghostbusters (1984) App")
cast_mem()