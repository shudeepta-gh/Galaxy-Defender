
def draw_text(x,y,text):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, w_width, 0, w_height)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18,ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw_hud():
    global ammo,score,lives,rem_flare,cheat_mode,black_hole_active,game_over,w_height,w_width
    ammo_text="INF" if cheat_mode else str(ammo)
    info=f"Score: {score} | Lives: {lives} | Ammo: {ammo_text} | Flares: {rem_flare}"
    if cheat_mode:
        info+=" | [CHEAT: AUTO-AIM]"
    if black_hole_active:
        info+=" | ALERT - BLACK HOLE!"


    boost_text = f"Engine Heat: {int(boost_heat)} / {max_boost_heat}"
    info += f" | {boost_text}"

    
    draw_text(10,w_height-30,info)
    if game_over:
        draw_text(w_width//2-50,w_height//2,"GAME OVER")
