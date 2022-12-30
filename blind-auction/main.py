import os
from art import logo

print(logo)
auction_running = True


def find_winner(auction_record):
    highest_bid = 0
    winner = ""
    for key in auction_record:
        if highest_bid < auction_record[key]:
            heighest_bid = auction_record[key]
            winner = f"{key}"
    print(f"The winner is {winner} with heighest bid of {heighest_bid}")


while auction_running:
    name = input("Type your name: ")
    bid = int(input("Type bid price: "))

    auction_record = {}
    auction_record[name] = bid
    other_users = input(
        "Are there other users who want to place bid? 'Y' for Yes and 'N' for No: "
    ).lower()
    if other_users == 'y':
        #clear terminal
        os.system('cls')
        print(logo)
    elif other_users == 'n':
        auction_running = False
        find_winner(auction_record)
