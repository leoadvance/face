from picamera import picamera
# coding=utf-8
import cv2

print(cv2.__version__)

camera = picamera()
camera.start_preview()
sleep(3)
camera.stop_preview()
