# coding=utf-8
###########################
#
#
# 局部加权线性回归函数
# testPoint : 要测试的点
# xArr : [[1,1],[1,2],[1,3],[1,4],[1,5]]
# yArr : [[1,2,3,4,5]]
# k : 一个参数
#############################
def lwlr(testPoint,xArr,yArr,k):
    # 读入数据并创建所需矩阵
    xMat = matrix(xArr)
    yMat = matrix(yArr).t()
    # np.shape()函数计算传入矩阵的维数
    m = yMat.shape()[0]
    # 权重，创建对角矩阵，维数与xMat维数相同
    weights = matrix(m)     # m维的单位对角矩阵

    '''
    权重矩阵是一个方阵,阶数等于样本点个数。也就是说,该矩阵为每个样本点初始
        化了一个权重。接着,算法将遍历数据集,计算每个样本点对应的权重值,
    '''
    for j in range(m):
        # 计算预测点和训练集的差距
        diffMat = xMat.rowvec(j)
        diffMat = diffMat.numberSubMatrix(testPoint)
        # 采用高斯核函数进行权重赋值，样本附近点将被赋予更高权重
        tt = (diffMat*(diffMat.t()))[0][0]
        weights[j][j] = exp(tt/(-2.0*(k**2)))
    # (2*2) = (2*n) * ( (n*n)*(n*2) )
    xTx = xMat.t() * (weights * xMat)     
    if xTx.is_invertible() == False:
        #print ("This matrix is singular,cannot do inverse")
        return
    # (2*1) = (2*2) * ( (2*n) * (n*n) * (n*1))
    ws = xTx.inverse() * (xMat.t() * (weights * yMat))    
    #print(ws)
    return testPoint * ws
##################################
##
##
## 样本点依次做局部加权
##
## testArr:要测试的所有的点
## xArr : [[1,1],[1,2],[1,3],[1,4],[1,5]]
## yArr : [[1,2,3,4,5]]
## k : 一个参数
######################################
def lwlrTest(testArr,xArr,yArr,k):
    
    m = len(testArr)
    yHat = []
    # 为样本中每个点，调用lwlr()函数计算ws值以及预测值yHat
    for i in range(m):
        #print(u"正在预测点："+str(testArr[i]))
        #print(u"预测出："+str(lwlr(testArr[i],xArr,yArr,k)))
        yHat.append(round(lwlr(testArr[i],xArr,yArr,k)[1][0]))
    return yHat
    
