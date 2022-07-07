import cv2
import cv2 as cv
import numpy as np

print(cv.__version__)


def nothing(x):
    pass


dispW = 640
dispH = 480

cam = cv.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/parham/Dev/Projects/aimbot/image_processing/cascade/faces.xml')

while True:

    # frame = cv.imread("/home/parham/Dev/Projects/aimbot/image_processing/Photos/smarties.png", cv.IMREAD_UNCHANGED)
    ret, frame = cam.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 2)
    for (x, y, w, h) in faces:
        cv.line(frame, (int(x + w / 2), 0), (int(x + w / 2), 480), (0, 255, 0), 3)
        cv.line(frame, (0, int(y + h / 2)), (dispW, int(y + h / 2)), (0, 255, 0), 3)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

    cv.imshow('faces', frame)
    cv.imshow('something', gray)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()