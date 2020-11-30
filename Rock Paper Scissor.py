import random
def gameWin(guess, comp):
    if guess == comp:
        return None
    elif guess == "Rock":
        if comp == "Paper":
           return False
        else:
            return True
    elif guess == "Paper":
        if comp == "Scissors":
           return False
        else:
            return True
    elif guess == "Scissors":
        if comp == "Rock":
            return False
        else:
            return True

print("Computer has already played!")
num = random.randint(1,3)

if num == 1:
    comp = "Rock"
elif num == 2:
    comp = "Scissors"
else:
    comp = "Paper"
guess = input("Your turn! Rock, Paper or Scissors?")

a = gameWin(guess, comp)

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print(f"You lose! Your guess was {guess} and Computer's guess was {comp}.")
