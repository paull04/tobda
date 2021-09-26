from model import BaseModel
import numpy as np
import cv2


class Unet(BaseModel):
    def __init__(self):
        super(Unet, self).__init__('unet.tflite')

    def mask(self, x):
        mask = self.get_value(x)[0]
        threshold = 0.8
        mask = cv2.resize(mask, x.shape[:2][::-1])
        mask[np.where(mask >= threshold)] = 1
        mask[np.where(mask < threshold)] = 0
        return mask


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    model = Unet()
    img = cv2.imread('./img/320.jpg')
    a = model.mask(img)
    plt.imshow(a)
    plt.show()

