
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Variables to manage the object and camera
show_pyramid = True  # Start with pyramid visible
object_rotation = 0.0
cam_x, cam_y, cam_z = 0.0, 0.0, 5.0
cam_yaw, cam_pitch = 0.0, 0.0
pitch_limit = 1.5
rotation_increment = 0.1

# Function to draw the pyramid with different colored sides
def draw_pyramid():
    glBegin(GL_TRIANGLES)
    # Front face (red)
    glColor3f(1, 0, 0)
    glVertex3f(0.0, 2.0, 0.0)  
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 1.0)

    # Right face (green)
    glColor3f(0, 1, 0)
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, -1.0)

    # Back face (blue)
    glColor3f(0, 0, 1)
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    # Left face (yellow)
    glColor3f(1, 1, 0)
    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, 1.0)
    glEnd()

    # Draw base of the pyramid
    glBegin(GL_QUADS)
    glColor3f(1, 0, 1)
    glVertex3f(-1.0, 0.0, 1.0)
    glColor3f(0, 1, 1)
    glVertex3f(1.0, 0.0, 1.0)
    glColor3f(1, 1, 0)
    glVertex3f(1.0, 0.0, -1.0)
    glColor3f(0, 1, 0)
    glVertex3f(-1.0, 0.0, -1.0)
    glEnd()

# Function to draw the triangular prism as a parallelogram
def draw_prism():
    # Base Triangle 1
    glBegin(GL_QUADS)
    glColor3f(0, 0, 1)  # Blue color
    glVertex3f(-1.5, -0.5, 1.5)  
    glVertex3f(1.5, -0.5, 1.5)
    glVertex3f(0.5, 1.5, 1.5)
    glVertex3f(-0.5, 1.5, 1.5)
    glEnd()

    # Base Triangle 2 (back face)
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)  # Red color
    glVertex3f(-1.5, -0.5, -1.5)
    glVertex3f(1.5, -0.5, -1.5)
    glVertex3f(0.5, 1.5, -1.5)
    glVertex3f(-0.5, 1.5, -1.5)
    glEnd()

    # Side 1: Connect left edges of both triangles
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)  # Green color
    glVertex3f(-1.5, -0.5, 1.5)
    glVertex3f(-1.5, -0.5, -1.5)
    glVertex3f(-0.5, 1.5, -1.5)
    glVertex3f(-0.5, 1.5, 1.5)
    glEnd()

    # Side 2: Connect right edges of both triangles
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)  # Yellow color
    glVertex3f(1.5, -0.5, 1.5)
    glVertex3f(1.5, -0.5, -1.5)
    glVertex3f(0.5, 1.5, -1.5)
    glVertex3f(0.5, 1.5, 1.5)
    glEnd()

    # Side 3: Connect bottom edges of both triangles
    glBegin(GL_QUADS)
    glColor3f(1, 0, 1)  # Magenta color
    glVertex3f(-1.5, -0.5, 1.5)
    glVertex3f(1.5, -0.5, 1.5)
    glVertex3f(1.5, -0.5, -1.5)
    glVertex3f(-1.5, -0.5, -1.5)
    glEnd()

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera setup
    gluLookAt(cam_x, cam_y, cam_z,
              cam_x + math.sin(cam_yaw) * math.cos(cam_pitch),
              cam_y + math.sin(cam_pitch),
              cam_z - math.cos(cam_yaw) * math.cos(cam_pitch),
              0.0, 1.0, 0.0)

    glRotatef(object_rotation, 0.0, 1.0, 0.0)

    if show_pyramid:
        draw_pyramid()
    else:
        draw_prism()

    pygame.display.flip()

# Initialize the OpenGL settings
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1.0, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

# Handle keyboard input
def keyboard(event):
    global object_rotation, show_pyramid
    if event.key == pygame.K_a:
        object_rotation += 5.0
    elif event.key == pygame.K_d:
        object_rotation -= 5.0
    elif event.key == pygame.K_PERIOD:  # '.' key
        show_pyramid = True
    elif event.key == pygame.K_COMMA:  # ',' key
        show_pyramid = False

# Handle special input for camera control
def special_input(key):
    global cam_x, cam_y, cam_pitch, cam_yaw
    if key == K_LEFT:
        cam_x -= 0.1
    elif key == K_RIGHT:
        cam_x += 0.1
    elif key == K_UP:
        cam_y += 0.1
    elif key == K_DOWN:
        cam_y -= 0.1
    elif key == K_5:  # Pitch up when 5 is pressed
        cam_pitch += rotation_increment
    elif key == K_6:  # Pitch down when 6 is pressed
        cam_pitch -= rotation_increment
    elif key == K_7:  # Yaw left when 7 is pressed
        cam_yaw -= rotation_increment
    elif key == K_8:  # Yaw right when 8 is pressed
        cam_yaw += rotation_increment

    # Clamp camera pitch
    if cam_pitch > pitch_limit:
        cam_pitch = pitch_limit
    if cam_pitch < -pitch_limit:
        cam_pitch = -pitch_limit

# Main program
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)
    init()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keyboard(event)
            elif event.type == pygame.KEYUP:
                special_input(event.key)

        display()
        clock.tick(60)

    pygame.quit()

