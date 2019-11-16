import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
import math
import cv2
import time
from statistics import mean
from numpy import ones, vstack
from numpy.linalg import lstsq

def make_coordinates(image, line_parameters):
    slope,  intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


def avarage_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    try:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            interceprt = parameters[1]
            if slope < 0:
                left_fit.append((slope, interceprt))
            else:
                right_fit.append((slope, interceprt))

        left_fit_avg = np.average(left_fit, axis=0)
        right_fit_avg = np.average(right_fit, axis=0)


        left_line = make_coordinates(image, left_fit_avg)
        right_line = make_coordinates(image, right_fit_avg)
        return np.array([left_line, right_line])


    except:
        pass


def canny(image):
    # convert to gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blur the gray image
    blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # get th edge by canny function use to blue image
    canny_image = cv2.Canny(blur_image, 50, 105)
    return canny_image

def display_line(image, lines):
    try:
        line_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cords1 = (x1, y1)
                cords2 = (x2, y2)
                cv2.line(line_image, cords1, cords2, (255, 0, 0), thickness=10)
        return line_image
    except:
        line_image = np.array((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cords1 = (x1, y1)
                cords2 = (x2, y2)
                cv2.line(line_image, cords1, cords2, (255, 0, 0), thickness=10)
        return line_image





def region_of_interest(image):
    # set height
    height = image.shape[0]
    # set mask size
    #triangle = np.array([[(300, height), (850, height), (500, 250)]])
    triangle = np.array([[[100, 500], [100, 340], [200, 300], [500, 300], [800, 300], [800, 500]] ])
    #set mask ranger as 0
    mask = np.zeros_like(image)
    # fill the image
    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image




last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))
    # printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    # .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

    print('Loop took {} second'.format(time.time()- last_time))
    last_time = time.time()

    canny_screen = canny(screen)
    rio_screen = region_of_interest(canny_screen)
    lines = cv2.HoughLinesP(rio_screen, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    averaged_line = avarage_slope_intercept(rio_screen, lines)
    line_screen = display_line(screen, averaged_line)
    combo_screen = cv2.addWeighted(screen, 0.8, line_screen, 1, gamma=1)

    #cv2.imshow('window', screen)
    cv2.imshow('window2', combo_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break