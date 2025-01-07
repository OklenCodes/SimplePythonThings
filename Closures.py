#closures // is a function having access to the scope of its parent function
#after the parent function has returned

# def parent_function(person):
#     coins = 3

#     def play_game():
#         nonlocal coins
#         coins -= 1

#         if coins > 1:
#             print("\n" + person + " has " + str(coins) + " coins left.")
#         elif coins == 1:
#             print("\n" + person + " has " + str(coins) + " coin left.")
#         else:
#             print("\n" + person + " is " + str(coins) + " out of coins.")

#     return play_game



tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

tommy() # Tommy should have 2 coins left 
tommy() # Tommy should have 1 coins left 

jenny() # Jenny should have 2 coins left 

tommy() # Jenny should no coins left 

jenny() # Jenny should have 1 coins left 

def parent_function(person, coins):  #Now we can decide how many coins is given out as a parameter
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is " + str(coins) + " out of coins.")

    return play_game



tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy() # Tommy should have 3 coins left 
tommy() # Tommy should have 2 coins left 

jenny() # Jenny should have 4 coins left 

tommy() # Jenny should have 1 coin left 

jenny() # Jenny should have 3 coins left
