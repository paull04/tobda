import numpy as np
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from PIL import Image as PImage
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import jnius
from matplotlib import cm

import PIL.Image as I

print('1')
"""# Context is a normal java class in the Android API
Context = jnius.autoclass('android.content.Context')
PythonActivity = jnius.autoclass('org.renpy.android.PythonActivity')

activity = PythonActivity.mActivity

# This is almost identical to the java code for the vibrator
#vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

#vibrator.vibrate(1)  # The value is in milliseconds - this is 10s
"""

arr = np.asarray(np.load("./mask.npy"))
newarr = np.empty([arr.shape[0], arr.shape[1], 3], dtype=np.uint8)
print(arr.shape)
for x in range(newarr.shape[0]):
    for y in range(newarr.shape[1]):
        p = newarr[x, y]
        p[0] = p[1] = p[2] = int(arr[x, y] * 255)


im = I.fromarray(newarr)
newarr = np.asarray(im.resize((500, 500)))
plt.imshow(newarr)
plt.show()
newarr = newarr[::-1]
h, w = newarr.shape[:2]

print(w, h)


class TouchPoint(Image):
    def on_touch_down(self, touch):
        if 1:
            # coordinates of image lower left corner inside the TouchPoint widget
            im_x = (self.size[0] - self.norm_image_size[0]) / 2.0 + self.x
            im_y = (self.size[1] - self.norm_image_size[1]) / 2.0 + self.y

            # touch coordinates relative to image location
            im_touch_x = touch.x - im_x
            im_touch_y = touch.y - im_y

            # check if touch is with the actual image
            if im_touch_x < 0 or im_touch_x >= self.norm_image_size[0]:
                print('Missed')
            elif im_touch_y < 0 or im_touch_y >= self.norm_image_size[1]:
                print('Missed')
            else:
                im_touch_y = self.norm_image_size[1] - im_touch_y

                u, v = self.norm_image_size
                print('image touch coords:', int(im_touch_x * w/u), int(im_touch_y * h/v))
                print('color:', newarr[int(im_touch_y * h/v), int(im_touch_x * w/u)])


class MainApp(App):
    def __init__(self):
        super(MainApp, self).__init__()

    def build(self):
        try:
            box = BoxLayout()
            #box.add_widget(FigureCanvasKivyAgg())
            texture = Texture.create(size=(w, h), colorfmt="rgb")
            data = newarr.tobytes()
            texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="rgb")
            img = TouchPoint(size=(w, h))
            img.texture = texture
            box.add_widget(img)
            return box

        except Exception as e:
            print(e)



MainApp().run()
