import random as rd
from time import sleep
from rules import rules_show
from tittle import tittle

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
while not hp_player == 0 or hp_enemy == 0:
    numb_bullets = rd.randint(2, 6)
    numb_reals = rd.randint(1, numb_bullets - 1)
    numb_fake = numb_bullets - numb_reals
    print(numb_bullets, numb_reals, numb_fake)
    sleep(5)