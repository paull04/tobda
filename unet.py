from model import BaseModel
import cv2


class Unet(BaseModel):
    def __init__(self):
        super(Unet, self).__init__('unet.tflite')

    def get_segment(self, x):
        y = self.get_value(x)[0]
        y = cv2.resize(y, x.shape[:2][::-1])
        return y


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    model = Unet()
    img = cv2.imread('./img/320.jpg')
    a = model.get_segment(img)
    plt.imshow(a)
    plt.show()

