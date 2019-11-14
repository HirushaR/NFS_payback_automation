import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()
while(True):
    screen =  np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))
    # printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    # .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

    print('Loop took {} second'.format(time.time()- last_time))
    last_time = time.time()

    # convert to gray
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # blur the gray image
    blur_screen = cv2.GaussianBlur(gray_screen, (5, 5), 0)
    #cv2.imshow('window', screen)
    cv2.imshow('window2', blur_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break