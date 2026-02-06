
def reset_game():
    global score,lives,game_over,ship_pos,max_tilt_angle,rem_flare,boost_heat,is_boosting,boost_cooldown,spaceship_bullets,enemies,red_missiles,flares,particles,grey_asteroids,enemy_blue_missiles,black_hole_active,black_hole_timer,camera_angle_h,camera_height,ammo,powerups

    score=0
    lives=50
    game_over=False
    ship_pos=[0,0,0]
    max_tilt_angle=0.0
    rem_flare=3
    boost_heat=0.0
    is_boosting=False
    boost_cooldown=False

    camera_angle_h=0
    camera_height=20

    spaceship_bullets.clear()
    enemies.clear()
    enemy_blue_missiles.clear()
    red_missiles.clear()
    flares.clear()
    particles.clear()
    grey_asteroids.clear()

    black_hole_active = False
    black_hole_timer = 0

    ammo=100
    powerups.clear()

    print("Game Restarted!")
