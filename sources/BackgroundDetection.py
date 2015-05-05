import cv2
import numpy as np

# cap = cv2.VideoCapture('1.avi')
# width  = cap.get(3)
# height = cap.get(4)

# fgbg = cv2.BackgroundSubtractorMOG()
# # sum = zeros()
# for k in range(1):
#     ret, frame = cap.read()
#     print frame
# # sum = frame
# # background = cv2.divide(1,sum)
# # print background
# # cv2.imshow('background', background)
# cv2.waitKey(0)

# cap.release()

cap = cv2.VideoCapture('1.avi')

fgbg = cv2.BackgroundSubtractorMOG()
ret, frame = cap.read()

for k in range(500):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame, learningRate = 0.001)
    cv2.imshow('frame',fgmask)
    cv2.waitKey(1)
print 'Completed Once.'
cap.release()

cap = cv2.VideoCapture('1.avi')
for k in range(100):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame, learningRate = 0)
    cv2.imshow('original', frame)
    cv2.imshow('frame', fgmask)
    while (1):
        if cv2.waitKey(0) & 0xff == ord('n'):
            break
    print k,' frames passed'

cap.release()
cv2.destroyAllWindows()