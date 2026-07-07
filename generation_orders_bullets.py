def gen_order_bullets(list_bullet, bool, numb ):

    if bool == True:
        for bullet in range(0, numb):
            list_bullet.append(True)
        return list_bullet
    
    else:
        for bullet in range(0, numb):
            list_bullet.append(False)
        return list_bullet
