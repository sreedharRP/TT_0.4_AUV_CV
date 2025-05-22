import cv2 as cv

capture = cv.VideoCapture(1)

while True:
    istrue , frame= capture.read()

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()