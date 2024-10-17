"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Vertices for a pyramid and a prism
pyramid_vertices = [
    [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1], [0, 0, 1]
]

prism_vertices = [
    [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1], [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]
]

pyramid_edges = [(0,1), (1,2), (2,3), (3,0), (0,4), (1,4), (2,4), (3,4)]
prism_edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]

def draw_pyramid():
    glBegin(GL_TRIANGLES)
    for edge in pyramid_edges:
        for vertex in edge:
            glVertex3fv(pyramid_vertices[vertex])
    glEnd()

def draw_prism():
    glBegin(GL_QUADS)
    for edge in prism_edges:
        for vertex in edge:
            glVertex3fv(prism_vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    shape = 'pyramid'  # Start with pyramid

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_PERIOD:
                    shape = 'prism'
                if event.key == K_COMMA:
                    shape = 'pyramid'

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        if shape == 'pyramid':
            draw_pyramid()
        elif shape == 'prism':
            draw_prism()

        pygame.display.flip()
        pygame.time.wait(10)

main()
"""



import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define vertices for the pyramid and triangular prism
# Pyramid vertices (5 points)
pyramid_vertices = [
    [0, 1, 0],     # Top point (apex)
    [1, -1, 1],    # Base - front right
    [-1, -1, 1],   # Base - front left
    [-1, -1, -1],  # Base - back left
    [1, -1, -1],   # Base - back right
]

# Triangular prism vertices (6 points)
prism_vertices = [
    [0, 1, 0],     # Top point of the front triangle
    [1, -1, 1],    # Base - front right
    [-1, -1, 1],   # Base - front left
    [0, 1, -1],    # Top point of the back triangle
    [1, -1, -1],   # Base - back right
    [-1, -1, -1],  # Base - back left
]

# Faces of the pyramid (4 triangles)
pyramid_faces = [
    (0, 1, 2),  # Front face
    (0, 2, 3),  # Left face
    (0, 3, 4),  # Back face
    (0, 4, 1),  # Right face
    (1, 2, 3, 4)  # Base face
]

# Faces of the triangular prism (2 triangles and 3 parallelograms)
prism_faces = [
    (0, 1, 2),  # Front triangle face
    (3, 4, 5),  # Back triangle face
    (1, 2, 5, 4),  # Right parallelogram face
    (0, 3, 4, 1),  # Front parallelogram face
    (0, 3, 5, 2),  # Left parallelogram face
]

# Colors for the pyramid faces
pyramid_colors = [
    (1, 0, 0),  # Red for front face
    (0, 1, 0),  # Green for left face
    (0, 0, 1),  # Blue for back face
    (1, 1, 0),  # Yellow for right face
    (1, 0.5, 0)  # Orange for base face
]

# Colors for the prism faces
prism_colors = [
    (1, 0, 0),    # Red for front triangle
    (0, 1, 0),    # Green for back triangle
    (0, 0, 1),    # Blue for right parallelogram
    (1, 1, 0),    # Yellow for front parallelogram
    (1, 0.5, 0)   # Orange for left parallelogram
]

# Function to draw the shapes with colors
def draw_shape(vertices, faces, colors):
    for i, face in enumerate(faces):
        glBegin(GL_POLYGON)  # Use GL_POLYGON to accommodate both triangles and quads
        glColor3fv(colors[i])  # Set color for the current face
        for vertex in face:
            glVertex3fv(vertices[vertex])
        glEnd()

# Initialize Pygame and OpenGL
pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
gluPerspective(45, (800 / 600), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)  # Move back a bit
glEnable(GL_DEPTH_TEST)

# Initial shape is the pyramid
is_pyramid = True

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PERIOD:  # '.' changes to prism
                is_pyramid = False
            elif event.key == pygame.K_COMMA:  # ',' changes to pyramid
                is_pyramid = True

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Rotate the shape slightly for better visualization
    glRotatef(1, 3, 1, 1)

    # Draw the current shape with colors
    if is_pyramid:
        draw_shape(pyramid_vertices, pyramid_faces, pyramid_colors)
    else:
        draw_shape(prism_vertices, prism_faces, prism_colors)

    # Swap buffers to display the shape
    pygame.display.flip()
    pygame.time.wait(10)

# Quit Pygame
pygame.quit()

