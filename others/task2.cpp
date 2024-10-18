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

