#Version 3- Checks that response is in a given list

#Functions go here

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

#Main routine goes here

#Lists for valid input for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]


#Loop for testing purposes
user_choice_rock_paper_scissors = ""
while user_choice_rock_paper_scissors != "xxx":

    #Ask user for choice and check it is valid
    user_choice_rock_paper_scissors = choice_checker("Please choose rock, paper or scissors (r,p,s):", rps_list,
                                                     "<Error> Please choose from rock, paper or scissors (r,p,s)")

    #print out choice for comparison purposes
    print("you chose {}".format(user_choice_rock_paper_scissors))
