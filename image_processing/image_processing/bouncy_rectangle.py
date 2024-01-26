import cv2 as cv
print(cv.__version__)
dispW = 640
dispH = 480
flip = 2

x = y = 0
x_inc = y_inc = 0

speed = 2

rect = (160, 140)

color = (0, 0, 255)

cam = cv.VideoCapture(0)


while True:
    ret, frame = cam.read()

    x = x + x_inc
    y = y + y_inc

    if x <= 0:
         x_inc = speed
    elif x + rect[0] >= frame.shape[1]:
        x_inc = -speed

    if y <= 0:
        y_inc = speed
    elif y + rect[1] >= frame.shape[0]:
        y_inc = -speed

    print (f'x: {x}, y: {y}')
    # frame = cv.resize(frame, (dispW, dispH))
    frame = cv.rectangle(frame, (x, y), (rect[0] + x,  rect[1] + y), color, 2)

    roi = frame[y: rect[1] + y, x: rect[0] + x].copy()
    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    roi = cv.cvtColor(roi, cv.COLOR_GRAY2BGR)
    frame[y: rect[1] + y, x: rect[0] + x] = roi

    cv.imshow('Camera', frame)
    cv.moveWindow('Camera', 200, 200)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
