import random

#Functions

#Played before function, output depends on what the user answers
#If the user answers yes, program continues to ask the user how much they want to play with
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
def played_before(question):
    valid = False
    while not valid:
        response = input(question).lower()
#If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response
#If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response
#If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer yes/no")

#User Game Instructions 
def Rock_Paper_Scissors_Game_Instructions():
    print("Welcome to the Rock, Paper, Scissors game")
    print("This game follows the basic and universal rules of Rock, Paper and Scissors")
    print("If you do not know what these rules are they are as followed:")
    print("Rock, Paper, Scissors is a game where you verse another person (in this case a computer).")
    print("In this game you throw hand gestures in the hope of winning")
    print("The hand gestures are Rock, Paper and Scissors")
    print("THe mechanics on how to win the game are as followed:")
    print("Rock beats Scissors, this also means that Scissors losses to Rock")
    print("Paper beats Rock, this also means Rock losses to Paper")
    print("Scissors beats Paper, this also means that Paper losses to Scissors ")
    print("If you and your opponent have the same hand gesture the match is a tie.")
    print("In this Rock, Paper, Scissors game there is two game modes.")
    print("The first game mode is where you can set the maximum amount of games your want to play")
    print("THe second game mode is continuous mode where you can play an infinite number of rounds")
    print("To play infinite mode press <Enter> or the Space bar when you are asked how many rounds you want to play")
    print("If you ever want to quit the game type 'xxx'")
    print("This is all the information you need to know")
    print("Good luck hopefully you can beat the computer in this game of Rock, Paper and Scissors.")
    return""


def choice_checker(question, valid_list, error_message):

    valid = False
    while not valid:

        #Ask user for choice and puts choice in lowercase
        response = input(question).lower()

        #Iterates through list anf if response is an item
        #In the list (or the first letter of an item),
        #The full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        #Output error if the item is not in the list
        print(error_message)
        print()



def check_rounds():
    while True:
        statement_generator("How many rounds: ", "#")
        response = input("How many rounds do you want to play: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
#If ifinite mode is not chosen, check response is an integer more than 0
        if response != "":
            try:
                response = int(response)

#If response is too low, go back to the start of the loop and display an error message to help user
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response

#Statement generator
#Decorates the statements in the Lucky Unicorn game
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides , statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main Routine

#Welcomes user to the Lucky Unicorn game, the
#"Welcome to the Lucky Unicorn game" statement is decorated
statement_generator("Welcome to the Rock ✊, Paper ✋, Scissors ✌ game", "*")
print()

#Calls ask user if they have played before funtion and game information function
#Played before statement is decorated
#If the user answers yes, program continues to ask the user how much they want to play with
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
print()
statement_generator("Played before", "?")
show_played_before = played_before("Have you played this game before (yes/no)?")
print()

if show_played_before == "no":
    print()
    Rock_Paper_Scissors_Game_Instructions()

#Lists for valid input for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

#Emoji
rock_emoji = "✊"
paper_emoji = "✋"
scissors_emoji = "✌"

#Game History
game_summary = []

#Rounds
rounds_played = 0
rounds_won = 0
rounds_lost = 0
rounds_drawn = 0

rounds = check_rounds()

end_game = "no"
while end_game == "no":

#Round heading

    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)


    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)

    choose_instruction = "Please choose rock (r), paper (p) or scissors (s) or 'xxx to quit the game: "

    choose_error = "<Error> Please choose from rock (r), paper (p) or scissors (s)"

#Ask user for choice and check it is valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

#End game if exit code is typed
    if user_choice == "xxx":
        break

#Get Computer Choice
    computer_choice = random.choice(rps_list[:-1])

#Compare User and Computer Choice

#If User inputs the same option as the COmputers random choice
#result is outputed to the User as that they drew with the computer in that round
    if computer_choice == user_choice:
        result = "tie 👔"
        rounds_drawn += 1

#Rock beats Scissors
#Result is outputed to the User that they hay have won the round
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "Won ✔"
        rounds_won += 1

#Paper beats Rock
#Result is outputed to the User that they hay have won the round
    elif user_choice == "paper" and computer_choice == "rock":
        result = "Won ✔"
        rounds_won += 1

#Scissors beats Paper
#Result is outputed to the User that they hay have won the round
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "Won ✔"
        rounds_won += 1

#If User inputs either Rock, Paper or Scissors and the Computers choice wins
#Result is outputed to the User that they have lost the round
    else:
        result = "Lost ❌ (Better Luck next time)"
        rounds_lost += 1

    if result == "tie":
        feedback = "Result: It is a tie 👔"
    else:
        feedback = "You chose {} the computer chose {}. \nResult: You {}. ".format(user_choice.upper(), computer_choice.upper(), result)

#Result outputed to User
    print(feedback)

    rounds_result = "Round {}, Result: {}".format(rounds_played + 1, result)
    game_summary.append(rounds_result)

    rounds_played += 1

#End game if the number of rounds has been played
    if rounds_played == rounds:
        break

#Statistics

#Calculate Game Statistics

percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tied = rounds_drawn / rounds_played * 100

print()
print("*****Game History*****")
for game in game_summary:
    print(game)

print()

#Displays Game Statistics with percentage (%) values to the nearest whole number

print("*****Game Statistics*****")
print("Win: {}, ({:.0f}%)\nLoss: {},({:.0f}%)\nTied: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_tied))

