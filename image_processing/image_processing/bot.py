import time

import cv2 as cv
import numpy as np
import pyautogui

print(cv.__version__)


def nothing():
    pass


dispW = 640
dispH = 480

rect = (dispW, dispH)

cam = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('/home/parham/Dev/Projects/aimbot/image_processing/cascade/faces.xml')

while True:

    # frame = cv.imread("/home/parham/Dev/Projects/aimbot/image_processing/Photos/smarties.png", cv.IMREAD_UNCHANGED)
    image = pyautogui.screenshot()
    image = cv.cvtColor(np.array(image),
                         cv.COLOR_RGB2BGR)
    # ret, image = cam.read()

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 2)
    print(faces, '\n')
    face = sorted(faces, key=lambda rect: rect[2] * rect[3], reverse=True)
    print(face)

    if not len(face) == 0:
        for (x, y, w, h) in faces:
        # (x, y, w, h) = face[0]
        #     cv.line(image, (int(x + w / 2), 0), (int(x + w / 2), dispH), (0, 255, 0), 3)
        #     cv.line(image, (0, int(y + h / 2)), (dispW, int(y + h / 2)), (0, 255, 0), 3)
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # pyautogui.moveTo(int(x + w / 2), int(y + h / 2))
        # pyautogui.click(int(x + w / 2), int(y + h / 2))

    image = cv.resize(image, rect)
    cv.imshow('image', image)
    cv.moveWindow('image', 1400, 0)
    # cv.imshow('something', gray)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()