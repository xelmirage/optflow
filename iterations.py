__author__ = 'xelmirage'

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import string


datafile = open('datas/iterations/out1.txt')
list_of_all_the_lines = datafile.readlines( )

plt.style.use('fivethirtyeight')

#fig = plt.figure()
#fig.set_size_inches(8, 6)
#ax = fig.add_subplot(111, projection='3d')
fig, ax=plt.subplots();
xs=[]
ys=[]

for line in list_of_all_the_lines:
    list=line.split(',')
    x=int(list[0])
    y=float(list[1])
    print "%d,%f"%(x,y)
    xs.append(x)
    ys.append(y)
ax.plot(xs,ys)

datafile = open('datas/iterations/out2.txt')
list_of_all_the_lines = datafile.readlines( )

#fig = plt.figure()
#fig.set_size_inches(8, 6)
#ax = fig.add_subplot(111, projection='3d')
xs=[]
ys=[]

for line in list_of_all_the_lines:
    list=line.split(',')
    x=int(list[0])
    y=float(list[1])
    print "%d,%f"%(x,y)
    xs.append(x)
    ys.append(y)
ax.plot(xs,ys)

datafile = open('datas/iterations/out3.txt')
list_of_all_the_lines = datafile.readlines( )

#fig = plt.figure()
#fig.set_size_inches(8, 6)
#ax = fig.add_subplot(111, projection='3d')

xs=[]
ys=[]

for line in list_of_all_the_lines:
    list=line.split(',')
    x=int(list[0])
    y=float(list[1])
    print "%d,%f"%(x,y)
    xs.append(x)
    ys.append(y)
ax.plot(xs,ys)


#ax.set_zlabel('ALTITUDE')

plt.show()

