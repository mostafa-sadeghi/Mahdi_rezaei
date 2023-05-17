# for i in range(5):
#     print("hello")


# i = 0
# while i < 5:
#     print("hello")
#     i += 1

# quit = "no"
# while quit == "no":
#     quit = input("Do you want to quit?(yes or no?) ")

# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit == "yes":
#         done = True
#     attack = input("Does your elf attack the dragon? ")
#     if attack == "yes":
#         print("Bad choice, you died.")
#         done = True

import random

# x = random.randrange(10)
# print(x)
# for i in range(100):
#     x = random.randrange(1, 11)
#     print(x)

CHOICES = ("r", "p", "s")
# print(len(CHOICES))
# random_index = random.randrange(len(CHOICES))  # 0 1 2
# print(random_index)
# print(CHOICES[random_index])
# print(random.choice(CHOICES))

user_hand = input('enter your choice("r", "p", "s") ')
computer_hand = random.choice(CHOICES)

print("user choice", user_hand)
print("computer choice", computer_hand)
if user_hand == "r":
    if computer_hand == "p":
        print("Computer is winner!")
    elif computer_hand == "s":
        print("User is winner!")
    elif computer_hand == "r":
        print("both equal")
elif user_hand == "p":
    if computer_hand == "s":
        print("Computer is winner!")
    elif computer_hand == "r":
        print("User is winner!")
    elif computer_hand == "p":
        print("both equal")
