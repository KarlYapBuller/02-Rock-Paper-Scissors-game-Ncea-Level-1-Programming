import random

#Functions

#Round Mechanics Function

#User Choice Rock,Paper,Scissors

def choice_checker(question, valid_list, error_message):

    valid = False
    while not valid:

        #Ask user for choice and pit choice in lowercase
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
        response = input ("How many rounds: ")

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

#Main Routine

#Lists for valid input for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

rounds_played = 0

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

#Get Computer Choice

#Compare User and Computer Choice

    computer_choice = random.choice(rps_list[:-1])
    print("Computer Choice: ", computer_choice)

    if user_choice == "rock":
        if computer_choice == "rock":
            result = "It is a draw"

        elif computer_choice == "paper":
            result = "You lost"

        else:
            result = "You Won"

    elif user_choice == "paper":

        if computer_choice == "rock":
            result = "You Won"

        elif computer_choice == "paper":
            result = "It is a draw"

        else:
            result = "You lost (Better luck next time)"

    else:

        if computer_choice == "rock":
            result = "You lost (Better luck next time)"

        elif computer_choice == "paper":
            result = "You Won"

        else:
            result = "It is a draw"


#End game if exit code is typed
    if user_choice == "xxx":
        break

#rest of loop/game


    print("You chose {} the computer chose {}. \nResult: {}. ".format(user_choice, computer_choice, result))
    rounds_played += 1

#End game if the number of rounds has been played
    if rounds_played == rounds:
        break

print("Thank you for playing")
