import random as rd
from time import sleep
from rules import rules_show
from title import title
from generation_orders_bullets import gen_order_bullets as gob

# Game's Tittle
title('NORTHEAST ROULETTE')

# Asking if the player knows the rules. Handling excepetions.
print("Welcome to the underground of brazilian's northeast. How about betting your life for" \
" a coffee and couscous package?")
sleep(5)
while True:
    try:
        know_rules = str(input('Do you know the rules?\n[Y] or [N] >> '))[0].upper()
        if know_rules in "YN":
            break
        else:
            print('Invalid Answer! Please try again.')
            sleep(2)
            continue
    except:
        print('Invalid Answer! Please try again.')
        sleep(2)
        continue

# Explaining the rules and starting the game.
rules_show(know_rules)
input('Press Enter to start the game!')
print('Loading...')
sleep(5)
title('MACH STARTED')

# The match
hp_player = 5
hp_enemy = 5
current_round = 1
player_turn = True
bullet_turn = 0

while hp_player > 0 or hp_enemy > 0:

    # Match: generation of bullets
    numb_bullets = rd.randint(2, 6) # Ex: By chance is 4

    numb_real = rd.randint(1, numb_bullets - 1) # By chance, it's 3
    numb_reals_list = list() # A empty list
    gob(numb_reals_list, True, numb_real) # Put boolean values in the list belove based on the bullet number

    numb_fake = numb_bullets - numb_real # # So it's 1
    numb_fake_list = list() # A empty list
    gob(numb_fake_list, False, numb_fake) # Put boolean values in the list belove based on the bullet number

    gun_order = rd.sample(numb_reals_list + numb_fake_list, k=len(numb_reals_list + numb_fake_list)) # Create a list containing the
    # boolean values from the list of real and false bullets and shuffle the list.
    
    # Math: Rounds
    while not bullet_turn == len(gun_order):

        print(f"Guns loadeds! There's {numb_real} real bullets {numb_fake} fake bullets.")
        print(f'The round {current_round} has started! ',end='')

        # Match: Player's turn
        # Match: Checking the valid choice
        while player_turn == True:

            print(f"It's your turn. Make your choice!\n")
            sleep(3)
            print(f"Player's: {hp_player}")
            print(f"Enemy's HP: {hp_enemy}\n")
            while True:
                try:
                    player_choice = str(input(f"What will you do?\n>> Shot the enemy [1]\n>> Shot yourself [2]\n>> "))[0]
                    if player_choice in "12":
                        break
                    else:
                        print('Invalid choice! Try again!\n')
                        sleep(2)
                        continue
                except:
                    print('Invalid choice! Try again!\n')
                    sleep(2)
                    continue

            # Match: system of the choices
            if player_choice == "1": # Shot the enemy

                if gun_order[bullet_turn] == True:
                    print('You shot the enemy and the bullet was real!\nThe enemy lost -1 HP.')
                    hp_enemy -= 1
                    del gun_order[bullet_turn]
                    sleep(4)
                    print('Your turn is over!')
                    player_turn = False

                if gun_order[bullet_turn] == False:
                    print("You shot the enemy, but the bullet is fake. Nothing happened.")
                    del gun_order[bullet_turn]
                    sleep(4)
                    print('Your turn is over!')
                    player_turn = False

            if player_choice == "2": # Shot yourself

                if gun_order[bullet_turn] == True:
                    print('You shot yourself and the bullet was real! You lost -1 HP.')
                    hp_player -= 1
                    del gun_order[bullet_turn]
                    print('Your turn is over!')
                    player_turn = False
                
                if gun_order[bullet_turn] == False:
                    print('You shot yourself and the bullet was fake! You got one more turn!')
                    del gun_order[bullet_turn]
                    sleep(1)
        
        while player_turn == False:
            print("It's the brazilian's turn!")
            sleep(2)

