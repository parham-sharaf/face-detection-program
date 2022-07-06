import cv2 as cv
import numpy as np

print(cv.__version__)

def nothing(x):
    pass

dispW = 640
dispH = 480

cam = cv.VideoCapture(0)

cv.namedWindow('Trackbars')
cv.moveWindow('Trackbars', 1400, 0)


cv.createTrackbar('hue_lower', 'Trackbars', 0, 179, nothing)
cv.createTrackbar('hue_upper', 'Trackbars', 0, 179, nothing)
cv.createTrackbar('sat_lower', 'Trackbars', 0, 255, nothing)
cv.createTrackbar('sat_upper', 'Trackbars', 0, 255, nothing)
cv.createTrackbar('val_lower', 'Trackbars', 0, 255, nothing)
cv.createTrackbar('val_upper', 'Trackbars', 0, 255, nothing)

while True:
    # pyautogui.moveTo(1000, 1000)

    # frame = cv.imread("/home/parham/Dev/Projects/aimbot/image_processing/Photos/smarties.png", cv.IMREAD_UNCHANGED)
    ret, frame = cam.read()

    cv.imshow('Camera', frame)
    cv.moveWindow('Camera', 0, 0)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    hue_lower = cv.getTrackbarPos('hue_lower', 'Trackbars')
    hue_upper = cv.getTrackbarPos('hue_upper', 'Trackbars')

    sat_lower = cv.getTrackbarPos('sat_lower', 'Trackbars')
    sat_upper = cv.getTrackbarPos('sat_upper', 'Trackbars')

    val_lower = cv.getTrackbarPos('val_lower', 'Trackbars')
    val_upper = cv.getTrackbarPos('val_upper', 'Trackbars')

    # print(hue_lower, hue_lower, sat_lower, sat_upper, val_lower, val_upper)

    lower_bound = np.array([hue_lower, sat_lower, val_lower])
    upper_bound = np.array([hue_upper, sat_upper, val_upper])

    print(lower_bound, upper_bound)
    print(hsv)
    foreground_mask = cv.inRange(hsv, lower_bound, upper_bound)

    cv.imshow('foreground_mask', foreground_mask)
    cv.moveWindow('foreground_mask', 700, 0)

    foreground = cv.bitwise_and(frame, frame, mask=foreground_mask)
    cv.imshow('foreground', foreground)
    cv.moveWindow('foreground', 0, 700)

    background_mask = cv.bitwise_not(foreground_mask)
    cv.imshow('background_mask', background_mask)
    cv.moveWindow('background_mask', 700, 700)

    background_mask = cv.cvtColor(background_mask, cv.COLOR_GRAY2BGR)
    final = cv.add(foreground, background_mask)
    cv.imshow('final', final)
    cv.moveWindow('final', 1400, 700)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()