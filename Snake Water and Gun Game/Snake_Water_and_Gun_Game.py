import random

# function one-----------------------------------------------------------


def gamebrain(comp, mine, countmine, countcomp):
    mine = mine.lower()

    if (comp == mine):
        print("ROUND DRAWN")

    elif (comp == "snake" and mine == "gun"):
        print("YOU WON THE ROUND")
        countmine += 1

    elif (comp == "gun" and mine == "water"):
        print("YOU WON THE ROUND")
        countmine += 1

    elif (comp == "water" and mine == "snake"):
        print("YOU WON THE ROUND")
        countmine += 1

    else:
        print("YOU LOSE THE ROUND")
        countcomp += 1

    return [countmine, countcomp]

# function two --------------------------------------------------------------------------------


def count(countmine, countcomp):
    print("")
    if (countmine == countcomp):
        print("MATCH TIED")
    elif (countmine > countcomp):
        print("YOU WON THE MATCH")
    else:
        print("YOU LOSE THE MATCH")
    print(f"You WON {countmine} times AND the Computer WON {countcomp} times. Number of Rounds Drawen --> { number -(countcomp+countmine)}\n ")


# Main code -------------------------------------------------------------------------------

countmine = 0
countcomp = 0
number = int(input("\nEnter how many ROUNDS you want to play : "))
print("")  # Can be used to get a new line.
print("-"*50)
print("")
for i in range(1, number + 1):
    print(f"ROUND {i}")
    choice = ("snake", "water", "gun")
    # randint() function choose a number from the range (0,n) ----> random.randint(0,2) ; n=2, where n = 2 the last limit of the range.
    comp = random.randint(0, 2)
    comp = choice[comp]  # choice[ comp --> index number of tupple "choice"]
    mine = input('''Enter "SNAKE" or "WATER" or "GUN" : ''')
    if (i == 1):
        result = gamebrain(comp, mine, countmine, countcomp)
    else:
        result = gamebrain(comp, mine, result[0], result[1])

    print(f"You Chose {mine} AND the Computer Chose {comp}.\n")
print("-"*50)
count(result[0], result[1])
