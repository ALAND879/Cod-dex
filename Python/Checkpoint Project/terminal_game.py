# A classic mini-RPG (role-playing game) with hp health points, character moves like attack/block/heal,
# and NPCs (non-player characters) that attacks based on a random number generator.

import random

# variables
User_Health_Points = 100
Enemy_Health_points = 100
Enemy_Defense = 0
movement_choice = 0
game_round = 1
User_damage = 0
User_defense = 0
User_heal = 0
score = 0
enemy_killed = 1

# Introduction to the game
print("Welcome to the game! \nYou start with 100 health points, try to get the highest score possible.")
print("You can attack, block, or heal.")
print("The enemy will attack you with a random amount of damage, in the round 5 the enemy will start to defend.")
print("The game will get harder as you progress through the rounds.")
print("The score is calculated by the number of rounds you survive, kill enemies give extra score.")
print("Good luck!\n\n")

# Game loop until the Player dies
while User_Health_Points > 0:

    print("\n\tRound ", game_round)
    # User movement election
    while movement_choice != 1 or movement_choice != 2 or movement_choice != 3:
        print("--List of Movements--")
        print("1) Attack")
        print("2) Block")
        print("3) Heal")
        movement_choice = int(input("Enter your choice: "))
        if movement_choice == 1 or movement_choice == 2 or movement_choice == 3:
            break
        else:
            print("Invalid choice, try again.\n")
            break

    # Make  the stats of the movement selected
    if movement_choice == 1:
        print("You chose to attack.")
        User_damage = random.randint(10, 50)
        print("Your attack is: ", User_damage)
        User_defense = 0
        User_heal = 0

    elif movement_choice == 2:
        print("You chose to block.")
        User_defense = random.randint(1, 30)
        print("Your defense is: ", User_defense)
        User_damage = 0
        User_heal = 0

    elif movement_choice == 3:
        print("You chose to heal.")
        User_heal = random.randint(18, 25)
        print("You're going to heal: ", User_heal)
        User_damage = 0
        User_defense = 0

# Enemy's turn
# Randomly generate enemy stats
    Enemy_attack = random.randint((1+game_round), (3+game_round))
    if game_round > 5:
        Enemy_Defense = random.randint(0, game_round)

# Show the stats
    print(f"\n\nYour Stats: \nHealth Points:{User_Health_Points} \nAttack: {User_damage} \nDefense: {User_defense} \nYou healed: {User_heal}.\n")
    print(f"Enemy's Stats: \nHealth Points:{Enemy_Health_points} \nAttack: {Enemy_attack} \nDefense: {Enemy_Defense}\n")

# Movements
    Enemy_defended = User_damage - Enemy_Defense
    if Enemy_defended < 0:
        Enemy_defended = 0
    Enemy_Health_points = Enemy_Health_points - Enemy_defended

    if User_Health_Points > 0:
        if Enemy_Health_points < 0:
            print("You killed the enemy!")
            print("You have ", User_Health_Points, "health points left.")
            User_Health_Points += 10
            score = score + (enemy_killed * 25)
            print("You gained 10 health points and 25 points of score.")
            print("A new enemy appears!")
            enemy_killed = enemy_killed + 1
            Enemy_Health_points = 100

        else:
            Enemy_new_attack = Enemy_attack - User_defense
            if Enemy_new_attack < 0:
                Enemy_new_attack = 0
            User_Health_Points += User_heal
            User_Health_Points -= Enemy_new_attack

            if User_Health_Points <= 0:
                print("You died!")
                print(f"You survived {game_round} rounds.")
                print(f"You killed {enemy_killed-1} enemies.")
                print(f"Your score is {score}")
                break

        score = score + 10
        print("New round!")
        print(f"Starting stats: \nHealth Points: {User_Health_Points} \nEnemy Health Points: {Enemy_Health_points} \nscore: {score}")
        game_round = game_round + 1
        movement_choice = 0
        Enemy_Defense = 0
