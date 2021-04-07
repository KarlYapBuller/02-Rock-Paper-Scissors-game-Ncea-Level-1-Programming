#Rock, Paper, Scissors Computer Choice

import random

rps_list = ["rock", "paper", "scissors", "xxx"]

for item in range(0,20):
    computer_choice = random.choice(rps_list[:-1])
    print(computer_choice, end="\t")
