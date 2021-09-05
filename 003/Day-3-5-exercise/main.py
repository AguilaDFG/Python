# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_l = name1.lower()
name2_l = name2.lower()
T1 = name1_l.count("t")
T2 = name2_l.count("t")
R1 = name1_l.count("r")
R2 =name2_l.count("r")
U1 = name1_l.count("u")
U2 =name2_l.count("u")
E1 = name1_l.count("e")
E2 = name2_l.count("e")
L1 = name1_l.count("l")
L2 = name2_l.count("l")
O1 = name1_l.count("o")
O2 = name2_l.count("o")
V1 = name1_l.count("v")
V2 = name2_l.count("v")
score_true = str(T1+T2+R1+R2+U1+U2+E1+E2)
score_love = str(L1+L2+O1+O2+V1+V2+E1+E2)
scorestr = score_true + score_love
score = int(scorestr)
if score > 90 or score < 10:
  print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score is {score}")
  #Could have also concatinated the names in a single string in the beginning for simplicity