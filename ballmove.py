def ballmove():
    #None of the below code will work until we replace GM functions with actual code
    hsp = direction * movespeed
    vsp += grav
    #Horizontal collision & movement
    if place_meeting(x + hsp, y, obj_wall):
        while not place_meeting(x + sign(hsp), y, obj_wall):
            x += sign(hsp)
        hsp = 0
        direction *= -1
    x += hsp
    #Vertical collision & movement
    if place_meeting(x, y + vsp, obj_wall):
        while not place_meeting(x, y + sign(vsp), obj_wall):
            y += sign(vsp)
        vsp = 0
        if fearofheights and not position_meeting(x + (sprite_width / 2) * direction, y + (sprite_height / 2) + 1, obj_wall):
            dir *= -1
    y += vsp
    #Enemy collision
    if place_meeting(x, y, obj_player):
        if obj_player.y < y - 20:
            with(obj_player):
                vsp = -jumpspeed
            instance_destroy()
        else:
            game_restart()
