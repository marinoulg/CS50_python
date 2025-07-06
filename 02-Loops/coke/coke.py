# In a file called coke.py, implement a program that prompts the user to
# insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change
# the user is owed. Assume that the user will only input integers, and ignore
# any integer that isn’t an accepted denomination.

amount_due = 50
accepted_coins = [5, 10, 25, 50]

while amount_due != 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: ").strip())
    if coin in accepted_coins:
        amount_due = amount_due - coin
    else:
        next
    if amount_due <= 0:
        print(f"Change Owed: {-amount_due}")
        break
