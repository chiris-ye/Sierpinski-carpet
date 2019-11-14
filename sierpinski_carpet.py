from matplotlib import pyplot as plt
from matplotlib import colors
import matplotlib as mpl
from numba import jit
import numpy as np

@jit
def carpet(degre):
    #degre的次数为演进次数
    size=3**degre
    #np.ones是设定各位都为1的矩阵
    matrix=np.ones([size, size])

    for niveau in range(degre+1):
        step=3**(degre-niveau)
        for x in range(size):
            if x%3==1:
                for y in range(size):
                    if y%3==1:
                        matrix[y*step:(y+1)*step, x*step:(x+1)*step]=0
                
    return matrix


degre=6
matrix=carpet(degre)
zoom=1 # default: 1
bouge=[
        0   #droite - gauche
        ,0      #haut-bas
]

mpl.rcParams['toolbar'] = 'None' #erase buttons
'''
plt.rcParams['figure.figsize'] = (8.0, 4.0) # 设置figure_size尺寸
plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
plt.rcParams['image.cmap'] = 'gray' # 设置 颜色 style
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
'''
#像素为72，无边框
fig=plt.figure(dpi=72,frameon=False)
#颜色为灰
cmap = 'gray'

ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

img=ax.imshow(matrix, cmap, interpolation="bilinear")



plt.show()