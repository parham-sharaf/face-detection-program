import cv2 as cv
import numpy as np
print(cv.__version__)

cam = cv.VideoCapture(0)
square_ctr = np.zeros((480, 640, 1), np.uint8)
half = np.zeros((480, 640, 1), np.uint8)

square_ctr[190:290, 270:370] = [255]
half[0:480, 0:320] = [255]
and_bitwise = cv.bitwise_or(square_ctr, half)

while True:

    ret, frame = cam.read()

    frame = cv.bitwise_or(frame, frame, mask=half)

    cv.imshow('Camera', frame)
    cv.imshow('Square Center', square_ctr)
    cv.imshow('Half and Half', half)
    cv.imshow('Bitwise and', and_bitwise)
    # cv.imshow('masked image', masked)

    cv.moveWindow('Camera', 0, 0)
    cv.moveWindow('Square Center', 800, 0)
    cv.moveWindow('Half and Half', 0, 800)
    cv.moveWindow('Bitwise and', 800, 800)
    # cv.moveWindow('masked image', 800, 1600)

    print(f'{frame.shape[0]}, {frame.shape[1]}')
    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()