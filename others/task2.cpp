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

void keyboard(unsigned char key, int x, int y) {
    switch (key) {
        case 'a': objectRotation += 5.0f; break;
        case 'd': objectRotation -= 5.0f; break;
        case '.': showPyramid = true; break;
        case ',': showPyramid = false; break;
    }

    glutPostRedisplay();
}

void specialInput(int key, int x, int y) {
    switch (key) {
        case GLUT_KEY_LEFT: camX -= 0.1f; break;
        case GLUT_KEY_RIGHT: camX += 0.1f; break;
        case GLUT_KEY_UP: camY += 0.1f; break;
        case GLUT_KEY_DOWN: camY -= 0.1f; break;
        case 5: camPitch += rotationIncrement; break;
        case 6: camPitch -= rotationIncrement; break;
        case 7: camYaw -= rotationIncrement; break;
        case 8: camYaw += rotationIncrement; break;
    }


    if (camPitch > pitchLimit) camPitch = pitchLimit;
    if (camPitch < -pitchLimit) camPitch = -pitchLimit;

    glutPostRedisplay();
}

void init() {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glEnable(GL_DEPTH_TEST);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, 1.0, 1.0, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Pyramid/Prism");

    init();
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutSpecialFunc(specialInput);
    glutMainLoop();
    return 0;
}

