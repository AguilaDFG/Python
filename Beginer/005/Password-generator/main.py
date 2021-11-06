#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

num_characters = int(nr_letters + nr_numbers + nr_symbols)
password = ""
for n in range (0, num_characters):
  if nr_letters == 0 and nr_symbols == 0:
    n = random.choice(numbers)
    password += n
    nr_numbers -= 1
  elif nr_letters == 0 and nr_numbers == 0:
    s = random.choice(symbols)
    password += s
    nr_symbols -= 1
  elif nr_numbers == 0 and nr_symbols == 0:
    l = random.choice(letters)
    password += l
    nr_letters -= 1
  elif nr_letters == 0:
    lsn = random.randint(1, 2)
    if lsn == 1:
      n = random.choice(numbers)
      password += n
      nr_numbers -= 1
    elif lsn == 2:
      s = random.choice(symbols)
      password += s
      nr_symbols -= 1
  elif nr_numbers == 0:
    lsn = random.randint(1, 2)
    if lsn == 1:
      l = random.choice(letters)
      password += l
      nr_letters -= 1
    elif lsn == 2:
      s = random.choice(symbols)
      password += s
      nr_symbols -= 1
  elif nr_symbols == 0:
    lsn = random.randint(1, 2)
    if lsn == 1:
      l = random.choice(letters)
      password += l
      nr_letters -= 1
    elif lsn == 2:
      n = random.choice(numbers)
      password += n
      nr_numbers -= 1
  else:
    lsn = random.randint(1, 3)
    if lsn == 1:
      l = random.choice(letters)
      password += l
      nr_letters -= 1
    elif lsn == 2:
      s = random.choice(symbols)
      password += s
      nr_symbols -= 1
    else:
      n = random.choice(numbers)
      password += n
      nr_numbers -= 1
print(password)
#or adding the characters to a password list (in order, to make it simpler) and then use the function random.shuffle(list). Lastly with a for loop, add the list of shuffled characters in the password string