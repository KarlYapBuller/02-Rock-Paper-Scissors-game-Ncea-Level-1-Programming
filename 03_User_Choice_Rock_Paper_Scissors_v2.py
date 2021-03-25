#Version 2- Error message included when calling function

#Functions go here

def choice_checker(question, error_message):

    valid = False
    while not valid:

        #Ask user for choice and pit choice in lowercase
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response

        elif response == "p" or response == "paper":
            return response

        elif response == "s" or response == "scissors":
            return response

        #Check for exit code
        elif response == "xxx":
            return response
        else:
            print(error_message)

#Main routine goes here


#Loop for testing purposes
user_choice_rock_paper_scissors = ""
while user_choice_rock_paper_scissors != "xxx":

    #Ask user for choice and check it is valid
    user_choice_rock_paper_scissors = choice_checker("Please choose rock, paper or scissors (r,p,s):",
                                                     "<Error> Please choose from rock, paper or scissors (r,p,s)")

    #print out choice for comparison purposes
    print("you chose {}".format(user_choice_rock_paper_scissors))
