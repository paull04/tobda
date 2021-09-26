import urllib.request
import cv2
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import json


def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


images_dir = 'img/'
with open('school_hallway_ver2-v0.1.json','r') as f:
    dataset = json.load(f)

for i in range(350, 360):
    img_url = dataset['dataset']['samples'][i]['attributes']['image']['url']
    img_name = dataset['dataset']['samples'][i]['name']
    img = url_to_image(img_url)
    cv2.imwrite(images_dir+img_name,img)