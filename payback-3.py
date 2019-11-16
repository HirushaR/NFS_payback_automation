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

if os.path.isfile(file_name):
    print('File exist, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting data')
    training_data = []

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80, 60))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen, output])
        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

main()
