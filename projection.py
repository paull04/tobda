import numpy as np


class Projection:
    def __init__(self, cx, cy, fx, fy, pxToMetre):
        self.cx = cx
        self.cy = cy
        self.fx = fx
        self.fy = fy
        self.pxToMetre = pxToMetre

    def convert_from_uvd(self, u, v, d):
        d *= self.pxToMetre
        x_over_z = (self.cx - u) / self.fx
        y_over_z = (self.cy - v) / self.fy
        z = d / np.sqrt(1. + x_over_z ** 2 + y_over_z ** 2)
        x = x_over_z * z
        y = y_over_z * z
        return int(x), int(y), int(z)

    def match_point(self, u, v, depth: np.ndarray):
        x, y, z = self.convert_from_uvd(u, v, depth.max() - depth[u][v])
        return x, y, z

    def run(self, seg: np.ndarray, depth: np.ndarray):
        points = []
        for i in range(int(2 * self.cx)):
            for j in range(int(2 * self.cy)):
                if seg[i][j] == 1:
                    points.append((self.convert_from_uvd(i, j, depth[i][j])))
        return points
