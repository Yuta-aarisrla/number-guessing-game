import random

print("-- Number guessing Game --")
print("(1) HARD MODE -- (2) EASY MODE")
mode = int(input("Choose Mode: "))
print()

def game(taret, num):
    for i in range(num,-1, -1):
       user_input = int(input("enter number:"))
    print() 
    if user_input == target:
        print("You win!")
        quit()
    elif user_input > target:
        print(f"The number is too high\n Try again! {i} left")
    elif user_input < target:
        print(f"The number is too low\n Try again! {i} left")

    print("you lose!")
    print("The correct ansmer is" + str(taret))

if mode == 1:
    target = random.randint(1, 30)
    print("guess the number between 1-10!")
    print("**you can guess 3 times.**")
    game(target, 9)
elif mode == 2:
    target = random.randint(1, 10)
    print("guess the number between 1-10!")
    print("**you can guess 3 times.**")
    game(target, 2)
