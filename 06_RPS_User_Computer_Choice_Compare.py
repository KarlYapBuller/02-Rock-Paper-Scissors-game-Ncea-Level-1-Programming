#Rock, Paper, Scissors- Compare User Choice and Computer Choice with one another and show user results

rps_list = ["rock", "paper", "scissors"]
computer_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        computer_choice = rps_list[computer_index]
        user_index += 1

        #Compare options

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


        print("You chose {} the computer chose {}. \nResult: {}. ".format(user_choice, computer_choice, result))


    computer_index += 1
    print()

