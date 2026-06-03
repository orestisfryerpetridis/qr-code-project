from PIL import ImageGrab
#import cv2
import numpy as np
import cv2
from pyzbar import pyzbar
import urllib
import webbrowser   

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_info = ""
        barcode_info = barcode.data.decode('utf-8')
        if barcode_info != "":
            webbrowser.open(barcode_info)
            exit()

    return frame

while True:
    screen = np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
    while True:
        Beef = read_barcodes(screen)
        break
