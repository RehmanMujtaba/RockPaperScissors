x = 5
while x == 5:
    print("Rock, Paper, Scissors?")

    ans = input()

    if ans == "Rock" or "rock":
        rep = "Paper"
        
    elif ans == "Paper" or "paper":
        rep = "Scissors"
        
    elif ans == "Scissors" or "scissors":
        rep = "Rock"
        
    else:
        continue

    print("I choose %s, you lose :(" % rep)

    print("Play again? y/n")

    ans1 = input()

    if ans1 == "No" or "no" or "n":
        break
    elif ans1 != "Yes" or "yes" or "y":
       print("Sorry, did not quite catch that")
    
