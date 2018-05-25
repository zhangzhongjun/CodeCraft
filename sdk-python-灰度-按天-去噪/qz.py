# coding=utf-8
import math
import pymatrix
#################################
## 对请求数进行去噪
## arr 所有的请求
## input_nos: 要预测的规格
## 
########################
def quZao2(arr,input_nos):
    train_data=[]
    M = pymatrix.matrix(arr)
    M = M.transpose()
    for input_no in input_nos:
        temp = M.rowAt(input_no+1)
        #print(input_no,temp,type(temp))
        temp = quZao(temp)
        #print(temp)
        train_data.append(temp)
    #print(M)
    return train_data

##########################################
## 去噪的方法
##
## arr：是一个数组，代表着某种规格的虚拟机的请求数随时间的变化
##
###########################################
def quZao(arr):
    #print("数据总数："+str(len(arr)))

    #print("原始数据："+str(arr))
    diff = list([])

    for i in range(1,len(arr),1):
        diff.append(arr[i]-arr[i-1])
    diff_sum = sum(diff)

    diff_average = diff_sum/float(len(diff))
    print(u"均值："+str(diff_average))

    diff_delta = 0
    for i in range(0,len(diff),1):
        diff_delta = diff_delta + math.pow(diff[i]-diff_average,2)
    diff_delta = diff_delta/len(diff)
    #print("标准差："+str(diff_delta))
    diff_delta = math.sqrt(diff_delta)
    print(u"标准差："+str(diff_delta))

    yuzhi_high = diff_average + 1.5 * diff_delta
    yuzhi_low = diff_average - 1.5 * diff_delta
    print(u"阈值（高点）"+str(yuzhi_high))
    print(u"阈值（低点）"+str(yuzhi_low))


    for i in range(0,len(diff),1):
        if diff[i]>yuzhi_high:
            arr[i+1] = arr[i]
            #print(str(diff[i])+"偏大")
        elif diff[i]<yuzhi_low:
            arr[i] = arr[i-1]
            #print(str(diff[i])+"偏小")
        else:
            pass
            
    #print("去噪之后的数据："+str(arr))
    return arr
if __name__ == "__main__":
    arr = list([1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1])
    arr = quZao(arr)
    print(arr)