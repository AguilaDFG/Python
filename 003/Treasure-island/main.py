print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cave = input("You see a cave to your right and it is drizzling a bit, do you want to enter? Y or N\n").lower()
if cave == "n":
  print("It starts raining more and more and you find yourself in a storm. A lightning hits you. You died")
elif cave == "Y" or cave == "y":
  river = input("There is an underground river blocking your path, would you like to swim(S) across it or jump(J) it using some rocks to get to the other side?\n").lower()
  if river == "s" or river == "swim":
    print("The current is too strong and you hit with some rocks. You died")
  elif river == "j"  or river == "jump":
    tunnel = input("The cave is separated in three before you, where do you want to go? L, R or M\n").lower()
    if tunnel == "r":
      print("A bear attacks you. You died")
    elif tunnel == "m":
      print("It is too dark to see anything and you fall into a hole. You died")
    elif tunnel == "l":
      print("You find a chest with lots of gold and treasures and the exit of the cave. You win")
    else:
      print("It seems you don't know what to do. While you're making up your mind, some wolves appear and attack you. You died")
  else:
    print("It seems you don't know what to do. While you're making up your mind, some wolves appear and attack you. You died")
else:
  print("It seems you don't know what to do. While you're making up your mind, some wolves appear and attack you. You died")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload