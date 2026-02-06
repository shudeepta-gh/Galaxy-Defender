
def handle_shooting(x, y):
    global ammo,cheat_mode,spaceship_bullets,ship_pos

    if ammo>0 or cheat_mode:
        shoot_dir=calculate_aim_vector(x, y)

        bullet_speed=25.0
        velocity=[shoot_dir[0]*bullet_speed,shoot_dir[1]*bullet_speed,shoot_dir[2]*bullet_speed]
        spaceship_bullets.append({'pos': list(ship_pos), 'vel': velocity})
        if not cheat_mode:
            ammo-=1
    else:
        print("Out of Ammo! Destroy enemies to collect powerups.")

def calculate_aim_vector(x,y):
    global camera_mode,ship_pos,camera_angle_h,camera_distance,camera_height,w_width,w_height,fovY

    look_x=math.sin(camera_angle_h)
    look_z=math.cos(camera_angle_h)
    cam_pos=[]
    f_vec=[]
    if camera_mode==0:
        cam_x=ship_pos[0]+look_x*camera_distance
        cam_z=ship_pos[2]+look_z*camera_distance
        cam_y=ship_pos[1]+camera_height
        cam_pos=[cam_x,cam_y,cam_z]
        f_vec=normalize(vector_sub(ship_pos, cam_pos))
    else:
        cam_pos=[ship_pos[0],ship_pos[1]+0.5,ship_pos[2]]
        target_y=(camera_height-20)
        dir_vec=[-look_x*100,target_y,-look_z*100]
        f_vec=normalize(dir_vec)
    world_up=[0,1,0]
    r_vec=normalize(cross_product(f_vec,world_up))
    u_vec=normalize(cross_product(r_vec,f_vec))

    fov_rad=math.radians(fovY)
    tan_fov=math.tan(fov_rad / 2.0)
    aspect=w_width/w_height

    nx=(2.0*x/w_width)-1.0
    ny=1.0-(2.0*y/w_height)
    dx=nx*aspect*tan_fov
    dy=ny*tan_fov
    ray_x=f_vec[0]+r_vec[0]*dx+u_vec[0]*dy
    ray_y=f_vec[1]+r_vec[1]*dx+u_vec[1]*dy
    ray_z=f_vec[2]+r_vec[2]*dx+u_vec[2]*dy
    ray_dir=normalize([ray_x,ray_y,ray_z])
    aim_distance=2000
    target_point=[cam_pos[0]+ray_dir[0]*aim_distance,cam_pos[1]+ray_dir[1]*aim_distance,cam_pos[2]+ray_dir[2]*aim_distance]
    shoot_vec=vector_sub(target_point,ship_pos)
    return normalize(shoot_vec)
