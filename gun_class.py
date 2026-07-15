import random as rd
from generation_orders_bullets import gen_order_bullets as gob

class Gun:
    def __init__(self):
        self.numb_bullets = rd.randint(2, 8) # Ex: By chance is 4

        self.numb_lives = rd.randint(1, self.numb_bullets - 1) # By chance, it's 3
        self.lives_list = [] # A empty list
        gob(self.lives_list, True, self.numb_lives) # Put boolean values in the list belove based on the bullet number

        self.numb_blanks = self.numb_bullets - self.numb_lives # So it's 1
        self.blanks_list = [] # A empty list
        gob(self.blanks_list, False, self.numb_blanks) # Put boolean values in the list belove based on the bullet number

        self.gun_order_gen = rd.sample(self.lives_list + self.blanks_list, k=len(self.lives_list + self.blanks_list))
        # Create a list containing the boolean values from the list of live and false bullets and shuffle the list.

        self.gun_order = self.gun_order_gen




        