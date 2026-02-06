
def update_enemy_projectiles():
  global enemy_blue_missiles,red_missiles,flares,lives,game_over,ship_pos
  for m in red_missiles:
    for f in flares:
             if check_collision(m['pos'],4,f['pos'],5):
                 if m in red_missiles:
                    red_missiles.remove(m)
  
def update_flares():
    global flares
    for f in flares:
        f['timer']-=1
    alives_flares=[]
    for f in flares:
        if f['timer']>0:
            alives_flares.append(f)
    flares[:]=alives_flares
