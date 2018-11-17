# coding=utf-8
from picamera import PiCamera
from time import sleep
import cv2

print(cv2.__version__)

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
print("start recording......")
camera.start_recording('foo.h264')
camera.wait_recording(6)
camera.stop_recording()
print("stop record!")
sleep(1)
print("Taking pictures")
camera.capture('foo.jpg')
camera.stop_preview()
print("finish!")
