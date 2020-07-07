# Write your code here
import random
import os


def winner(player, computer, moves, score):
    if player == computer:
        score += 50
        return f"There is a draw ({player})", score
    user_index = moves.index(player)
    midpoint = (len(moves) - 1) // 2
    if user_index >= midpoint:
        losers = moves[user_index - midpoint:user_index]
        if computer in losers:
            score += 100
            return f"Well done. Computer choose {computer} and failed", score
        else:
            return f"Sorry, but computer chose {computer}", score
    if user_index < midpoint:
        user_index += 1  # shifts index to the right by 1
        winners = moves[user_index:midpoint + user_index]
        if computer in winners:
            return f"Sorry, but computer chose {computer}", score
        else:
            score += 100
            return f"Well done. Computer choose {computer} and failed", score


def get_points(user):
    if os.path.exists('rating.txt'):
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


name = input("Enter your name: ")
print(f"Hello, {name.title()}")
points = get_points(name)
choices = input("Type a list of choices separated by a comma. No Spaces! or leave blank for the "
                "default rock, paper, scissors:\n").split(',')
if choices[0] == '':
    choices = ['rock', 'paper', 'scissors']
print("Okay, let's start")
while True:
    options = [choices, '!exit', '!rating']
    user_choice = input("Enter your choice: ")  # get user's choice
    if user_choice not in options[0] and user_choice not in options[1:]:
        print("Invalid input")
        continue
    if user_choice == options[2]:  # prints out the user's rating (points)
        if points > 0:
            print(f"Your rating: {points}")
        else:
            print("Your rating: 0")
        continue
    if user_choice == options[1]:
        print("Bye!")
        break
    if user_choice in options[0]:
        computer_choice = random.choice(choices)  # pseudo-random selection of available moves
        who_wins, points = winner(user_choice, computer_choice, choices, points)  # find a winner
        print(who_wins)  # print winner
        continue
