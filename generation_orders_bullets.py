def gen_order_bullets(list_bullet, valor):
    list_bullet = list()
    
    if valor == True:
        for bullet in range(0, len(list_bullet)):
            list_bullet.append(True)
        return list_bullet
    
    else:
        for bullet in range(0, len(list_bullet)):
            list_bullet.append(False)
        return list_bullet