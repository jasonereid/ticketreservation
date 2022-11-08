#variables
choice_1 = 1


# display message
print("""Welcome to the ticket reservation system. 
Please make a selection on what you would like to do: 

1. New Reservation
2. Lookup Existing Reservation
3. Cancel Reservation
""")

choice_1 = input("Please pick 1 through 3: ")
print("Your choice is " + choice_1)

if choice_1 == 1:
  # new reservation
  print("new reservation")
elif choice_1 == 2:
  # lookup existing
  print("lookup existing")
elif choice_1 == 3:
  # cancel existing
  print("cancel existing")
else:
  print("Please choose 1 through 3.")

# 
