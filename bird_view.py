from unet import Unet
from midas import Midas
from transform import warpBird, find_points


unet = Unet()
midas = Midas()


def imgTobird(img):
    mask = unet.mask(img)
    depth = midas.get_depth(img)
    points = find_points(mask)
    return warpBird(mask, depth, points)
