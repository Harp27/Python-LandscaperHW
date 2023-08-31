game_data = {
    "money": 0,
    "quit": False
}

def cut_lawn_with_teeth():
    print("You start cutting a lawn with your teeth...")
    game_data["money"] += 1
    print("You earned $1!")

while True:
    user_input = input("""
                    What would you like to do?
                    [1] Cut a lawn with your teeth
                    [2] Quit the game
                    Enter the number of your choice: """)
    
    if user_input == '1':
        cut_lawn_with_teeth()
        print(f"You now have a total of ${game_data['money']}")
        
    elif user_input == '2':
        game_data["quit"] = True
        
    if game_data["quit"]:
        print("You quit the game")
        break