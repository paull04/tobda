from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2



class TouchPoint(Image):
    def __init__(self, **kwargs):
        self.arr = None
        self.w, self.h = kwargs['size']
        super().__init__(**kwargs)

    def my_update(self, arr):
        self.arr = arr
        texture = Texture.create(size=arr.shape[:2][::-1], colorfmt="rgb")
        data = arr[::-1].tobytes()
        texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="rgb")
        self.texture = texture

    def on_touch_down(self, touch):
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


class CamApp(App):

    def build(self):
        layout = BoxLayout()
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        self.w = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.h = self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.img1 = TouchPoint(size=(self.w, self.h))
        layout.add_widget(self.img1)

        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.my_update(buf1)

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()