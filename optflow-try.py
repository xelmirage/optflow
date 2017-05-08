# -*- coding:utf-8 -*-


import cv2
import numpy as np
import optFlowshow
from matplotlib import pyplot as plt


img1 = cv2.imread("datas/flow/tm1-0002.jpeg", 0)
img2 = cv2.imread("datas/flow/tm1-0003.jpeg", 0)

flow = 0
flow1=cv2.calcOpticalFlowFarneback(img1, img2, flow, 0.5, 3, 15, 3, 5, 1, 0)

flow_img = optFlowshow.draw_flow(img1, flow1)

plt.imshow(flow_img)
plt.show()
