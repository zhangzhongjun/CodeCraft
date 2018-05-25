# coding=utf-8
import time
from math import *
from pymatrix import *
#from draw import draw
#一天的秒数
nd = 1*24*60*60
#一小时的秒数
nh = 1*60*60
#一分钟的秒数
nm = 1*60
#一秒钟的秒数
ns = 1

#################################################
# 注意ecs_lines里面的每一个元素都是带回车换行符的
#
#################################################
def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print ('ecs information is none')
        return result
    if input_lines is None:
        print ('input file information is none')
        return result
        
    # 训练集的时间跨度
    ecs_first_date = time.strptime(ecs_lines[0].split("\t")[2].strip(), "%Y-%m-%d %H:%M:%S")
    ecs_last_date = time.strptime(ecs_lines[-1].split("\t")[2].strip(), "%Y-%m-%d %H:%M:%S")
    ecs_kuadu_first_last_hour = (time.mktime(ecs_last_date)-time.mktime(ecs_first_date))/nh
    ecs_kuadu_first_last_hour = int(ecs_kuadu_first_last_hour) + 1
    
    # input文件中的物理机的规格
    input_wuLiJi_cpu = int(input_lines[0].split(" ")[0])
    input_wuLiJi_mem = int(input_lines[0].split(" ")[1])
    # 需要预测的时间跨度
    input_first_date = time.strptime(input_lines[3+int(input_lines[2].strip())+3].strip(), "%Y-%m-%d %H:%M:%S")
    input_last_date = time.strptime(input_lines[3+int(input_lines[2].strip())+4].strip(), "%Y-%m-%d %H:%M:%S")
    input_kuadu_first_last_hour = (time.mktime(input_last_date)-time.mktime(input_first_date))/nh
    input_kuadu_first_last_hour = int(input_kuadu_first_last_hour) + 1
        
    #input文件中需要预测的虚拟机[("flavor1",12,1024),("flavor1",12,1024)]
    input_xuNiJis = []
    i = 3
    while(i<3 + int(input_lines[2].strip())):
        input_now_flavor_name = input_lines[i].strip().split(" ")[0]
        input_now_flavor_CPU = int(input_lines[i].strip().split(" ")[1])
        input_now_flavor_MEM = int(input_lines[i].strip().split(" ")[2])
        input_now_flavor = [input_now_flavor_name,input_now_flavor_CPU,input_now_flavor_MEM]
        input_xuNiJis.append(input_now_flavor)
        i = i + 1
    
    # 优化的维度
    input_weidu = input_lines[3+int(input_lines[2].strip())+1].strip()
    #print(input_xuNiJis)
        
    
    # 所有规格的虚拟机的请求情况 行：30代表虚拟机的种类数 列：训练集的时间跨度
    ecs_nums = {"flavor1":[0]*ecs_kuadu_first_last_hour,"flavor2":[0]*ecs_kuadu_first_last_hour,"flavor3":[0]*ecs_kuadu_first_last_hour,"flavor4":[0]*ecs_kuadu_first_last_hour,"flavor5":[0]*ecs_kuadu_first_last_hour,"flavor6":[0]*ecs_kuadu_first_last_hour,"flavor7":[0]*ecs_kuadu_first_last_hour,"flavor8":[0]*ecs_kuadu_first_last_hour,"flavor9":[0]*ecs_kuadu_first_last_hour,"flavor10":[0]*ecs_kuadu_first_last_hour,"flavor11":[0]*ecs_kuadu_first_last_hour,"flavor12":[0]*ecs_kuadu_first_last_hour,"flavor13":[0]*ecs_kuadu_first_last_hour,"flavor14":[0]*ecs_kuadu_first_last_hour,"flavor15":[0]*ecs_kuadu_first_last_hour,"flavor16":[0]*ecs_kuadu_first_last_hour,"flavor17":[0]*ecs_kuadu_first_last_hour,"flavor18":[0]*ecs_kuadu_first_last_hour,"flavor19":[0]*ecs_kuadu_first_last_hour,"flavor20":[0]*ecs_kuadu_first_last_hour,"flavor21":[0]*ecs_kuadu_first_last_hour,"flavor22":[0]*ecs_kuadu_first_last_hour,"flavor23":[0]*ecs_kuadu_first_last_hour,"flavor24":[0]*ecs_kuadu_first_last_hour,"flavor25":[0]*ecs_kuadu_first_last_hour,"flavor26":[0]*ecs_kuadu_first_last_hour,"flavor27":[0]*ecs_kuadu_first_last_hour,"flavor28":[0]*ecs_kuadu_first_last_hour,"flavor29":[0]*ecs_kuadu_first_last_hour,"flavor30":[0]*ecs_kuadu_first_last_hour}

    for ecs_line in ecs_lines:
        ecs_line = ecs_line.strip()
        
        ecs_now_date = time.strptime(ecs_line.split("\t")[2].strip(), "%Y-%m-%d %H:%M:%S")
        #计算时间跨度
        ecs_kuadu_first_now_hour = (time.mktime(ecs_now_date)-time.mktime(ecs_first_date))/nh
        ecs_kuadu_first_now_hour = int(ecs_kuadu_first_now_hour)
        ecs_now_name = ecs_line.split("\t")[1]
        #print(ecs_now_name,ecs_kuadu_first_now_hour)
        ecs_nums[ecs_now_name][ecs_kuadu_first_now_hour] = ecs_nums[ecs_now_name][ecs_kuadu_first_now_hour] + 1
    #print(ecs_nums)
    
    # 训练集所有规格的虚拟机的请求数的和
    ecs_points = {"flavor1":[],"flavor2":[],"flavor3":[],"flavor4":[],"flavor5":[],"flavor6":[],"flavor7":[],"flavor8":[],"flavor9":[],"flavor10":[],"flavor11":[],"flavor12":[],"flavor13":[],"flavor14":[],"flavor15":[],"flavor16":[],"flavor17":[],"flavor18":[],"flavor19":[],"flavor20":[],"flavor21":[],"flavor22":[],"flavor23":[],"flavor24":[],"flavor25":[],"flavor26":[],"flavor27":[],"flavor28":[],"flavor29":[],"flavor30":[]}
    for input_xuNiJi in input_xuNiJis:
        input_xuNiJi_name = input_xuNiJi[0]
        input_xuNiJi_CPU = input_xuNiJi[1]
        input_xuNiJi_MEM = input_xuNiJi[2]
        # 该种型号的虚拟机请求情况
        ecs_num = ecs_nums[input_xuNiJi_name]
        temp_sum = 0
        temp_last_sum = 0
        for i in range(0,len(ecs_num),1):
            temp_sum = temp_sum + ecs_num[i]
            if(temp_sum != temp_last_sum):
                ecs_points[input_xuNiJi_name].append((i,temp_sum))
                temp_last_sum = temp_sum
        
    #print(ecs_points)
    #draw(ecs_points["flavor3"])
    # 开始预测
    yuce_flvorname_flavornum_s = {"flavor1":0,"flavor2":0,"flavor3":0,"flavor4":0,"flavor5":0,"flavor6":0,"flavor7":0,"flavor8":0,"flavor9":0,"flavor10":0,"flavor11":0,"flavor12":0,"flavor13":0,"flavor14":0,"flavor15":0,"flavor16":0,"flavor17":0,"flavor18":0,"flavor19":0,"flavor20":0,"flavor21":0,"flavor22":0,"flavor23":0,"flavor24":0,"flavor25":0,"flavor26":0,"flavor27":0,"flavor28":0,"flavor29":0,"flavor30":0}
    yuce_yuceFirst_xunliangFirst_hour = (time.mktime(input_first_date)-time.mktime(ecs_first_date))/nh
    yuce_yuceFirst_xunliangFirst_hour = int(yuce_yuceFirst_xunliangFirst_hour) + 1
    yuce_yuceLast_xunliangFirst_hour = (time.mktime(input_last_date)-time.mktime(ecs_first_date))/nh
    yuce_yuceLast_xunliangFirst_hour = int(yuce_yuceLast_xunliangFirst_hour) + 1
    
    # 使用训练集来训练模型
    for input_xuNiJi in input_xuNiJis:
        input_xuNiJi_name = input_xuNiJi[0]
        
        ecs_xuNiJi_points = ecs_points[input_xuNiJi_name]
        
        #print("=============================================")
        #print ((input_xuNiJi_name)+" "+str(ecs_xuNiJi_points))
        xArr = []
        yArr = [[]]
        for ecs_xuNiJi_point in ecs_xuNiJi_points:
            xArr.append([1,ecs_xuNiJi_point[0]])
            yArr[0].append(ecs_xuNiJi_point[1])
        #print(u"训练集x: "+str(xArr))
        #print(u"测试集y: "+str(yArr))
        
        values = lwlrTest([yuce_yuceFirst_xunliangFirst_hour,yuce_yuceLast_xunliangFirst_hour], xArr, yArr, k = 450)
        
        yuce_value = values[1] - values[0]
        yuce_value = max(yuce_value,0)
        yuce_value = int(yuce_value)
        yuce_flvorname_flavornum_s[input_xuNiJi_name] = yuce_value
        
    
    # 开始装箱
    zx_yuce_xuNiJis = []
    for input_xuNiJi in input_xuNiJis:
        input_xuNiJi_name = input_xuNiJi[0]
        input_xuNiJi_CPU = input_xuNiJi[1]
        input_xuNiJi_MEM = input_xuNiJi[2]
        
        yuce_xuNiJi_num = yuce_flvorname_flavornum_s.get(input_xuNiJi_name)
        for i in range(0,yuce_xuNiJi_num,1):
            yuce_xuNiJi = (input_xuNiJi_name,input_xuNiJi_CPU,input_xuNiJi_MEM)
            zx_yuce_xuNiJis.append(yuce_xuNiJi)
    #print(zx_yuce_xuNiJis)
    zx_yuce_xuNiJis = sortedDictByWeidu(zx_yuce_xuNiJis,input_weidu)
    #print(zx_yuce_xuNiJis)
    
    # 开始装箱
    zx_wuLiJis = ff(zx_yuce_xuNiJis,input_wuLiJi_cpu,input_wuLiJi_mem*1024)
    
    #开始输出结果
    result=[]
    sum = 0
    for input_xuNiJi in input_xuNiJis:
        input_xuNiJi_name = input_xuNiJi[0]
        input_xuNiJi_num = yuce_flvorname_flavornum_s.get(input_xuNiJi_name)
        sum = sum + input_xuNiJi_num
        result.append(input_xuNiJi_name+" "+str(input_xuNiJi_num))
    result.insert(0,str(sum))
    result.append("")
    result.append(len(zx_wuLiJis))
    
    for zx_wuLiJi in zx_wuLiJis:
        sss = ""
        sss = sss + str(zx_wuLiJi[0]) +" "
        for xuNiJi in (zx_wuLiJi[3::1]) :
            sss = sss + xuNiJi[0]
            sss = sss + " "
            sss = sss + str(xuNiJi[1]) + " "
        result.append(sss.strip())
    
    return result
    #return ["t1","t2","t3"]

##############################################
# zx_yuce_xuNiJis 最好先排过序的，先放“西瓜”，后放“芝麻”，效果更好
#
#
#
################################################
def ff(zx_yuce_xuNiJis,input_wuLiJi_cpu,input_wuLiJi_mem):
    no = 1
    zx_wuLiJis = []
    zx_wuLiJis_first = [no,input_wuLiJi_cpu,input_wuLiJi_mem]
    zx_wuLiJis.append(zx_wuLiJis_first)
    #对每一个需要装箱的虚拟机
    for zx_yuce_xuNiJi in zx_yuce_xuNiJis:
        zx_yuce_xuNiJi_name = zx_yuce_xuNiJi[0]
        zx_yuce_xuNiJi_cpu = zx_yuce_xuNiJi[1]
        zx_yuce_xuNiJi_mem = zx_yuce_xuNiJi[2]
        # 物理机列表中已经有够的了
        flag_has_good_wuLiJi = False 
        # 对已经存在的物理机
        for zx_wuLiJi in zx_wuLiJis:
            zx_wuLiJi_cpu = zx_wuLiJi[1]
            zx_wuLiJi_mem = zx_wuLiJi[2]
            if(zx_wuLiJi_cpu>=zx_yuce_xuNiJi_cpu and zx_wuLiJi_mem>=zx_yuce_xuNiJi_mem):
                flag_has_good_wuLiJi = True
                zx_wuLiJi[1] = zx_wuLiJi[1] - zx_yuce_xuNiJi_cpu
                zx_wuLiJi[2] = zx_wuLiJi[2] - zx_yuce_xuNiJi_mem
                
                # 开始检测是否已经在该物理机中
                # 该型号的虚拟机已经在物理机列表中
                flag_already_in_wuLiJi = False
                for xuNiJi in zx_wuLiJi[3::]:
                    if xuNiJi[0] == zx_yuce_xuNiJi_name:
                        xuNiJi[1] = xuNiJi[1] + 1
                        flag_already_in_wuLiJi = True
                        break
                if(flag_already_in_wuLiJi==False):
                    zx_xuNiJi_temp = [zx_yuce_xuNiJi_name,1]
                    # 将这台虚拟机放在它的物理机的后面
                    zx_wuLiJi.append(zx_xuNiJi_temp)
            #如果已经分配了，则直接跳出
            if(flag_has_good_wuLiJi==True):
                break
        # 如果已经存在的物理机没有合适的
        if(flag_has_good_wuLiJi==False):
            no = no + 1 #获得新的物理机的编号
            zx_xuNiJi_temp = [zx_yuce_xuNiJi_name,1]
            zx_wuLiJis.append([no,input_wuLiJi_cpu-zx_yuce_xuNiJi_cpu,input_wuLiJi_mem-zx_yuce_xuNiJi_mem,zx_xuNiJi_temp])
    return zx_wuLiJis

    
###########################
#
#
# 局部加权线性回归函数
# xArr : [[1,1],[1,2],[1,3],[1,4],[1,5]]
# yArr : [[1,2,3,4,5]]
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

# 样本点依次做局部加权
def lwlrTest(testArr,xArr,yArr,k):
    
    m = len(testArr)
    yHat = []
    # 为样本中每个点，调用lwlr()函数计算ws值以及预测值yHat
    for i in range(m):
        #print(u"正在预测点："+str(testArr[i]))
        #print(u"预测出："+str(lwlr(testArr[i],xArr,yArr,k)))
        yHat.append(round(lwlr(testArr[i],xArr,yArr,k)[1][0]))
    return yHat
    

###############################################################################
# 按照某个维度对list类型的数据进行排序
#
# list：待排序的变量
# weidu：按照哪个维度进行排序 CPU或MEM
#
# return：排序之后的数据，是一个list，list的每一个元素都是一个tuple
#   tuple的第一个数据是虚拟机的名字，第二个数据是CPU的信息，第三个数据是CPU的信息
################################################################################
def sortedDictByWeidu(list,weidu):
    if (weidu=="CPU"):
        list.sort(key=lambda x:x[1],reverse=True)
    elif(weidu=="MEM"):
        list.sort(key=lambda x:x[2],reverse=True)
    return list
    
###############################################################################
# 按照某个维度对list类型的数据进行排序
#
# list：待排序的变量
# weidu：按照哪个维度进行排序 CPU或MEM
#
# return：排序之后的数据，是一个list，list的每一个元素都是一个tuple
# tuple的第一个数据是虚拟机的名字，第二个数据是CPU的信息，第三个数据是MEM的信息
################################################################################
def sortedListByWeidu2(list,weidu):
    if (weidu=="CPU"):
        list.sort(key=lambda x:x[1]/x[2],reverse=True)
    elif(weidu=="MEM"):
        list.sort(key=lambda x:x[2]/x[1],reverse=True)
    else:
        print("出错了，别玩了")
    return list