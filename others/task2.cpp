#include <windows.h>
#include <GL/glut.h>
#include <cmath>

bool showPyramid = false;
float objectRotation = 0.0f;
float camX = 0.0f, camY = 0.0f, camZ = 5.0f;
float camYaw = 0.0f, camPitch = 0.0f;
const float pitchLimit = 1.5f;
const float rotationIncrement = 0.1f;

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();


    gluLookAt(camX, camY, camZ,
              camX + sin(camYaw) * cos(camPitch),
              camY + sin(camPitch),
              camZ - cos(camYaw) * cos(camPitch),
              0.0f, 1.0f, 0.0f);


    glRotatef(objectRotation, 0.0f, 1.0f, 0.0f);

    if (showPyramid) {

        glBegin(GL_TRIANGLES);
        // Front face
        glColor3f(1, 0, 0);
        glVertex3f(0.0, 1.0, 0.0);
        glColor3f(0, 1, 0);
        glVertex3f(-1.0, 0.0, 1.0);
        glColor3f(0, 0, 1);
        glVertex3f(1.0, 0.0, 1.0);
        // Right face
        glColor3f(1, 0, 0);
        glVertex3f(0.0, 1.0, 0.0);
        glColor3f(0, 0, 1);
        glVertex3f(1.0, 0.0, 1.0);
        glColor3f(1, 1, 0);
        glVertex3f(1.0, 0.0, -1.0);

        // Back face
        glColor3f(1, 0, 0);
        glVertex3f(0.0, 1.0, 0.0);
        glColor3f(1, 1, 0);
        glVertex3f(1.0, 0.0, -1.0);
        glColor3f(0, 1, 1);
        glVertex3f(-1.0, 0.0, -1.0);

        // Left face
        glColor3f(1, 0, 0);
        glVertex3f(0.0, 1.0, 0.0);
        glColor3f(0, 1, 1);
        glVertex3f(-1.0, 0.0, -1.0);
        glColor3f(0, 1, 0);
        glVertex3f(-1.0, 0.0, 1.0);
        glEnd();

        // Draw base of the pyramid
        glBegin(GL_QUADS);
        glColor3f(1, 0, 1);
        glVertex3f(-1.0, 0.0, 1.0);
        glColor3f(0, 1, 1);
        glVertex3f(1.0, 0.0, 1.0);
        glColor3f(1, 1, 0);
        glVertex3f(1.0, 0.0, -1.0);
        glColor3f(0, 1, 0);
        glVertex3f(-1.0, 0.0, -1.0);
        glEnd();
    } else {

        // Draw triangular prism

        // Base Triangle 1
        glBegin(GL_TRIANGLES);
        glColor3f(1, 0, 0);
        glVertex3f(-1.0, -0.5, 1.0);
        glVertex3f(1.0, -0.5, 1.0);
        glVertex3f(0.0, 0.5, 1.0);
        glEnd();

        // Base Triangle 2 (back face)
        glBegin(GL_TRIANGLES);
        glColor3f(0, 1, 0);
        glVertex3f(-1.0, -0.5, -1.0);
        glVertex3f(1.0, -0.5, -1.0);
        glVertex3f(0.0, 0.5, -1.0);
        glEnd();

        // Side 1: Connect left edges of both triangles
        glBegin(GL_QUADS);
        glColor3f(0, 0, 1);
        glVertex3f(-1.0, -0.5, 1.0);
        glVertex3f(-1.0, -0.5, -1.0);
        glVertex3f(0.0, 0.5, -1.0);
        glVertex3f(0.0, 0.5, 1.0);
        glEnd();

        // Side 2: Connect right edges of both triangles
        glBegin(GL_QUADS);
        glColor3f(1, 1, 0);
        glVertex3f(1.0, -0.5, 1.0);
        glVertex3f(1.0, -0.5, -1.0);
        glVertex3f(0.0, 0.5, -1.0);
        glVertex3f(0.0, 0.5, 1.0);
        glEnd();

        // Side 3: Connect bottom edges of both triangles
        glBegin(GL_QUADS);
        glColor3f(1, 0, 1);
        glVertex3f(-1.0, -0.5, 1.0);
        glVertex3f(1.0, -0.5, 1.0);
        glVertex3f(1.0, -0.5, -1.0);
        glVertex3f(-1.0, -0.5, -1.0);
        glEnd();
    }

    glutSwapBuffers();
}


