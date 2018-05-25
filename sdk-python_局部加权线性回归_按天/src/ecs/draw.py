# coding=utf-8
#先加载画图需要用的包
import matplotlib as mpl
import matplotlib.pyplot as plt

def draw(points):
    x=[]
    y=[]
    for point in points:
        x.append(point[0])
        y.append(point[1])
    mpl.style.use('ggplot')
    plt.figure(figsize=(12,6))
    
    plt.scatter(x,y)
    # 保存图片到指定路径  
    #plt.savefig("../data/HeightAndWeight.png")
    # 展示
    plt.show()
