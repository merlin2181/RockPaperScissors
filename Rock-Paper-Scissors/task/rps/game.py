# Write your code here
import random


def winner(player, computer):
    # a dictionary where the selected key defeats the value in the Rock Paper Scissors game.
    rock_paper_scissors = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if rock_paper_scissors[player] == computer:
        return f"Well done. Computer choose {computer} and failed"
    if rock_paper_scissors[computer] == player:
        return f"Sorry, but computer chose {computer}"
    if player == computer:
        return f"There is a draw ({player})"


choices = ['rock', 'paper', 'scissors']  # list of available choices to play the game
user_choice = input()  # get user's choice
computer_choice = random.choice(choices)  # pseudo-random selection of available moves
winner = winner(user_choice, computer_choice)  # find a winner
print(winner)  # print winner
