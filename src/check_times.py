import pytesseract
import cv2
import time
from collections import deque

def how_many_minutes(hour):
    return hour*60

def check_times():
    img_cv = cv2.imread('/home/esozen1/tubitime/example_pic/iCard3.jpg')
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    converted_string = pytesseract.image_to_string(img_rgb)
    all_text_list = converted_string.strip().split('\n')

    for key in all_text_list:
        print(key)
        time.sleep(0.3)
        if key.__contains__('Buradaki'):
            pass
        elif key.__contains__('saat'):
            #print(key)
            #key = key.strip('dk').split('saat')
            hour = key[0]
            minute = key[1]
            #hour = float(hour)
            #minutes1 = how_many_minutes(hour)
            #minutes2 = float(minute)
            #print(minutes1 + minutes2)
        elif key.__contains__('202'):
            print(2)
        elif key.__contains__(':'):
            print(3)
        

if __name__ == "__main__":
    # execute only if run as a script
    check_times()