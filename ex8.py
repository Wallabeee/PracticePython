# Rock Paper Scissors
#
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

print("A game of rock-paper-scissors will now commence. Please make sure there are two players.")
print("""Remember the rules:
       Rock beats scissors
       Scissors beats paper
       Paper beats rock.\n""")

while True:
    player1 = input("Player 1 choose your move: ")
    player2 = input("Player 2 choose your move: ")

    if player1 == 'rock' and player2 == 'scissors':
        print("Rock beats scissors, player 1 wins.")
    elif player1 == 'scissors' and player2 == 'rock':
        print("Rock beats scissors, player 2 wins.")
    elif player1 == 'scissors' and player2 == 'paper':
        print("Scissors beats paper, player 1 wins")
    elif player2 == 'scissors' and player1 == 'paper':
        print("Scissors beats paper, player 2 wins")
    elif player1 == 'paper' and player2 == 'rock':
        print("Paper beats rock, player 1 wins.")
    elif player2 == 'paper' and player1 == 'rock':
        print("Paper beats rock, player 2 wins.")

    redo = input("Would you like to play again? (Y/N)\n>")

    if redo == 'N':
        break