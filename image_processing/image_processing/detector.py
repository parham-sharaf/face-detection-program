import cv2 as cv
import pyautogui

# # img = cv.imread("Photos/Jett-Feature-1.jpg", cv.IMREAD_UNCHANGED)
# img = cv.imread("Photos/Jett-gun.jpeg", cv.IMREAD_UNCHANGED)
# scale = 60
#
# width = int(img.shape[1] * scale / 100)
# length = int(img.shape[0] * scale / 100)
# dim = (width, length)
#
# resized_img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
#
# gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
#
# haar_cascade = cv.CascadeClassifier('haar_face.xml')
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
#
# print(f'Number of faces found = {len(faces_rect)}')
#
# for (x, y, w, h) in faces_rect:
#     cv.rectangle(resized_img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)
#
# cv.imshow('Jett', resized_img)
# cv.waitKey(0)
# cv.destroy

import cv2 as cv
print(cv.__version__)

dispW = 640
dispH = 480
flip = 2

x = y = 0
x_inc = y_inc = -2

rect = (60, 40)

color = (0, 0, 255)

cam = cv.VideoCapture(0)


while True:
    # pyautogui.moveTo(1000, 1000)

    ret, frame = cam.read()
    roi = frame[240: 380, 240: 380].copy()
    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    roi = cv.cvtColor(roi, cv.COLOR_GRAY2BGR)
    frame[240: 380, 240: 380] = roi


    # frame = cv.resize(frame, (dispW, dispH))

    cv.imshow('Camera', frame)
    cv.imshow('Region of interest', roi)
    cv.moveWindow('Camera', 200, 200)
    cv.moveWindow('Region of interest', 1500, 0)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()