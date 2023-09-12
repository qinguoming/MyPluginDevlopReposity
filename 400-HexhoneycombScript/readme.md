
> python version : 2.7.15
> 修改日期：2023/09/12

使用前须安装好dxfwrite库,如果要在abaqus中运行，需要把dxfwrite所在路径添加到`sys.path`,即：
```py
# 将库路径添加到path
import sys
sys.path.append('C:\Python27\Lib\site-packages')
```

然后设定参数：
+ DXF_FILE : 输出dxf文件名
+ x,y : 蜂窝结构基准点坐标(x,y)
+ r : 六边形的大小
+ horizon_num : 水平方向阵列总数
+ vertical_num : 竖直方向阵列总数

运行脚本后，会生成一个.dxf文件。在abaqus中导入该文件，拉伸即可得到几何模型。

![img](https://img2023.cnblogs.com/blog/2026433/202309/2026433-20230912114519316-1569746848.png)

![img](https://img2023.cnblogs.com/blog/2026433/202309/2026433-20230912114600877-752919118.png)

