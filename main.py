import random as rd
from time import sleep
from rules import rules_show
from title import title, line
from generation_orders_bullets import gen_order_bullets as gob
from enemy_choice import enemy
# game's verssion: 1.0

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
hp_player = 1
hp_enemy = 1
bullets_left = True
while hp_player > 0 and hp_enemy > 0:

    current_round = 1
    player_turn = True

    # Match: generation of bullets
    numb_bullets = rd.randint(2, 4) # Ex: By chance is 4 

    numb_real = rd.randint(1, numb_bullets - 1) # By chance, it's 3
    real_list = list() # A empty list
    gob(real_list, True, numb_real) # Put boolean values in the list belove based on the bullet number

    numb_fake = numb_bullets - numb_real # # So it's 1
    numb_fake_list = list() # A empty list
    gob(numb_fake_list, False, numb_fake) # Put boolean values in the list belove based on the bullet number

    gun_order_gen = rd.sample(real_list + numb_fake_list, k=len(real_list + numb_fake_list)) # Create a list containing the
    # boolean values from the list of real and false bullets and shuffle the list.
    gun_order = gun_order_gen # [True , true, false, false]

    print(f"Gun loaded! There's {numb_real} real bullets {numb_fake} fake bullets.")
    print(f'The round {current_round} has started! ',end='')

    # Math: Rounds
    while bullets_left:
        # Match: Player's turn

        # Match: Checking the valid choice
        while player_turn == True:

            if len(gun_order) <= 0:
                bullets_left = False
                break

            if hp_player <= 0 or hp_enemy <= 0:
                bullets_left = False
                break

            print(f"It's your turn. Make your choice!\n")
            sleep(3)
            line(100)
            print(f"Player's: {hp_player}")
            print(f"Enemy's HP: {hp_enemy}")
            line(100)
            while True:
                try:
                    player_choice = str(input(f"What will you do?\n>> Shoot the enemy [1]\n>> Shoot yourself [2]\n>> "))[0]
                    line(80)
                    if player_choice in "12":
                        break
                    else:
                        print('Invalid choice! Try again!\n')
                        line(100)
                        sleep(2)
                        continue
                except:
                    print('Invalid choice! Try again!\n')
                    line(100)
                    sleep(2)
                    continue

            # Match: system of the choices
            if player_choice == "1": # Shot the enemy

                if gun_order[0] == True:
                    print('You shoot the enemy and the bullet was real!\nThe enemy lost -1 HP.')
                    hp_enemy -= 1
                    del gun_order[0]
                    print('Your turn is over!')
                    line(100)
                    player_turn = False
                    sleep(5)
                    break

                if gun_order[0] == False:
                    print("You shoot the enemy, but the bullet is fake.\nNothing happened.")
                    del gun_order[0]
                    print('Your turn is over!')
                    line(100)
                    player_turn = False
                    sleep(5)
                    break

            if player_choice == "2": # Shot yourself

                if gun_order[0] == True:
                    print('You shoot yourself and the bullet was real! You lost -1 HP.')
                    sleep(1)
                    hp_player -= 1
                    del gun_order[0]
                    print('Your turn is over!')
                    line(100)
                    player_turn = False
                    sleep(5)
                    break

                if gun_order[0] == False:
                    print('You shoot yourself and the bullet was fake! You got one more turn!')
                    del gun_order[0]
                    line(100)
                    sleep(5)
                    break
            
        while player_turn == False:

            if len(gun_order) <= 0:
                bullets_left = False
                break

            if hp_player <= 0 or hp_enemy <= 0:
                bullets_left = False
                break

            print("It's the brazilian's turn!")
            sleep(2)
            print("He is thinking about what he's gonna do...\n")
            line(100)
            sleep(5)

            if enemy(gun_order, hp_player, hp_enemy) == 1: # Shoot to player

                if gun_order[0] == True:
                    print('He shoot to you and the bullet was real!')
                    sleep(1)
                    print('You lost -1 HP!')
                    hp_player -= 1
                    print('His turn is over!')
                    line(100)
                    sleep(3)
                    del gun_order[0]
                    player_turn = True
                    break

                if gun_order[0] == False:
                    print('He shoot to you and the bullet was fake. Nothing happened.\n')
                    line(100)
                    sleep(3)
                    del gun_order[0]
                    player_turn = True
                    break
                    

            if enemy(gun_order, hp_player, hp_enemy) == 2: # Shoot to himself

                if gun_order[0] == True:
                    print('He shoot to himself and the bullet was real! He lost -1 HP.')
                    hp_enemy -= 1
                    del gun_order[0]
                    print('His turn is over!')
                    line(100)
                    sleep(3)
                    player_turn = True
                    break
                    

                if gun_order[0] == False:
                    print('He shoot to himself and the bullet was fake! He got one more turn.')
                    line(100)
                    sleep(3)
                    del gun_order[0]
                    break

        if hp_player <= 0 or hp_enemy <= 0:
            bullets_left = False
            break

        if not bullets_left:
            break

if hp_enemy == 0:
    title(f"WINNER: PLAYER!")
    sleep(1)
    print('You almost lost your mind!\nBut you got the coffee and couscous package.')
else:
    title(f"YOU ARE DEAD!")
    sleep(1)
    print('You wasted your life for food! How you are pathetic!')

