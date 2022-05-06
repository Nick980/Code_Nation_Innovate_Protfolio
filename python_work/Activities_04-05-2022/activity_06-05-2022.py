user_input = "None"

def start_program():
    global user_input
    user_input = "None"
    user_input = input("Please enter you telephone number:>           ")
    try:
        user_input = int(user_input)
    except:
        print("Error: Please enter your phone number using only numerical characters")
        start_program()

start_program()
print(f"Thank you, you entered the following number: 0{user_input}")

# dont judge, still have things to add!!! 