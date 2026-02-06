
def update_player_movement():
    global ship_pos,is_boosting,boost_cooldown,boost_heat,ship_speed
    if is_boosting:
        speed=ship_speed*2.0
   
    else:
        speed=ship_speed

    if keys.get(b'w'):
        ship_pos[2]-=speed
    if keys.get(b's'):
        ship_pos[2]+=speed
    if keys.get(b'a'):
        ship_pos[0]-=speed
    if keys.get(b'd'):
        ship_pos[0]+=speed
    if keys.get(b'q'):
        ship_pos[1]+=speed
    if keys.get(b'e'):
        ship_pos[1]-=speed

    if is_boosting and not boost_cooldown:
        boost_heat += 1.5
        if boost_heat>=max_boost_heat:
            boost_cooldown = True
    else:
        boost_heat = max(0, boost_heat - 0.5)
        if boost_heat == 0: 
            boost_cooldown = False


def keyboardListener(key,x,y):
    global cheat_mode, cheat_vision,rem_flare,is_boosting
    if key==b'r':
        reset_game()
        return
    if key == b'w':
        keys[b'w']=True
    elif key == b's':
        keys[b's']=True
    elif key == b'a':
        keys[b'a']=True
    elif key == b'd':
        keys[b'd']=True
    elif key == b'q':
        keys[b'q']=True
    elif key == b'e':
        keys[b'e']=True

    if key==b'c':
        cheat_mode=not cheat_mode
    if key == b'f' and rem_flare>0:
        flares.append({'pos':list(ship_pos),'timer': 180})
        rem_flare-=1
    if key==b'b':
        if not boost_cooldown:
            is_boosting=True


  
def keyboardUpListener(key,x,y):
    global is_boosting

    if key==b'w':
        keys[b'w']=False
    elif key == b's':
        keys[b's']=False
    elif key == b'a':
        keys[b'a']=False
    elif key == b'd':
        keys[b'd']=False
    elif key == b'q':
        keys[b'q']=False
    elif key == b'e':
        keys[b'e']=False
    if key == b'b':
        is_boosting=False

def specialListener(key, x, y):
    global camera_height,camera_angle_h
    if key==GLUT_KEY_UP:
        camera_height+=2
    if key==GLUT_KEY_DOWN:
        camera_height-=2
    if key==GLUT_KEY_LEFT:
        camera_angle_h-=0.05
    if key==GLUT_KEY_RIGHT:
        camera_angle_h+=0.05

def mouseListener(button,state,x,y):
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        handle_shooting(x,y)
    elif button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
        handle_camera_toggle()
