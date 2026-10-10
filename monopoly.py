import random

# Very simple Monopoly for 2 players.
board = [
    "GO", "Old Kent Road", "Whitechapel Road", "Tax",
    "The Angel", "Euston Road", "Free Parking", "Pall Mall",
    "Whitehall", "Tax", "Park Lane", "Mayfair"
]

prices = [0, 60, 80, 0, 100, 120, 0, 140, 160, 0, 200, 240]
owners = [None] * len(board)
money = [500] * 2
positions = [0] * 2
playing = [True] * 2
names = []

print("SIMPLE MONOPOLY")
print("Pass GO: collect £100. Tax: pay £100.")
print("Rent is a quarter of the property's price.")
print("No houses or jail. Last player left wins!\n")

for player in range(2):
    name = input(f"Player {player + 1} name: ").strip()
    names.append(name or f"Player {player + 1}")

quit_game = False

while sum(playing) > 1 and not quit_game:
    for player in range(2):
        if not playing[player]:
            continue

        print(f"\n{names[player]}'s turn — £{money[player]}")
        answer = input("Press Enter to roll, or q to quit: ")

        if answer.lower().strip() == "q":
            quit_game = True
            break

        dice = random.randint(1, 6)
        positions[player] += dice
        print(f"You rolled {dice}!")

        if positions[player] >= len(board):
            positions[player] -= len(board)
            money[player] += 100
            print("Passed GO! Collect £100.")

        square = positions[player]
        print(f"You landed on {board[square]}.")

        if board[square] == "Tax":
            money[player] -= 100
            print("Pay £100 tax.")

        elif prices[square] > 0:
            owner = owners[square]

            if owner is None:
                price = prices[square]

                if money[player] >= price:
                    buy = input(f"Buy for £{price}? (y/n): ")

                    if buy.lower().strip() == "y":
                        money[player] -= price
                        owners[square] = player
                        print("Bought!")
                else:
                    print("You cannot afford this property.")

            elif owner != player:
                rent = prices[square] // 4
                paid = min(money[player], rent)
                money[owner] += paid
                money[player] -= rent
                print(f"You paid {names[owner]} £{paid} rent.")

            else:
                print("You own this property.")

        if money[player] <= 0:
            money[player] = 0
            playing[player] = False
            print(f"{names[player]} is bankrupt and out of the game!")

            for property_number in range(len(board)):
                if owners[property_number] == player:
                    owners[property_number] = None

        print(f"Money: £{money[player]}")

        if sum(playing) == 1:
            break

if quit_game:
    print("\nGame ended.")
else:
    winner = playing.index(True)
    print(f"\n{names[winner]} wins with £{money[winner]}!")