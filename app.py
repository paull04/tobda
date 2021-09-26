import numpy as np
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import PIL.Image as Pimage
import cv2
from bird_view import imgTobird



class TouchPoint(Image):
    def __init__(self, **kwargs):
        self.arr = None
        self.is_cam_on: bool = False
        self.arr = None
        self.capture = None
        self.callback = lambda dt: self.my_update(self.capturing())
        self.event = None
        super().__init__(**kwargs)

    def capturing(self):
        ret, frame = self.capture.read()
        return frame

    def my_update(self, arr):
        self.arr = arr
        self.h, self.w = self.arr.shape[:2]
        texture = Texture.create(size=arr.shape[:2][::-1], colorfmt="rgb")
        data = arr[::-1].tobytes()
        texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="rgb")
        self.texture = texture

    def check_pos(self, touch):
        if self.arr is None:
            return
        # coordinates of image lower left corner inside the TouchPoint widget
        im_x = (self.size[0] - self.norm_image_size[0]) / 2.0 + self.x
        im_y = (self.size[1] - self.norm_image_size[1]) / 2.0 + self.y

        # touch coordinates relative to image location
        im_touch_x = touch.x - im_x
        im_touch_y = touch.y - im_y

        # check if touch is with the actual image
        if im_touch_x < 0 or im_touch_x >= self.norm_image_size[0]:
            #진동
            print('Missed')
        elif im_touch_y < 0 or im_touch_y >= self.norm_image_size[1]:
            #진동
            print('Missed')

        else:
            im_touch_y = self.norm_image_size[1] - im_touch_y
            u, v = self.norm_image_size
            new_x = int(im_touch_x * self.w/u)
            new_y = int(im_touch_y * self.h/v)
            print('image touch coords:', new_x, new_y)
            print('color:', self.arr[new_y, new_x])
            if sum(self.arr[new_y, new_x]):
                #진동
                pass

    def on_touch_down(self, touch):
        if self.is_cam_on and touch.is_double_tap:
            self.is_cam_on = False
            self.capture.release()
            self.event.cancel()
            arr = imgTobird(self.arr)
            newarr = np.empty([arr.shape[0], arr.shape[1], 3], dtype=np.uint8)
            for x in range(newarr.shape[0]):
                for y in range(newarr.shape[1]):
                    p = newarr[x, y]
                    p[0] = p[1] = p[2] = int(arr[x, y] * 255)
            self.my_update(newarr)

        elif touch.is_double_tap:
            self.is_cam_on = True
            self.capture = cv2.VideoCapture(0)
            self.capture.set(3, 1920)
            self.capture.set(4, 1080)
            self.event = Clock.schedule_interval(self.callback, 1.0/33.0)

        elif not self.is_cam_on:
            self.check_pos(touch)

    def on_touch_move(self, touch):
        if not self.is_cam_on:
            self.check_pos(touch)


class MainApp(App):
    def __init__(self):
        super(MainApp, self).__init__()

    def build(self):
        box = BoxLayout()
        self.img = TouchPoint()
        box.add_widget(
            self.img
        )
        return box


def test():
    MainApp().run()


if __name__ == "__main__":
    test()