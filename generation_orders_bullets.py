def gen_order_bullets(list_bullet, is_real, numb ):

    if is_real:
        for bullet in range(0, numb):
            list_bullet.append(True)
    
    else:
        for bullet in range(0, numb):
            list_bullet.append(False)
