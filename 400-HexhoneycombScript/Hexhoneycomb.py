# -*- coding: UTF-8 -*-
# 将库路径添加到path
import sys
sys.path.append('C:\Python27\Lib\site-packages')

from dxfwrite import DXFEngine as dxf

# define a function to draw a Cshape 
def DrawCshape(x,y,r):
    # calculate point (x,y)
    import math
    angle=math.pi/6.0
    p1=(x-math.cos(angle)*r,y+0.5*r)
    p2=(x,y+r)
    p3=(x+math.cos(angle)*r,y+0.5*r)
    p4=(x+math.cos(angle)*r,y-0.5*r)
    p5=(x,y-r)
    p6=(x-math.cos(angle)*r,y-0.5*r)
    p7=(x,y+2*r)
    # draw lines
    global drawing
    
    drawing.add(dxf.line(start=p1,end=p2))
    drawing.add(dxf.line(start=p2,end=p3))
    drawing.add(dxf.line(start=p3,end=p4))
    drawing.add(dxf.line(start=p4,end=p5))
    drawing.add(dxf.line(start=p5,end=p6))
    drawing.add(dxf.line(start=p2,end=p7))

def FixLeft(x,y,r):
    import math
    p1=(x-math.cos(math.pi/6.0)*r,y-0.5*r)
    p2=(x-math.cos(math.pi/6.0)*r,y+0.5*r)
    drawing.add(dxf.line(start=p1,end=p2))

# 封顶,偶数行调用这个函数
def Capping(x,y,r):
    import math
    p1=(x+math.cos(math.pi/6.0)*r,y-0.5*r+3*r)
    p2=(x,y-r+3*r)
    p3=(x-math.cos(math.pi/6.0)*r,y-0.5*r+3*r)
    drawing.add(dxf.line(start=p1,end=p2))
    drawing.add(dxf.line(start=p2,end=p3))

def HVCopy(x,y,r,Hnum,Vnum):
    import math
    
    deltaX=2*math.cos(math.pi/6.0)*r
    deltaY=3*r
    Iscap=False
    
    if Vnum%2==0:
        #偶数行
        vn=int(Vnum/2)
        Iscap=True
    else:
        vn=int((Vnum+1)/2)
    
    for h in range(0, Hnum):
        x_h=x+h*deltaX
        for v in range(0,vn):
            y_v=y+v*deltaY
            DrawCshape(x_h,y_v,r)
            # 绘制左侧封闭线，只在1 3 5...等行绘制。
            if h==0:
                FixLeft(x_h,y_v,r)
            if v==vn-1 and Iscap:
                Capping(x_h,y_v,r)
# const var
# layer name
DXF_FILE='20230813.dxf'
x=0
y=0
# 六边形的大小
r=6
#水平方向
horizon_num=6
#竖直方向
vertical_num=6

# first : create a dxf file
drawing = dxf.drawing(DXF_FILE)
#drawing.add_layer(LAYER)

HVCopy(x,y,r,horizon_num,vertical_num)

drawing.save()
