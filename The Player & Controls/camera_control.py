
def update_camera_view():
    global camera_mode,ship_pos,camera_angle_h,camera_height,camera_distance
    global cheat_mode,enemies
    look_x=math.sin(camera_angle_h)
    look_z=math.cos(camera_angle_h)
    if camera_mode==1:
        eye_x=ship_pos[0]
        eye_y=ship_pos[1]+0.5
        eye_z=ship_pos[2]
        target_x=eye_x-(look_x*100)
        target_z=eye_z-(look_z*100)
        target_y=eye_y+(camera_height-20)
        gluLookAt(eye_x,eye_y,eye_z,target_x,target_y,target_z,0,1,0)


    else:
        cam_x=ship_pos[0]+look_x*camera_distance
        cam_z=ship_pos[2]+look_z*camera_distance
        cam_y=ship_pos[1]+camera_height
        gluLookAt(cam_x,cam_y,cam_z,ship_pos[0],ship_pos[1],ship_pos[2],0,1,0)
