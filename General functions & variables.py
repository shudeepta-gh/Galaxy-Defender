from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

last_time = 0
tar_fps = 60
frame_delay = 1.0/tar_fps

w_width,w_height=1000,800
fovY = 60
frame_count=0
ammo=100
powerups=[]

score=0
lives=50
game_over=False
cheat_mode=False


ship_pos=[0,0,0]
ship_vel=[0,0,0]
ship_speed=2.0
max_tilt_angle=0.0

rem_flare=3
boost_heat=0.0
max_boost_heat=100.0
is_boosting=False
boost_cooldown=False


camera_distance=60
camera_angle_h=0
camera_height=20
camera_mode=0


spaceship_bullets=[]
enemies=[]
red_missiles=[]
flares=[]
particles=[]
grey_asteroids=[]
enemy_blue_missiles=[]

black_hole_active=False
black_hole_pos=[0,0,-800]
black_hole_timer=0

spaceship_x=0.0
spaceship_z=0.0
first_person_mode=False

keys={}


def vector_sub(v1,v2):
    return [v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]]

def normalize(v):
    mag = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    if mag == 0:
        return [0,0,0]
    return [v[0]/mag,v[1]/mag,v[2]/mag]

def check_collision(pos1, r1, pos2, r2):
    dist=math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2+(pos1[2]-pos2[2])**2)
    return dist<(r1+r2)

def get_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def cross_product(a,b):
    return [
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0]
    ]


def draw_world_objects():
    global camera_mode,enemies
    draw_environment()
    draw_black_hole()
    if camera_mode==0:
        draw_ship()
    for e in enemies:
        draw_enemy(e)
    draw_grey_asteroids()
    draw_projectiles()
    draw_powerups()
