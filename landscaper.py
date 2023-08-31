game_data = {
    "money": 0,
    "rusty_scissors": False,
    "push_lawnmower": False,
    "quit": False
}

def cut_lawn_with_teeth():
    print("You start cutting a lawn with your teeth...")
    game_data["money"] += 1
    print("You earned $1!")

def cut_lawn_with_rusty_scissors():
    print("You start cutting a lawn with your rusty scissors...")
    game_data["money"] += 5
    print("You earned $5!")

def use_push_lawnmower():
    print("You start cutting a lawn with your old-timey push lawnmower...")
    game_data["money"] += 50
    print("You earned $50!")

def buy_rusty_scissors():
    if game_data["money"] >= 5:
        game_data["money"] -= 5
        game_data["rusty_scissors"] = True
        print("You bought a pair of rusty scissors!")
    else:
        print("You don't have enough money to buy rusty scissors.")

def buy_push_lawnmower():
    if game_data["money"] >= 25:
        game_data["money"] -= 25
        game_data["push_lawnmower"] = True
        print("You bought an old-timey push lawnmower!")
    else:
        print("You don't have enough money to buy an old-timey push lawnmower.")

while True:
    user_input = input("""
                    What would you like to do?
                    [1] Cut a lawn with your teeth
                    [2] Cut a lawn with rusty scissors
                    [3] Use old-timey push lawnmower
                    [4] Buy rusty scissors
                    [5] Buy old-timey push lawnmower
                    [6] Quit the game
                    Enter the number of your choice: """)
    
    if user_input == '1':
        cut_lawn_with_teeth()
        print(f"You now have a total of ${game_data['money']}")

    elif user_input == '2':
        if game_data["rusty_scissors"]:
            cut_lawn_with_rusty_scissors()
            print(f"You now have a total of ${game_data['money']}")
        else:
            print("You need rusty scissors to cut lawns.")

    elif user_input == '3':
        if game_data["push_lawnmower"]:
            use_push_lawnmower()
            print(f"You now have a total of ${game_data['money']}")
        else:
            print("You need an old-timey push lawnmower to use.")
        
    elif user_input == '4':
        buy_rusty_scissors()
        print(f"You now have a total of ${game_data['money']}")

    elif user_input == '5':
        buy_push_lawnmower()
        print(f"You now have a total of ${game_data['money']}")
        
    elif user_input == '6':
        game_data["quit"] = True
        
    if game_data["quit"]:
        print("You quit the game")
        break