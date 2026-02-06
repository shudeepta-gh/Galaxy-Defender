
w_width,w_height=1000,800
def draw_environment():
    world_size=2000
    half_world=world_size/2
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(1,1,1)

    for i in range(100):
        base_x=(i*1239)%world_size
        base_y=(i*3921)%world_size
        base_z=(i*8743)%world_size
        x=ship_pos[0]+((base_x-ship_pos[0])%world_size)-half_world
        y=ship_pos[1]+((base_y-ship_pos[1])%world_size)-half_world
        z=ship_pos[2]+((base_z-ship_pos[2])%world_size)-half_world
        glVertex3f(x, y, z)
    glEnd()
    glPushMatrix()
    glTranslatef(0,-600,-300)
    glColor3f(0.1,0.4,0.85)
    glutSolidSphere(400,50,50)
    glColor3f(0.2,0.7,0.3)
    glPushMatrix()
    glTranslatef(-120,50,330)
    glScalef(1.2,1.5,1.0)
    glutSolidSphere(110,30,30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(180,-100,300)
    glutSolidSphere(80,30,30)
    glPopMatrix()
    glColor3f(1.0,1.0,1.0)
    glPushMatrix()
    glTranslatef(50,150,355)
    glScalef(2.0,0.6,1.0)
    glutSolidSphere(50,20,20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-50,-200,340)
    glScalef(1.5,0.5,1.0)
    glutSolidSphere(40,20,20)
    glPopMatrix()

    glPopMatrix()



def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    update_camera_view()
    draw_world_objects()
    draw_hud()
    glutSwapBuffers()

def idle():
    global last_time,frame_delay
    current_time=time.time()
    elapsed=current_time-last_time
    if elapsed>=frame_delay:
        update_logic()
        glutPostRedisplay()
        last_time=current_time

def init():
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(fovY,w_width/w_height,1,2000)
    glMatrixMode(GL_MODELVIEW)

def main():
    global last_time
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(w_width,w_height)
    glutCreateWindow(b"Galaxy Defender")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboardListener)
    glutKeyboardUpFunc(keyboardUpListener)
    glutSpecialFunc(specialListener)
    glutMouseFunc(mouseListener)
    last_time=time.time()
    glutMainLoop()

if __name__=="__main__":
    main()
