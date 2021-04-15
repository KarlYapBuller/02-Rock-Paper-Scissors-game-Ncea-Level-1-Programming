#Game History

game_summary = []

rounds_won = 0
rounds_lost = 0
rounds_drawn = 0
rounds_played = 5

for item in range(0, 5):
    result = input("Choose Result: ")

    outcome = "Round{}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1

    elif result == "won":
        rounds_won += 1

    elif result == "tie: ":
        rounds_drawn += 1

    game_summary.append(outcome)

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
