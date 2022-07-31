import random

playerwin = 0
compwin = 0
print("First to 3 wins! Good luck.")


def win(user,computer):
    if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        return True

while playerwin or compwin != 3:
    if playerwin == 3:
        print(f"Game over! You win {playerwin} - {compwin}!")
        quit()

    if compwin == 3:
        print(f"Game over! I win {compwin} - {playerwin}!")
        quit()
    
    print(f"You: {playerwin}, me: {compwin}")
    playerc = input("What do you choose? Rock (r), paper (p) or scissors (s)?")
    player = playerc.lower()
    comp = random.choice(["r","p","s"])
        
    if player == comp:
        print(f"It's a tie! We both picked {comp}")

    elif win(player,comp):
        playerwin = playerwin +1
        print(f"Congrats! You won. I picked {comp}")
    else:
        compwin = compwin +1
        print(f"Sorry! You lost. I picked {comp}")