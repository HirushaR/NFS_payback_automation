import numpy as np
from PIL import ImageGrab
import cv2
import time
from key_direct import PressKey, W , A, S, D, ReleaseKey

def roi(img , vertices):
    # shape convert to zeros
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(original_image):
    # covert original image to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=300, threshold2=200)
    # shape of the road we want to identify i put a image later
    vertices = np.array([10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800,500] )
    processed_img = roi(processed_img, vertices)
    return processed_img

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

# get the time
last_time = time.time()
while(True):
    # get the screen my payback screen in 800 ,600
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))
    new_screen = process_img(screen)
    print('Loop took {} second'.format(time.time()-last_time))
    # how much time that goes to
    last_time = time.time()
    # time.sleep(3) with delay our new screen in 3 sec
    cv2.imshow('window', new_screen)
    # cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break