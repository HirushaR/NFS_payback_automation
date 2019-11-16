import numpy as np
import cv2
import time
import os

from PIL import ImageGrab
from get_keys import key_check

def keys_to_output(keys):
    # [A,W,D]
    output = [0, 0, 0]
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output

file_name = 'traning_data.npy'

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))
        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
