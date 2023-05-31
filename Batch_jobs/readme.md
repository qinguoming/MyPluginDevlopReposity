# batch jobs plugin version feature

[TOC]

## V1

有两个工作模式：mode 1 和mode 2，用于应对三种情况：
1. 已经在ABAQUS/CAE中完成了有限元模型设置，job 参数已经设置完毕，需要批量提交。
2. 目前手里没有.cae模型，只有.inp文件。需要再设置job的参数，然后才批量提交。
3. 手里有.inp文件,不需要再设置job的参数，直接批量提交。

### 情况1 

针对情况1，建议用mode 1。只要勾选mode1就行，插件将提交ABAQUS/CAE左侧模型树中**全部的job**.因此，任何job的设置都要提前设置好。

### 情况2

针对情况2，先用mode2(**mode 1就不要选中了**)批量创建job，再用mode1批量提交。
具体流程：
+ inp文件全部放到一个文件夹下(**路径全英文**)，启用mode 2,勾选 only inp file 和 create job but not run 两个选项。
+ 用路径选项，选择其中一个inp文件。
+ 接下来可以在插件界面设置一些简单的参数：处理器数量，结果文件格式，分析类型（full analysis或cover）,多核心模式。更多的参数设置由于要在ABAQUS/CAE中设置（如子程序路径等）
+ 点击apply，稍后每个inp就会创建一个相应的job.
+ 启用mode 1,关掉mode 2.点击OK。

### 情况3

针对情况3，和情况2一样。先用mode2(**mode 1就不要选中了**)批量创建job，再用mode1批量提交。
具体流程：
+ inp文件全部放到一个文件夹下(**路径全英文**)，启用mode 2,勾选 only inp file 和 create job but not run 两个选项。
+ 用路径选项，选择其中一个inp文件。
+ 接下来可以在插件界面设置一些简单的参数：处理器数量，结果文件格式，分析类型（full analysis或cover）,多核心模式。更多的参数设置由于要在ABAQUS/CAE中设置（如子程序路径等）
+ 点击apply，稍后每个inp就会创建一个相应的job.
+ **手动在ABAQUS/CAE修改job。**
+ 启用mode 1,关掉mode 2.点击OK。

### 参数说明

![img](https://img2023.cnblogs.com/blog/2026433/202305/2026433-20230531145110782-502150040.png)


