import cv2
import os
import shutil
import time

def start (camport : int):
    capture(camport)

def record (camport):
    shutil.rmtree('resources\\images')
    os.makedirs('resources\\images')
    cap = cv2.VideoCapture(camport)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            cv2.imwrite(f'resources\\images\\{time.time()}.jpg', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def capture (camport):
    shutil.rmtree('resources\\images')
    os.makedirs('resources\\images')
    cap = cv2.VideoCapture(camport)

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            cv2.imwrite(f'resources\\images\\{time.time()}.jpg', frame)
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()