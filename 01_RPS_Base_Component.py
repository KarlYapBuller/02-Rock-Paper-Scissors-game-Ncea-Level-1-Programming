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
    computer_choice = random.choice(rps_list[:-1])
    print("Computer Choice: ", computer_choice)

#Compare User and Computer Choice

#If User chooses rock
    if user_choice == "rock":

        #If User chooses rock and computers random choice is rock the result is outputed as 'It is a draw'
        #To indicate to the user that they and the computer drew in that round
        if computer_choice == "rock":
            result = "It is a draw"

        #If User chooses rock and computers random choice is paper result is outputed as 'You lost'
        #To indicate to the user that they lost the round
        elif computer_choice == "paper":
            result = "You lost"

        #If User chooses rock and computers random choice is scissors result is outputed as 'You Won'
        #To indicate to the user that they won the round
        else:
            result = "You Won"

#If user chooses paper
    elif user_choice == "paper":

        #If User chooses paper and computers random choice is rock result is outputed as 'You Won'
        #To indicate to the user that they won the round
        if computer_choice == "rock":
            result = "You Won"

        #If User chooses paper and computers random choice is paper the result is outputed as 'It is a draw'
        #To indicate to the user that they and the computer drew in that round
        elif computer_choice == "paper":
            result = "It is a draw"

#The else is if the User chooses scissors

        #If User chooses paper and computers random choice is scissors result is outputed as 'You lost'
        #To indicate to the user that they lost the round
        else:
            result = "You lost (Better luck next time)"

#The else is if the User chooses scissors
    else:

        #If User chooses scissors and computers random choice is scissors result is outputed as 'You lost'
        #To indicate to the user that they lost the round
        if computer_choice == "rock":
            result = "You lost (Better luck next time)"

        #If User chooses scissors and computers random choice is paper result is outputed as 'You Won'
        #To indicate to the user that they won the round
        elif computer_choice == "paper":
            result = "You Won"

#The else is if the User chooses scissors

        #If User chooses paper and computers random choice is scissors the result is outputed as 'It is a draw'
        #To indicate to the user that they and the computer drew in that round
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
