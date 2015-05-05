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

for k in range(1000):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame, learningRate = 0.001)
    cv2.imshow('frame',fgmask)
    cv2.waitKey(10)
print 'Completed Once.'
cap.release()

cap = cv2.VideoCapture('1.avi')
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame, learningRate = 0)
    cv2.imshow('original', frame)
    cv2.imshow('frame', fgmask)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

cap.release()


cv2.destroyAllWindows()