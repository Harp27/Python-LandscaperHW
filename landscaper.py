game_data = {
    "money": 0,
    "rusty_scissors": False,
    "push_lawnmower": False,
    "fancy_lawnmower": False,
    "team_of_students": False,
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

def use_fancy_lawnmower():
    print("You start cutting a lawn with your fancy battery-powered lawnmower...")
    game_data["money"] += 100
    print("You earned $250!")

def hire_team_of_students():
    if game_data["money"] >= 500:
        game_data["money"] -= 500
        game_data["team_of_students"] = True
        print("You hired a team of starving students!")
    else:
        print("You don't have enough money to hire a team of starving students.")

def use_team_of_students():
    if game_data["team_of_students"]:
        print("You start cutting lawns with your team of starving students...")
        game_data["money"] += 250
        print("Your team earned you $250!")
    else:
        print("You need a team of starving students to do this.")

def win_game():
    if game_data["team_of_students"] and game_data["money"] >= 1000:
        print("Congratulations! You've won the game.")
        game_data["quit"] = True

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

def buy_fancy_lawnmower():
    if game_data["money"] >= 250:
        game_data["money"] -= 250
        game_data["fancy_lawnmower"] = True
        print("You bought a fancy battery-powered lawnmower!")
    else:
        print("You don't have enough money to buy a fancy battery-powered lawnmower.")

while True:
    user_input = input("""
                    What would you like to do?
                    [1] Cut a lawn with your teeth
                    [2] Cut a lawn with rusty scissors
                    [3] Use old-timey push lawnmower
                    [4] Use fancy battery-powered lawnmower
                    [5] Hire a team of starving students for $500
                    [6] Use your team of starving students
                    [7] Buy rusty scissors for $5
                    [8] Buy old-timey push lawnmower for $25
                    [9] Buy fancy battery-powered lawnmower for $250
                    [10] Quit the game
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
        if game_data["fancy_lawnmower"]:
            use_fancy_lawnmower()
            print(f"You now have a total of ${game_data['money']}")
        else:
            print("You need a fancy battery-powered lawnmower to use.")
    
    elif user_input == '5':
        hire_team_of_students()
        print(f"You now have a total of ${game_data['money']}")

    elif user_input == '6':
        use_team_of_students()
        print(f"You now have a total of ${game_data['money']}") 
        
    elif user_input == '7':
        buy_rusty_scissors()
        print(f"You now have a total of ${game_data['money']}")
        
    elif user_input == '8':
        if game_data["rusty_scissors"]:
            buy_push_lawnmower()
            print(f"You now have a total of ${game_data['money']}")
        else:
            print("You need rusty scissors to buy an old-timey push lawnmower.")
        
    elif user_input == '9':
        if game_data["push_lawnmower"]:
            buy_fancy_lawnmower()
            print(f"You now have a total of ${game_data['money']}")
        else:
            print("You need an old-timey push lawnmower to buy a fancy battery-powered lawnmower.")
        
    elif user_input == '10':
        game_data["quit"] = True

    win_game()
     
    if game_data["quit"]:
        print("You quit the game")
        break