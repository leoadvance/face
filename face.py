# coding=utf-8
from picamera import PiCamera
from time import sleep
import cv2

print(cv2.__version__)

camera = PiCamera()
#camera.start_pr
camera.resolution = (1920, 1080)
camera.start_preview()
camera.start_recording('foo.h264')
camera.wait_recording(6)
camera.stop_recording()
camera.stop_preview()
print("finish!")
