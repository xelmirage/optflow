# -*- coding:utf-8 -*-


import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import numpy as np
import math
from matplotlib import pyplot as plt
str='datas/flow/8913-8921.flo'
flow = cv2.optflow.readOpticalFlow(str)

x = np.linspace(0, len(flow[0]) - 1, len(flow[0]))
y = np.linspace(0, len(flow) - 1, len(flow))
xv, yv = np.meshgrid(x, y)
# print xv, yv
# print len(xv[0]), len(yv[0])
z = []
for i in range(0, len(y)):
    z1 = []
    for j in range(0, len(x)):
        dx = flow[i][j][0]
        dy = flow[i][j][1]
        prllx = math.sqrt(dx ** 2 + dy ** 2)
        z1.append(prllx)
    z.append(z1)
#fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
#ls = LightSource(270, 45)
plt.set_cmap("gray")
plt.imshow(z)
plt.colorbar()
plt.title(str)
#rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
#surf = ax.plot_surface(xv, yv, z, rstride=1, cstride=1,
#                       linewidth=0, antialiased=False, shade=False)
plt.show()