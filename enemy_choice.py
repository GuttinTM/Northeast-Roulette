from random import choice

def enemy(gun_order, hp_player, hp_enemy):
    choices = (1, 2)
    num_real = 0
    num_fake = 0
    random_choice = choice([1, 2])

    for i, v in enumerate(gun_order):
        if gun_order[i] == True:
            num_real += 1
        else:
            num_fake += 1

    if num_real - num_fake == 1:
        if len(gun_order) == 1:
            return choices[0]
        if hp_player < hp_enemy:
            return choices[1]
        elif hp_player > hp_enemy:
            return choices[0]
        else:
            return random_choice
    
    if num_real - num_fake >= 2:
        return choices[0]
    
    if num_real == num_fake:
        if hp_player > hp_enemy:
            return choices[0]
        elif hp_player < hp_enemy:
            return choices[1]
        else:
            return choices[1]
        
    if num_fake - num_real >= 1:
        return choices[1]
