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
            print()

#Game information function
#This is displayed if the user answers no, they have not played this game before
def game_information():
    print()
    print("*****Game information*****")
    print()
    print()
    print("*****Rules of the game*****")
    print()
    return""

#Main Routine

#Welcomes user to rock, paper, scissor game
print("Welcome to the rock, paper, scissor game")
print("We hope you enjoy your gaming experience")
print()

#Asks user if they have played the game before
show_played_before = played_before("Have you played this game before (yes/no)?")

#If user answers no they have not played before game information will be displayed
if show_played_before == "no":
    game_information()

print()
print("program continues")
