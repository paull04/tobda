from model import BaseModel
import cv2


class Midas(BaseModel):
    def __init__(self):
        super(Midas, self).__init__('midas_lite.tflite')

    def get_depth(self, x):
        y = self.get_value(x)[0]
        y = cv2.resize(y, x.shape[:2][::-1])
        return y


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    model = Midas()
    img = cv2.imread('./img/320.jpg')
    a = model.get_depth(img)
    plt.imshow(a)
    plt.show()
    #print(a[0].shape)


