import cv2
import numpy as np

vid=cv2.VideoCapture("test_video.mp4")

while True:
    _,img = vid.read()
    canny = cv2.Canny(img, 150, 200)
    lines = cv2.HoughLinesP(canny, 1, np.pi/180, 150, minLineLength=10, maxLineGap=20)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    cv2.imshow("image",img)
    if (cv2.waitKey(1) & 0xFF == 27):
        break
cv2.destroyAllWindows()