# -*- coding:utf-8 -*-


import cv2
import numpy as np
from matplotlib import pyplot as plt


def draw_flow(img, flow, step=64):
    h, w = img.shape[:2]
    y, x = np.mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1)  # 以网格的形式选取二维图像上等间隔的点，这里间隔为16，reshape成2行的array
    fx, fy = flow[y, x].T  # 取选定网格点坐标对应的光流位移
    lines = np.vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)  # 将初始点和变化的点堆叠成2*2的数组
    lines = np.int32(lines + 0.5)  # 忽略微笑的假偏移，整数化
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 0))  # 以初始点和终点划线表示光流运动
    for (x1, y1), (x2, y2) in lines:
        cv2.circle(vis, (x1, y1), 5, (0, 255, 0), -1)  # 在初始点（网格点处画圆点来表示初始点）
    return vis


def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:, :, 0], flow[:, :, 1]
    ang = np.arctan2(fy, fx) + np.pi  # 得到运动的角度
    v = np.sqrt(fx * fx + fy * fy)  # 得到运动的位移长度
    hsv = np.zeros((h, w, 3), np.uint8)  # 初始化一个0值空3通道图像
    hsv[..., 0] = ang * (180 / np.pi / 2)  # B通道为角度信息表示色调
    hsv[..., 1] = 255  # G通道为255饱和度
    hsv[..., 2] = np.minimum(v * 4, 255)  # R通道为位移与255中较小值来表示亮度
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)  # 将得到的HSV模型转换为BGR显示
    return bgr


if __name__ == '__main__':
    img = cv2.imread('images/t1/tm8913.jpg')
    print img
    flow = cv2.optflow.readOpticalFlow('datas/flow/8913-8921.flo')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    flow_img=draw_flow(gray, flow)
    #flow_img = draw_hsv(flow)
    print('datas/flow/4950.flo',flow.max(),flow.min())
    plt.imshow(flow_img)
    plt.show()
    print (flow)
