import pandas
nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
word = input("What word do you want to spell? ").upper()
nato_word = [nato_dict[letter] for letter in word]
print(nato_word)