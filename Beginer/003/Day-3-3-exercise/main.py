# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 != 0:
  print("not a leap year")
elif year % 400 == 0:
  print("leap year")
elif year % 100 == 0:
  print("not a leap year")
else:
  print("leap year")

#or :
#if year % 4 == 0:
 # if year % 100 == 0:
  #  if year % 400 == 0:
   #   print("leap year")
    #else:
     #   print("not a leap year")
  #else:
   # print("leap year")
#else:
 # print("not a leap year")