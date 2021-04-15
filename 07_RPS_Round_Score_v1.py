#RPS Component 7- Scoring System

#Rounds won will be calculated (total - draw - lost)

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

#Results for testing purposes
test_results = ["won", "won", "loss", "loss","tie"]

#Play Game
for item in test_results:
    rounds_played += 1

    #Generate computer choice

    result = item

    if result == "tie":
        result = "It is a tie"
        rounds_drawn += 1

    elif result == "loss":
        rounds_lost += 1

#Statistics
#Rounds won will be calculated (total - draw - lost)
rounds_won = rounds_played - rounds_lost - rounds_drawn

#End of Game Summary
print()
print("*****End Game Summary*****")
print("Rounds Won: {} \t|\t Rounds Lost: {} \t|\t Rounds Drawn: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thank you for playing")
