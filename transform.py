import cv2
import numpy as np
from unet import Unet
from midas import Midas
from projection import Projection


def find_points(mask):
    # find mask's biggest contour
    thresholded_mask = cv2.convertScaleAbs(mask)
    contours, _ = cv2.findContours(thresholded_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_areas = []
    for i, c in enumerate(contours):
        contour_areas.append(cv2.contourArea(c))
    sorted_contours = sorted(zip(contour_areas, contours), key=lambda x: x[0], reverse=True)
    biggest_contour= sorted_contours[0][1]
    contour_image = cv2.drawContours(np.array(mask), biggest_contour, -1, (255, 255, 255), 3)
    x, y, w, h = cv2.boundingRect(biggest_contour)

    # four suitable points
    points = []
    left = True
    for i in range(0, mask.shape[1]):
        if mask[y+50][i] == 1 and left == True:
            points.append((y+100,i+20))
            left = False
        if mask[y+50][i] == 0 and left == False:
            points.append((y+100,i-20))
            break
    points.append((y+h-50,x+100))


P = Projection(1000, 1000, 1000, 1000, 1)


def warpBird(mask:np.ndarray,depth:np.ndarray,points:list):
    # find matrix for warping transform
    pts1 = [(point[1],point[0]) for point in points]
    Pmask.shape[0] / 2, mask.shape[1] / 2

    def f1(p):
        x, y, z = P.match_point(p[0], p[1], depth=depth)
        return 1100 - y, 2500 - z

    pts2 = [f1 for point in points]

    pts1, pts2 = np.float32(pts1),np.float32(pts2)
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    #print(matrix.shape)

    # warping transform
    warped_mask = cv2.warpPerspective(mask,matrix,(2000,2000))
    return warped_mask


