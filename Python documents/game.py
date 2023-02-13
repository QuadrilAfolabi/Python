import random
print("Welcome to the Number Guessing Game.")
print('I am thinking of a number right now.')

n = input("Choose between 'easy' and 'hard': ")
if n =="easy":
    y = 10
elif n == 'hard':
    y = 5
else:
    print("Enter a valid option")
    y = False
while y:
    query = random.randint(0,5)
    print(f"You have {y} attempts left")
    v = input("Make a guess...")

    if int(v)>query:
        print("Too high")
        print("Guess again..")
    
    if int(v)<query:
        print("Too low")
        print("Guess again...")

    if int(v)==query:
        print("You Won!!!")
        break
    if y == 0:
        print("GAME OVER!!!")
        break
    y-=1