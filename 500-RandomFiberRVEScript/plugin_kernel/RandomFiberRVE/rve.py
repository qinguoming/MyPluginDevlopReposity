# -*- coding: UTF-8 -*-
# The script must be placed in the working directory
# The fiber random distribution algorithm comes from：《A new method for generating random fibre distributions for fibre reinforced composites》
# unit: SI(mm)

# Add the dxf library path to path
import sys

# 外部依赖
import math,os
import random
from abaqusConstants  import *

# external dependency
# dxfwrite lib Path dirs
dxflib='C:\Python27\Lib\site-packages'
# abaqus working directory
Cae_WorkDir='K:\\202309\\0912'
# Required fiber volume fraction
vfr=0.65
# RVE width
a=100.0
# RVE height
b=100.0
# RVE deepth
fiberLength=100.0
# fiber radius
r=5
# Minimum fibers distance
lmin=0.5
# Maximum fibers distance
lmax=1
# Each fiber will be tried N times, looking for a fiber that fits the criteria, and 500 is already large enough.
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

# 中间变量
# vf0=（纤维横截面面积）/a*b
d=2*r

# 初始纤维中心点生成的区域


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

def RVE(vfr,vf0,a,b,a0,b0,r,lmax,lmin,N):
    """得到纤维对象序列"""
    # 结果变量
    fiberList=[]
    
    # 生成第一个纤维
    initFiber=FirstFiber(a0,b0,r)
    fiberList.append(initFiber)
    # fill fiber in windows
    for Fiber_i in fiberList:
        for j in range(N):
            tempFiber=GenerateFiber(Fiber_i,r,lmin,lmax,a,b)
            # 纤维生成的条件：不自相交 and 在边界之内
            if tempFiber[3]!='out' and IsintersectSelf(tempFiber,fiberList,r)==False:
                fiberList.append(tempFiber)
            else:
                continue
    # 计算当前的纤维体积分数,满足要求则返回fibers
    t=fiberList
    if CalVolumeFraction(t,a,b,r)>vfr:
        # 开始随机删除纤维
        for i in range(len(t)):
            NowNumOfFibers=len(fiberList)
            # 随机删除其中一个纤维
            del fiberList[random.randint(0, NowNumOfFibers)]
            if abs(CalVolumeFraction(fiberList,a,b,r)-vfr)<0.5*vf0:
                # 生成成功，返回纤维列表
                print('==> Generated successfully, the Volume Fraction is:'+str(CalVolumeFraction(fiberList,a,b,r)))
                return fiberList
    # 不能满足 vfr，纤维生成到达极限，充满了Windows。
    else:
        print('==> Generate failed, fiber filled window but volume fraction not satisfied!')
        return fiberList

def ISoverreach(x,y,r,a,b):
    """纤维是否与边界线相交,返回值表示相交的位置"""
    # global a,b
    
    state=CornerIsInFiber(x,y,r,a,b)
    
    if state=='go':
        # 说明角点不在纤维内，进一步判断。
        left = ((-0.5*a-r)<x<(-0.5*a+r) and abs(y)<(0.5*b-r)) or \
            ((-0.5*a-r)<x<(-0.5*a) and (0.5*b-r)<y<(0.5*b) and P2Pdistance((x,y),(-0.5*a,0.5*b))>r ) or \
            (P2Pdistance((x,y),(-0.5*a,-0.5*b))>r and (-0.5*a-r)<x<(-0.5*a) and (-0.5*b)<y<(-0.5*b+r))
        right= ((0.5*a-r)<x<(0.5*a+r) and abs(y)<(0.5*b-r)) or \
            ((0.5*a)<x<(r+0.5*a) and (0.5*b-r)<y<(0.5*b) and P2Pdistance((x,y),(0.5*a,0.5*b))>r ) or \
            ((0.5*a)<x<(r+0.5*a) and (-0.5*b)<y<(-0.5*b+r) and P2Pdistance((x,y),(0.5*a,-0.5*b))>r)
        bottom=(abs(x)<(0.5*a-r) and (-0.5*b-r)<y<(-0.5*b+r)) or \
            ((-0.5*a)<x<(-0.5*a+r) and (-0.5*b-r)<y<(-0.5*b) and P2Pdistance((x,y),(-0.5*a,-0.5*b))>r ) or \
            ((0.5*a-r)<x<(0.5*a) and (-0.5*b-r)<y<(-0.5*b) and P2Pdistance((x,y),(0.5*a,-0.5*b))>r)
        up=(abs(x)<(0.5*a-r) and (0.5*b-r)<y<(0.5*b+r)) or \
            ((-0.5*a)<x<(-0.5*a+r) and (0.5*b)<y<(0.5*b+r) and P2Pdistance((x,y),(-0.5*a,0.5*b))>r ) or \
            ((0.5*a-r)<x<(0.5*a) and (0.5*b)<y<(0.5*b+r) and P2Pdistance((x,y),(0.5*a,0.5*b))>r)
        # 其中一个成立则说明和边界相交 
        if left :
            return 'Bl'
        elif right:
            return 'Br'
        elif bottom:
            return 'Bb'
        elif up:
            return 'Bu'
        else:
            if (-0.5*a+r)<x<(0.5*a-r) and (-0.5*b+r)<y<(0.5*b-r):
                return 'in'
            else:
                return 'out'
    else:
        return state
    
def CornerIsInFiber(x,y,r,a,b):
    """判断边界角点是否在纤维内？哪个象限的角点落在纤维内"""
    # global a,b
    
    if P2Pdistance((0.5*a,0.5*b),(x,y))<r or ((0.5*a-r)<x and x<0.5*a and (0.5*b-r)<y and y<0.5*b):
        return 'Cru'
    if P2Pdistance((-0.5*a,0.5*b),(x,y))<r or (-0.5*a<x and x<(-0.5*a+r) and (0.5*b-r)<y and y<0.5*b):
        return 'Clu'
    if P2Pdistance((-0.5*a,-0.5*b),(x,y))<r or (-0.5*a<x and x<(-0.5*a+r) and y>-0.5*b and y<(-0.5*b+r)):
        return 'Clb'
    if P2Pdistance((0.5*a,-0.5*b),(x,y))<r or ((0.5*a-r)<x and x<0.5*a and y>-0.5*b and y<(-0.5*b+r)):
        return 'Crb'
    
    return 'go'

def FirstFiber(a0,b0,r):
    """生成第一个纤维"""
    # global a0,b0,r
    # 生成第一根纤维中心坐标(x1,y1)
    x1=random.uniform(a=-0.5*a0,b=0.5*a0)
    y1=random.uniform(a=-0.5*b0,b=0.5*b0)
    r1=r
    
    return [x1,y1,r1,'in']

def Polar2Dcar(recx,recy,distance,angle):
    """局部极坐标 转为 全局笛卡尔坐标"""
    x_g=recx+distance*math.cos(angle)
    y_g=recy+distance*math.sin(angle)
    return (x_g,y_g)

# 根据现有的纤维生成下一个纤维
def GenerateFiber(preFiber,r,lmin,lmax,a,b):
    # global r,lmin,lmax
    
    xlast=preFiber[0]
    ylast=preFiber[1]

    # 局部极坐标系下的坐标值：(distance,angle)
    distance=random.uniform(lmin+2*r,lmax+2*r)
    angle=random.uniform(0,2*math.pi)
    
    # 得到本条纤维的全局笛卡尔坐标值
    Center=Polar2Dcar(xlast,ylast,distance,angle)
    # 判断纤维和边界线的位置关系
    flag=ISoverreach(Center[0],Center[1],r,a,b)
    # 返回一个fiber对象
    return [Center[0],Center[1],r,flag]

def ExtractXY(fiberlist):
    """从纤维对象序列中提取x,y坐标"""
    XYlist=[]
    for i in fiberlist:
        XYlist.append(i[:2])
    return XYlist

def IsintersectSelf(nowfiber,fiberlist,r):
    """判断当前纤维是否与其他纤维相交"""
    # global r
    # 将现有的fibers按照flag进行分类，in、b、c
    ExpandFiberList=[]  
    for Fiber_i in fiberlist:
        if Fiber_i[3]=='in':
            ExpandFiberList.append(tuple(Fiber_i[:2]))
        else:
            # 和边界线相交的纤维，需要扩展。1变2、1变4.
            Cs=CalExpendCenter(Fiber_i,a,b)
            for j in Cs:
                ExpandFiberList.append(j)
    # 待检测的fiber的(x,y)s
    if nowfiber[3]=='in':
        ExpandNowFiber=tuple(nowfiber[:2])
        for k in ExpandFiberList:
            if math.sqrt((ExpandNowFiber[0]-k[0])**2+(ExpandNowFiber[1]-k[1])**2)<2*r:
                return True
    else:
        ExpandNowFiber=CalExpendCenter(nowfiber,a,b)
        for m in ExpandNowFiber:
            for n in ExpandFiberList:
                if math.sqrt((m[0]-n[0])**2+(m[1]-n[1])**2)<2*r:
                    return True
    return False


def CalVolumeFraction(fiberlist,a,b,r):
    # global a,b,r
    return (len(fiberlist)*math.pi*r*r)/(a*b)

def P2Pdistance(p1,p2):
    """两点间的距离:输入两个元组"""
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def Draw2DXF(fiberlist,dxfFile,a,b):
    from dxfwrite import DXFEngine as dxf
    """将现有的纤维写入到dxf文件"""
    # 创建dxf 文件
    drawing = dxf.drawing(dxfFile)
    # 将纤维写入 dxf 文件
    for fiber in fiberlist:
        center=tuple(fiber[:2])
        radius=fiber[2]
        if fiber[3]=='in':
            # 纤维完全在边界线内部
            drawing.add(dxf.circle(radius=radius,center=center))
        else:
            # 当纤维和边界相交，特殊处理
            DrawBrokenFiber(fiber,drawing,a,b)
    drawing.save()
    
def DrawBrokenFiber(fiber,drawing,a,b):
    """绘制和边界相交的纤维、位于角点的纤维"""
    from dxfwrite import DXFEngine as dxf
    # global a,b
    r=fiber[2]

    Cs=CalExpendCenter(fiber,a,b)
    if len(Cs)==4:
        # 角点在纤维内
        drawing.add(dxf.circle(radius=r,center=Cs[0],color=90))
        drawing.add(dxf.circle(radius=r,center=Cs[1],color=130))
        drawing.add(dxf.circle(radius=r,center=Cs[2],color=170))
        drawing.add(dxf.circle(radius=r,center=Cs[3],color=210))
    elif len(Cs)==2:
        # 角点不在纤维，但纤维和边界相交
        drawing.add(dxf.circle(radius=r,center=Cs[0],color=20))
        drawing.add(dxf.circle(radius=r,center=Cs[1],color=20))
        
# def ShowRVE(fiberlist):
#     """展示RVE结果"""
#     global a,b
#     figure, axes = plt.subplots()
#     for fiber in fiberlist:
#         center=tuple(fiber[:2])
#         radius=fiber[2]
#         if fiber[3]=='in':
#             # 纤维完全在边界线内部
#             draw1 = plt.Circle(center, radius,fill=False,color='g')
#             axes.add_artist(draw1)
#         else:
#             Cs=CalExpendCenter(fiber,a,b)
#             if len(Cs)==4:
#                 # 角点在纤维内
#                 d1=plt.Circle(Cs[0], radius,fill=False,color='b')
#                 axes.add_artist(d1)
#                 d2=plt.Circle(Cs[1], radius,fill=False,color='b')
#                 axes.add_artist(d2)
#                 d3=plt.Circle(Cs[2], radius,fill=False,color='b')
#                 axes.add_artist(d3)
#                 d4=plt.Circle(Cs[3], radius,fill=False,color='b')
#                 axes.add_artist(d4)
#             elif len(Cs)==2:
#                 # 角点不在纤维，但纤维和边界相交
#                 d5=plt.Circle(Cs[0], radius,fill=False,color='r')
#                 axes.add_artist(d5)
#                 d6=plt.Circle(Cs[1], radius,fill=False,color='r')
#                 axes.add_artist(d6)
#     plt.title('RVE')
#     axes.set_aspect(1)
#     plt.xlim(-0.5*a,0.5*a)
#     plt.ylim(-0.5*b,0.5*b)
#     plt.xlabel('a')
#     plt.ylabel('b')
#     plt.show()

def ShowInfo(r,a,b,lmax,lmin,vf0,vfr,dxfFile):
    # ----- info show -----
    print('\n')
    print(' ----- info show -----')
    print(' Required Fiber Volume Fraction = '+str(vfr))
    print(' Fiber Radius = '+str(r))
    print(' Windows Width = '+str(a))
    print(' Windows Height = '+str(b))
    print(' Fibre Spacing Min = '+str(lmin))
    print(' Fibre Spacing Max = '+str(lmax))
    print(' Vf0 = '+str(vf0))
    # print(' Low Limit Volume Fraction = '+str(tr))
    print(' Export To DXF = '+str(dxfFile))

def CalExpendCenter(fiber,a,b):
    """计算一个纤维的扩展纤维中心点，如果纤维和角点相交，那就返回四个中心点坐标"""
    x=fiber[0]
    y=fiber[1]
    tempflag=fiber[3]
    if tempflag[0]=='C':
        if tempflag=='Clu':
            c1=(x,y)
            c2=(x,y-b)
            c3=(x+a,y)
            c4=(x+a,y-b)
        elif tempflag=='Clb':
            c1=(x,y)
            c2=(x,y+b)
            c3=(x+a,y)
            c4=(x+a,y+b)
        elif tempflag=='Cru':
            c1=(x,y)
            c2=(x,y-b)
            c3=(x-a,y)
            c4=(x-a,y-b)
        elif tempflag=='Crb':
            c1=(x,y)
            c2=(x,y+b)
            c3=(x-a,y)
            c4=(x-a,y+b)
        return (c1,c2,c3,c4)
    elif tempflag[0]=='B':
        # 计算2个中心点位置
        if tempflag=='Bu':
            b1=(x,y)
            b2=(x,y-b)
        elif tempflag=='Bb':
            b1=(x,y)
            b2=(x,y+b)
        elif tempflag=='Bl':
            b1=(x,y)
            b2=(x+a,y)
        elif tempflag=='Br':
            b1=(x,y)
            b2=(x-a,y)
        return (b1,b2)

def LowLimitFillFraction(a,b,r):
    """简单估计纤维的极限最低填充率,实际会比这个起码高0.05~0.1以上"""
    # global a,b,d,r
    na=math.floor(a/(2*r))
    # print(na)
    nb=math.floor(b/(2*r))
    # print(nb)
    return (na*nb*math.pi*r*r)/(a*b)

def DXF2ABAQUS(fiberLength,a,b,model,FiberPartName,dxfFile,MatrixPartName,
                FiberInstanceName,MatrixInstanceName,RVEPartName):
    from abaqus import backwardCompatibility
    from dxf2abq import importdxf
    import abaqus
    from abaqus import mdb
    import abaqusConstants 
    import __main__
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import optimization
    import step
    import interaction
    import load
    import mesh
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    backwardCompatibility.setValues(reportDeprecated=False)
    
    # define var
    # 导入dxf到abaqus
    importdxf(fileName=dxfFile)
    s = mdb.models[model].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    s.setPrimaryObject(option=STANDALONE)
    s.sketchOptions.setValues(gridOrigin=(0.0432090759277344, -0.10296630859375))
    s.retrieveSketch(sketch=mdb.models[model].sketches[dxfFile[:-4]])
    
    # 创建fiber part
    p=mdb.models[model].Part(name=FiberPartName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = mdb.models[model].parts[FiberPartName]
    p.BaseSolidExtrude(sketch=s, depth=float(fiberLength))
    s.unsetPrimaryObject()
    del mdb.models[model].sketches['__profile__']
    
    # 绘制基体part
    s1 = mdb.models[model].ConstrainedSketch(name='base', sheetSize=200.0)
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(-0.5*a, -0.5*b), point2=(0.5*a, 0.5*b))
    mdb.models[model].Part(name=MatrixPartName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = mdb.models[model].parts[MatrixPartName]
    p.BaseSolidExtrude(sketch=s1, depth=fiberLength)
    s1.unsetPrimaryObject()
    del mdb.models[model].sketches['base']
    
    # 装配
    assem = mdb.models[model].rootAssembly
    assem.DatumCsysByDefault(CARTESIAN)
    p = mdb.models[model].parts[FiberPartName]
    fiber=assem.Instance(name=FiberInstanceName, part=p, dependent=ON)
    p = mdb.models[model].parts[MatrixPartName]
    matrix=assem.Instance(name=MatrixInstanceName, part=p, dependent=ON)
    
    assem.InstanceFromBooleanMerge(name=RVEPartName, instances=(fiber,matrix), keepIntersections=ON,originalInstances=SUPPRESS, domain=GEOMETRY)
    
    p = mdb.models[model].parts[RVEPartName]
    f = p.faces
    outFace=[]
    for i in f:
        "循环所有face"
        center=i.getCentroid()
        center=center[0]
        # center=((x, y, z),)
        # 判断face是否在matrix区域内。
        if -0.5*a<=center[0]<=0.5*a and -0.5*b<=center[1]<=0.5*b and 0<=center[2]<=fiberLength:
            # 在，跳过
            continue
        else:
            # 不在，删除
            outFace.append(i)
    p.RemoveFaces(faceList =outFace, deleteCells=False)
    p.regenerate()
    mdb.models[model].rootAssembly.regenerate()

def funKernel(vfr,a,b,r,lmax,lmin,N,dxfFile,Cae_WorkDir,fiberLength,
            model,FiberPartName,MatrixPartName,FiberInstanceName,MatrixInstanceName,
            RVEPartName,dxflib):
    import sys
    vf0=(math.pi*r*r)/(a*b)
    a0=a/10
    b0=b/10
    sys.path.append(dxflib)
    from dxfwrite import DXFEngine as dxf
    # show informations
    ShowInfo(r,a,b,lmax,lmin,vf0,vfr,dxfFile)
    # get RVE object
    fibers=RVE(vfr,vf0,a,b,a0,b0,r,lmax,lmin,N)
    # From RVE object to Dxf file
    Draw2DXF(fibers,os.path.join(Cae_WorkDir,dxfFile),a,b)
    # abaqus do
    DXF2ABAQUS(fiberLength,a,b,model,FiberPartName,dxfFile,
                MatrixPartName,FiberInstanceName,MatrixInstanceName,RVEPartName)