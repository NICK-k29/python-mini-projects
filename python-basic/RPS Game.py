import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: Match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper covers Rock = compurt win")
    else:
        print("Rock smashes Scissor = you win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Paper,computer win")
    else:
        print("Paper Covers Rock, you win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor,computer win")
    else:
        print("Scissor Cuts Paper, you win")