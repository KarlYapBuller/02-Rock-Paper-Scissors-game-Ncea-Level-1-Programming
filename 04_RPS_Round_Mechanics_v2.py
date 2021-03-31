#More efficient than 04_RPS_Round_Mechanics_v1.py
#Heading and 'xxx' break code not working

#Functions used to check input is valid

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
                continue

        return response

#Main routine goes here

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

#Ask user for number of rounds they want to play or if they want to play infinite mode they press <enter>

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
    choose = input("{} or 'xxx' to end the game:".format(choose_instruction))

#End game if exit code is typed
    if choose == "xxx":
        break

#rest of loop/game
    print("You chose {}".format(choose))

    rounds_played += 1

#End game if the number of rounds has been played
    if rounds_played == rounds:
        break

print("Thank you for playing")
