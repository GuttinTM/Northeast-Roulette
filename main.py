import random as rd
from time import sleep
from rules import rules_show
from tittle import tittle
from generation_orders_bullets import gen_order_bullet as gob

# Game's Tittle
tittle('NORTHEAST ROULETTE')

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
tittle('MACH STARTED')

# The match
hp_player = 5
hp_enemy = 5
round = 1
player_turn = True
while not hp_player == 0 or hp_enemy == 0:

    # Match: generation of bullets
    numb_bullets = rd.randint(2, 6) # Ex: By chance is 4

    numb_reals = rd.randint(1, numb_bullets - 1) # By chance, it's 3
    numb_reals_list = list() # A empty list
    gob(numb_reals_list, True) # Put boolean values in the list belove based on the bullet number

    numb_fake = numb_bullets - numb_reals # # So it's 1
    numb_fake_list = list() # A empty list
    gob(numb_fake_list, False) # Put boolean values in the list belove based on the bullet number

    bullets_list = rd.sample(numb_reals_list + numb_fake_list, k=len(numb_reals_list + numb_fake_list)) # Create a list containing the
    # boolean values from the list of real and false bullets and shuffle the list.

    print(f'The round {round} has started! ',end='')

    # Match: Player's turn
    if player_turn == True:
        print(f"It's your turn. Make your choice!")
        sleep(3)
        while True:
            try:
                player_choice = str(input('What will you do?\n>> Shot the enemy [1]\n>> Shot yourself [2]\n>>'))[0]
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
                
