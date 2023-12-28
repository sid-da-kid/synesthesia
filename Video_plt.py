import cv2
import numpy as np
cv2.namedWindow("example", cv2.WINDOW_NORMAL)
vid_file = "Vid1.mp4"
vid = cv2.VideoCapture(vid_file)
#spf = int(1000/vid.get(cv2.CV_CAP_PROP_FPS)) #not used for now
while True:
    ret, vid_frame = vid.read() # Capture video frame-by-frame
    vid_frame = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("example", vid_frame) # Display the resulting frame
    if cv2.waitKey(1) == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
