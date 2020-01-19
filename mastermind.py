secret = ["R", "B", "G", "Y"]
guess = ["R", "G", "B", "F"]
clue = []

for x in range(4):
    if secret[x] == guess[x]:
        clue.append('*')
    elif guess[x] not in secret:
        clue.append('#')
    else:
        clue.append('~')

print(f"The secret is {secret}")
print(f"The guess is {guess}")
print(f"The clue is {clue}")
