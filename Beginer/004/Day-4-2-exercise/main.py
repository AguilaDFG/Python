# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
ammount_of_names = len(names)
payer = names[random.randint(0, ammount_of_names - 1)]
#or:
#payer = random.choice(names)

print(f"{payer} pays.")