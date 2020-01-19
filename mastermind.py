import random

in_game = True
valid_colors = ["R", "G", "B", "C", "M", "Y"]
user_colors = []
computer_colors = ["", "", "", ""]

available_colors = valid_colors.copy()
for x in range(4):
    random_number = random.randint(0, len(available_colors) - 1)
    computer_colors[x] = available_colors[random_number]
    available_colors.remove(available_colors[random_number])

while in_game:
    valid_input = False
    clue = []
    computer_colors_copy = computer_colors.copy()
    while not valid_input:
        user_colors = input(f"Please enter four colors for your guess (do not use duplicate colors). Colors: {''.join(valid_colors)} ").upper()
        input_flag = False

        for color in user_colors:
            if color not in valid_colors:
                print(f"{color} is not a valid color.")
                input_flag = True

        if len(user_colors) > 4:
            print("You entered too many colors. Please enter four colors.")
            input_flag = True

        if not (len(user_colors) == len(set(user_colors))):
            input_flag = True
            
        if input_flag:
            print(f"Your input {user_colors} was invalid. Please try again.")
        else:
            valid_input = True

    for x in range(4):
        if computer_colors_copy[x] == user_colors[x]:
            computer_colors_copy[x] = ''
            clue.append('*')
        elif user_colors[x] not in computer_colors:
            computer_colors_copy[x] = ''
            clue.append('#')
        else:
            computer_colors_copy[x] = ''
            clue.append('~')
    

    print(f"Your input {user_colors}")
    print(f"Computer input {''.join(computer_colors)}")
    print(f"Your clue is {clue}")

    if clue.count('*') == 4:
        print("You guessed the correct colors!")
        in_game = False
    else:
        print("That is not the correct code! Guess again!")
        