<!--
 * @描述: 
 * @版本: V1_0_0
 * @作者: LiWanglin
 * @创建时间: Do not edit
 * @最后编辑人: LiWanglin
 * @最后编辑时间: Do not Edit
 -->
# OpenCV-Python 开发手册
## 简介
### OpenCV 简介
- OpenCV（开源计算机视觉库：<http://opencv.org>）是BSD许可的开源库，由加里·布拉德斯基 (Gray Bradsky) 于 1999 年创立，第一版于2000年问世。它轻量级而且高效——由一系列 C 函数和少量 C++ 类构成，可以运行在Linux、Windows和Mac OS操作系统上，同时又提供了Python、Ruby、MATLAB等语言的接口，实现了图像处理和计算机视觉方面的很多通用算法。
最新版本是 4.1.2 ，2019 年 10 月发布。

- OpenCV目前的应用领域
  - 人机互动
  - 物体识别
  - 图像分割
  - 人脸识别
  - 动作识别
  - 运动跟踪
  - 机器人
  - 运动分析
  - 机器视觉
  - 结构分析
  - 汽车安全驾驶

 ### OpenCV-Python 简介
- OpenCV-Python是OpenCV的Python API，旨在解决计算机视觉问题的Python绑定库。

- OpenCV-Python使用了 Numpy ，这是一个高度优化的库，用于使用 MATLAB 风格的语法进行数值运算。所有 OpenCV 数组结构都与 Numpy 数组相互转换。这也使与使用 Numpy 的其他库（例如 SciPy 和 Matplotlib ）的集成变得更加容易。
  
## 快速入手

## 入门篇
### 构造 OpenCV-Pyhton 开发环境
#### 1. 安装Anaconda  
Anaconda指的是一个开源的 Python 发行版本，其包含了conda、Python 等180多个科学包及其依赖项。通过安装 Anaconda ，能够大量减少配置Python环境的时间，减少许多不必要的麻烦。  
- 下载 Anaconda   
进入Anaconda官方网站 <https://www.anaconda.com/distribution> 下载相对的版本。  
![avatar](https://raw.githubusercontent.com/WanglinLi595/Save_Markdown_Picture/master/OpenCV-Python%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C/anaconda.png)  
选择 Python3.7 , 64 位版下载。  

- 安装 Anaconda  
在 Anaconda 的安装过程中，一般都是点击下一步就可以了。但有个地方要注意：
![安装Anaconda](https://raw.githubusercontent.com/WanglinLi595/Save_Markdown_Picture/master/OpenCV-Python%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C/install_anaconda.png)    
画红圈的地方要勾选，将 Anaconda 添加到环境变量。

- 为Anaconda配置清华镜像源  
Anaconda 默认的镜像源都在国外，访问不但速度慢，而且经常不稳定。在国内使用的话，把 Anaconda 的镜像源配置为清华镜像源，不仅访问稳定，而且下载速度快，非常适合下载安装 Python 的各种函数库。  
在cmd下运行命令：conda config --set show_channel_urls yes，在用户目录下生成 .condarc 文件。  
修改.condarc文件里面的内容：
```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

- 修改Aoaconda的Python版本  
由于Python-3.7版本还没有经过系统的测试，可能存在不稳定的情况，为了避免这种情况。所以我们须要更换稳定的版本，在这里，我们选用经过系统测试的Python-3.6版本。  
在cmd里面输入：conda install python=3.6 将 Aoaconda 的 Python 版本由 3.7 版本变更为 3.6 版本。  
![Python-version](https://raw.githubusercontent.com/WanglinLi595/Save_Markdown_Picture/master/OpenCV-Python%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C/python-version.png)    
下载完成后，可以在cmd输入ipython查看python版本.
![Python-version2](https://raw.githubusercontent.com/WanglinLi595/Save_Markdown_Picture/master/OpenCV-Python%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C/python-version2.png
)  
从图中可以看到，当前python版本为3.6.9。

#### 2. 安装OpenCV-Python
- 下载 OpenCV-Python  
进入网站：<https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv> ，选择 opencv_python-4.1.2+contrib-cp36-cp36m-win_amd64.whl 文件开始下载。
![OpenCV-python](https://raw.githubusercontent.com/WanglinLi595/Save_Markdown_Picture/master/OpenCV-Python%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C/OpenCV-Python.png)  
- 安装OpenCV-Python  
下载完成后，在cmd输入：pip install + opencv_python-4.1.2+contrib-cp36-cp36m-win_amd64.whl 文件的绝对路径
![OpenCV-python2](https://raw.githubusercontent.com/WanglinLi595/Save_Markdown_Picture/master/OpenCV-Python%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C/OpenCV-Python2.png)  
如果出现：Successfully installed opencv-python-4.1.2+contrib，则表示安装成功。

- 版本验证  
进入 ipython ，输入：
```python
>>> import cv2 
>>> cv2.__version__
```
可以查看 OpenCV-Python 版本
![OpenCV-python3](https://raw.githubusercontent.com/WanglinLi595/Save_Markdown_Picture/master/OpenCV-Python%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C/OpenCV-Python3.png)  
从图中可以看出，当前 OpenCV-Python 版本为4.1.2.


## 进阶篇

## API