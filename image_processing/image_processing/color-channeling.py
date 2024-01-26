import cv2 as cv
import numpy as np
print(cv.__version__)

dispW = 640
dispH = 480
flip = 2

cam = cv.VideoCapture(0)

blank = np.zeros([dispH, dispW, 1], np.uint8)
blank[:] = 0

while True:
    # pyautogui.moveTo(1000, 1000)

    ret, frame = cam.read()
    # frame = cv.resize(frame, (10, 10))
    b, g, r = cv.split(frame)

    # print(r)
    # print('\n\n\n')

    # blue = cv.merge((b, blank, blank))
    # green = cv.merge((blank, g, blank))
    # red = cv.merge((blank, g, r))

    # r[:] = r[:] * 2
    # merged = cv.merge((r, b, g))
    # frame = cv.resize(frame, (dispW, dispH))

    # cv.imshow('Camera', frame)
    cv.imshow('red', r)
    # cv.imshow('green', green)
    # cv.imshow('blue', blue)
    # cv.imshow('merged', merged)

    # cv.moveWindow('Camera', 0, 0)
    # cv.moveWindow('red', 700, 0)
    # cv.moveWindow('green', 0, 700)
    # cv.moveWindow('blue', 700, 700)
    # cv.moveWindow('merged', 1400, 700)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()