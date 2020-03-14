# Rock Paper Scissors game

# import modules we need
import random

#results - load_results()
# file i/o functions for historical results


def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history


def save_results(w, l, t):
    text_file = open("history.txt", "w")
    text_file.write(str(w) + "," + str(l) + "," + str(t))
    text_file.close()


# welcome message
results = load_results()

wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
print("Welcome to Rock, Paper, Scissors!")
print("Wins: %s Losses: %s Ties: %s " % (wins, losses, ties))
print("Please choose to continue...")

# initialize user, computer choices
computer = random.randint(1, 3)
user = int(input("[1] Rock   [2] Paper   [3] Scissors   [9] Quit\n"))

# gameplay loop
while not user == 9:
    # user chooses ROCK
    if user == 1:
        if computer == 1:
            print("Computer chose rock... tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper... computer wins!")
            losses += 1
        else:
            print("Computer chose scissors... you win!")
            wins += 1
    # user chooses PAPER
    elif user == 2:
        if computer == 1:
            print("Computer chose rock... you win!")
            wins += 1
        elif computer == 2:
            print("Computer chose paper... tie!")
            ties += 1
        else:
            print("Computer chose scissors... you lose!")
            losses += 1
    # user chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("Computer chose rock... computer wins!")
            losses += 1
        elif computer == 2:
            print("Computer chose paper... you win!")
            wins += 1
        else:
            print("Computer chose scissors... tie!")
            ties += 1
    else:
        print("Invalid selection. Please try again.")

        # print updated stats
        print("Wins: %s Losses: %s Ties: %s " % (wins, losses, ties))

        # prompt user to make another selection
        print("Please choose to continue...")
        # initialize user, computer choices
        computer = random.randint(1, 3)
        user = int(input("[1] Rock   [2] Paper   [3] Scissors   [9] Quit\n"))

# game over, save results
save_results(wins, losses, ties)
