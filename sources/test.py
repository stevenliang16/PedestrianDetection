import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread("London.jpg",0)
# cv2.imshow("Image", img)
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('LondonGrey.jpg', img)
#     cv2.destroyAllWindows()

# img = cv2.imread("London.jpg")
# img2 = img[:,:,::-1]
# plt.imshow(img2)
# plt.xticks([]), plt.yticks([])
# plt.show()

# cap = cv2.VideoCapture(0)
# fps = cap.get(5)
# print "FPS =", fps
# print cap.isOpened()
# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture('1.avi')
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

cap = cv2.VideoCapture('1.avi')

fgbg = cv2.BackgroundSubtractorMOG()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()