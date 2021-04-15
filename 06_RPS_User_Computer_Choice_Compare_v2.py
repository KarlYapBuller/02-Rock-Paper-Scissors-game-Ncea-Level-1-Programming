#Rock, Paper, Scissors- Compare User Choice and Computer Choice with one another and show user results
#Working and more effiecient than version 1
#Works in the Base Component

rps_list = ["rock", "paper", "scissors"]
computer_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        computer_choice = rps_list[computer_index]
        user_index += 1

        #Compare options

        if computer_choice == user_choice:
            result = "It is a draw"

        elif user_choice == "rock" and computer_choice == "scissors":
            result = "You Won"

        elif user_choice == "paper" and computer_choice == "rock":
            result = "You Won"

        elif user_choice == "scissors" and computer_choice == "paper":
            result = "You Won"

        else:
            result = "You Lost (Better Luck next time)"


        print("You chose {} the computer chose {}. \nResult: {}. ".format(user_choice, computer_choice, result))


    computer_index += 1
    print()
