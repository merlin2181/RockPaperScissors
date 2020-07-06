# Write your code here
import random


def winner(player, computer, score):
    # a dictionary where the selected key defeats the value in the Rock Paper Scissors game.
    rock_paper_scissors = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if rock_paper_scissors[player] == computer:
        score += 100
        return f"Well done. Computer choose {computer} and failed", score
    if rock_paper_scissors[computer] == player:
        return f"Sorry, but computer chose {computer}", score
    if player == computer:
        score += 50
        return f"There is a draw ({player})", score


def get_points(user):
    # check to see if the user's name is saved in the ratings.txt file.
    file = open('rating.txt')
    names = file.readlines()
    file.close()
    names = [names[i].split() for i in range(len(names))]
    for player in names:
        if user in player:
            score = player
            return int(score[1])
    return 0


choices = ['rock', 'paper', 'scissors']  # list of available choices to play the game
name = input("Enter your name: ")
print(f"Hello, {name.title()}")
points = get_points(name)
while True:
    options = ['rock', 'paper', 'scissors', '!exit', '!rating']
    user_choice = input()  # get user's choice
    if user_choice not in options:
        print("Invalid input")
        continue
    if user_choice == options[4]:  # prints out the user's rating (points)
        if points > 0:
            print(f"Your rating: {points}")
        else:
            print("Your rating: 0")
        continue
    if user_choice == options[3]:
        print("Bye!")
        break
    if user_choice in options[:3]:
        computer_choice = random.choice(choices)  # pseudo-random selection of available moves
        who_wins, points = winner(user_choice, computer_choice, points)  # find a winner
        print(who_wins)  # print winner
        continue
