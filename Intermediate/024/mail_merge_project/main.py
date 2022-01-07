with open("./Input/Names/invited_names.txt") as names:
    people = names.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
for name in people:
    new_name = name.strip()
    letter = starting_letter.replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/leter_for_{new_name}", "w") as ready_letters:
        ready_letters.write(letter)