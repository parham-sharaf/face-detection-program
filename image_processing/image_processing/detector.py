import cv2 as cv
#
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
    ret, frame = cam.read()

    x = x + x_inc
    y = y + y_inc

    if x <= 0:
         x_inc = 10
    elif x + rect[0] >= frame.shape[1]:
        x_inc = -10

    if y <= 0:
        y_inc = 10
    elif y + rect[1] >= frame.shape[0]:
        y_inc = -10

    print (f'x: {x}, y: {y}')
    # frame = cv.resize(frame, (dispW, dispH))
    frame = cv.rectangle(frame, (0 + x, 0 + y), (rect[0] + x,  rect[1] + y), color, 2)

    cv.imshow('Camera', frame)
    cv.moveWindow('Camera', 200, 200)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()