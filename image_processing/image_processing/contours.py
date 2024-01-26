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


cv.createTrackbar('hue_lower_right', 'Trackbars', 0, 179, nothing)
cv.createTrackbar('hue_upper_right', 'Trackbars', 5, 179, nothing)

cv.createTrackbar('hue_lower_left', 'Trackbars', 154, 179, nothing)
cv.createTrackbar('hue_upper_left', 'Trackbars', 179, 179, nothing)

cv.createTrackbar('sat_lower', 'Trackbars', 212, 255, nothing)
cv.createTrackbar('sat_upper', 'Trackbars', 255, 255, nothing)
cv.createTrackbar('val_lower', 'Trackbars', 83, 255, nothing)
cv.createTrackbar('val_upper', 'Trackbars', 255, 255, nothing)

while True:
    # pyautogui.moveTo(1000, 1000)

    # frame = cv.imread("/home/parham/Dev/Projects/aimbot/image_processing/Photos/smarties.png", cv.IMREAD_UNCHANGED)
    ret, frame = cam.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    hue_lower_right = cv.getTrackbarPos('hue_lower_right', 'Trackbars')
    hue_upper_right = cv.getTrackbarPos('hue_upper_right', 'Trackbars')

    hue_lower_left = cv.getTrackbarPos('hue_lower_left', 'Trackbars')
    hue_upper_left = cv.getTrackbarPos('hue_upper_left', 'Trackbars')

    sat_lower = cv.getTrackbarPos('sat_lower', 'Trackbars')
    sat_upper = cv.getTrackbarPos('sat_upper', 'Trackbars')

    val_lower = cv.getTrackbarPos('val_lower', 'Trackbars')
    val_upper = cv.getTrackbarPos('val_upper', 'Trackbars')

    lower_bound_right = np.array([hue_lower_right, sat_lower, val_lower])
    upper_bound_right = np.array([hue_upper_right, sat_upper, val_upper])

    lower_bound_left = np.array([hue_lower_left, sat_lower, val_lower])
    upper_bound_left = np.array([hue_upper_left, sat_upper, val_upper])

    foreground_mask_right = cv.inRange(hsv, lower_bound_right, upper_bound_right)
    foreground_mask_left = cv.inRange(hsv, lower_bound_left, upper_bound_left)

    foreground_mask_comp = cv.add(foreground_mask_right, foreground_mask_left)

    cv.imshow('foreground_mask', foreground_mask_comp)
    cv.moveWindow('foreground_mask', 700, 0)

    contours, _ = cv.findContours(foreground_mask_comp, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)
    for cnt in contours:
        area = cv.contourArea(cnt)
        (x, y, w, h) = cv.boundingRect(cnt)
        if area >= 100:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0,), 3)
            cv.line(frame, (int(x + w/2), 0), (int(x + w/2), 480), (0, 255, 0), 3)
            cv.line(frame, (0, int(y + h/2)), (640, int(y + h/2)), (0, 255, 0), 3)

    cv.imshow('Camera', frame)
    cv.moveWindow('Camera', 0, 0)

    foreground = cv.bitwise_and(frame, frame, mask=foreground_mask_comp)
    cv.imshow('foreground', foreground)
    cv.moveWindow('foreground', 0, 700)

    background_mask = cv.bitwise_not(foreground_mask_comp)
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