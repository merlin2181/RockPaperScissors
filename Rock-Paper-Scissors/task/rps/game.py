# Write your code here
def comp_wins(player):
    if player == "scissors":
        return "rock"
    if player == "paper":
        return "scissors"
    if player == "rock":
        return "paper"


user_choice = input()
computer = comp_wins(user_choice)
print(f"Sorry, but computer chose {computer}")
