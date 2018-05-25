# coding=utf-8
import pymatrix
import math

#################################################
##
##
##
##
#############################################
def cumsum(arr):
    sum = 0
    res = []
    for a in arr:
        sum = sum + a
        res.append(sum)
    return res

####################################################################
## N：要预测的天数
## train_data：训练集，二维数组，其行数是测试集的天数，列数是虚拟机的规格数
## 
## 返回值：二维数组，行数是虚拟机的规格数，列数是预测的天数
####################################################################
def yuce(N,train_data):
    #train_data = pymatrix.matrix(train_data_list)
    #print(train_data)
    # size[0]是行数 size[1]是列数
    seq_len,flavor_num = train_data.shape()
    #print(seq_len,flavor_num)
    res = []
    for i in range(1,flavor_num+1,1):
        #print(u"===规格"+str(i)+"===")
        seq_fi = train_data.colAt(i)
        #print(u"原始序列"+str(seq_fi))
        seq_fi = cumsum(seq_fi)
        #print(u"累加序列"+str(seq_fi))
        if(seq_fi[-1]==0):
            res.append(0)
            print(res)
            continue
        #print(seq_fi)
        z = [[0]]*(seq_len-1)
        #print(u"白化之前："+str(z))
        for j in range(0,seq_len-1,1):
            z[j] = [0.5*(float(seq_fi[j])+float(seq_fi[j+1]))]
        #print(u"白化背景之后： "+str(len(z))+str(z))
        z = pymatrix.matrix(z)
        print("z="+str(z))
        z = z.numberSubMatrix(0)
        print(u"-z="+str(z))
        B = [[1]]*(seq_len-1)
        B = pymatrix.matrix(B)
        B = z.heBing(B)
        #print(u"合并矩阵之后："+ str(B))
        
        u = B.transpose()*B
        #print(u"B的转置 "+str(B.transpose()))
        #print(u"B原来 "+str(B))
        u = u.inverse()
        u = u * B.transpose()
        #print(u)
        #print(train_data)
        #print(u"子矩阵 "+str(train_data.subMatrix(2,seq_len,i,i)))
        u = u * (train_data.subMatrix(2,seq_len,i,i))
        #print("u= "+str(u))
        u1 = u[0][0]
        u2 = u[1][0]
        #print(u1,u2)
        left = train_data[0][i-1] - u2/u1
        #print("left= "+str(left))
        #print("u1= "+str(u1))
        right = u2/u1
        
        forecast1 = []
        for t in range(seq_len-1,seq_len+N,1):
            forecast1.append(t)
        for i in range(0,len(forecast1),1):
            forecast1[i] = (-u1)*forecast1[i]
        for i in range(0,len(forecast1),1):
            forecast1[i] = math.exp(forecast1[i])
        for i in range(0,len(forecast1),1):
            forecast1[i] = left * forecast1[i]
        for i in range(0,len(forecast1),1):
            forecast1[i] = forecast1[i] + right

        #print(forecast1[-1]-forecast1[0])
        print(forecast1)
        rrr = abs(round(forecast1[-1]-forecast1[0]))
        if(rrr>40):
            rrr = 40
        res.append(int(rrr))
        print(res)
        #exchange=[]
        #for i in range(1,len(forecast1),1):
        #    exchange.append(forecast1[i]-forecast1[i-1])
    return res

if __name__ == "__main__":
    N = 7
    train_data=[[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9]]
    print(yuce(N,train_data))
    #arr = [1,2,54,2,5]
    #print(sum(arr))
    #print(cumsum(arr))