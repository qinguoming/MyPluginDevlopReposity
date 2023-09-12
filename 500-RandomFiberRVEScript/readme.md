> python version: 2.7.15
> 修改日期 ：20230912

abaqus的python2.7环境中自带了matplotlib，但缺少了绘图功能，需要另外安装一个完整的matplotlib.

第一步，本地安装一个python环境，然后安装好dxfwrite库和matplotlib库，在脚本RseFiberGenerate的6、7、8行代码替换为自己的路径

```py
import sys
sys.path.append('dxfwirte库和matplotlib库的路径')
sys.path.append('abaqusConstants.pyc文件的所在目录')
```

第二步，设定参数，有关变量的含义已经在脚本中说明。

第三步，在脚本最后，找到如下代码：
```py
# 注意：DXF2ABAQUS()和ShowRVE()不能同时存在！！
# 输出一些设定信息
# ShowInfo()
# # 返回Rve对象
# fibers=RVE()
# # 使用matplotlib绘制Rve对象
# ShowRVE(fibers)
# # 将rve对象输出到dxf文件中
# Draw2DXF(fiberlist=fibers,dxfFile=os.path.join(Cae_WorkDir,dxfFile))
```
将注释取消，运行代码。

![img](https://img2023.cnblogs.com/blog/2026433/202309/2026433-20230912135923389-484400804.png)

将会得到如下的结果，可以预览生成的情况。如果不满意重新运行一次就会刷新（dxf文件也相应重画）。

![img](https://img2023.cnblogs.com/blog/2026433/202309/2026433-20230912140209761-411607980.png)

第四步，得到对RVE纤维分布满意后，将刚才的代码恢复注释，激活DXF2ABQUS()函数，即：

![img](https://img2023.cnblogs.com/blog/2026433/202309/2026433-20230912140503419-387949795.png)

打开abaqus，将工作目录设定到Cae_WorkDir变量的路径。然后file——>Run Script——> 选择RseFiberGenerate.py ,即可得到一个RVE模型。例如：

![img](https://img2023.cnblogs.com/blog/2026433/202309/2026433-20230912140930430-2090970303.png)

