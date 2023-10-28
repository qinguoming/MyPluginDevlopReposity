# -*- coding: UTF-8 -*-
# 必须把RseFiberGenerate脚本放到工作目录下
# RSE 算法实现：《A new method for generating random fibre distributions for fibre reinforced composites》
# unit: SI(mm)
# 将dxf/matplotlib库路径添加到path
import sys
sys.path.append('C:\Python27\Lib\site-packages')
sys.path.append('G:\\SIMULIA\\EstProducts\\2020\\win_b64\\code\\python2.7\\lib')

# 外部依赖
import math,os
import random
from dxfwrite import DXFEngine as dxf
# abaqus的python2.7环境中自带了matplotlib，但缺少了绘图功能，
# 需要另外安装一个完整的matplotlib
import matplotlib.pyplot as plt
# from abaqusConstants  import *
# random.uniform(a, b)--生成[a, b] 之间的随机浮点数

# 参数设定
# abaqus工作目录
Cae_WorkDir='K:\\202309\\0912'
# 需要的纤维体积分数
vfr=0.65
# RVE宽度
a=100.0
# RVE高度
b=100.0
# RVE深度
fiberLength=100.0
# 纤维形状定义
PolygonShapeDef='D:\\five_pointed_star.txt'
# 纤维间距最小值
lmin=0.5
# 纤维间距最大值
lmax=1
# 每根纤维都会尝试N次，寻找符合条件的纤维，500已经足够大了。
N=500
# dxf 文件名
dxfFile='rve.dxf'
# ABAQUS Model name
# 运行前，必须model必须存在，且为当前工作对象。
model='Model-1'
FiberPartName='Fiber'
MatrixPartName='RVEbase'
FiberInstanceName='Fiber-1'
MatrixInstanceName='RVEbase-1'
RVEPartName='RVE'

# 初始纤维中心点生成的区域
a0=a/10
b0=b/10

# [x,y,r,flag] , flag--是否与边界相交，且相交的位置
# flag: 
#   + 'in': 完全在边界线内
#   + 'out': 完全在边界线外
#   + 'Bu':只和上边界线相交
#   + 'Bb':只和下边界线相交
#   + 'Bl':只和左边界线相交
#   + 'Br':只和右边界线相交
#   + 'Clu':同时和左、上边界线相交
#   + 'Clb':同时和左、下边界线相交
#   + 'Cru':同时和右、上边界线相交
#   + 'Crb':同时和右、下边界线相交

# define polygon shape object
def GetPolygonShape(PolygonShapeDef):
    import numpy as np
    data = np.genfromtxt(PolygonShapeDef,dtype=[float, float],delimiter=',')  # 将文件中数据加载到data数组里
    print(data)

GetPolygonShape()