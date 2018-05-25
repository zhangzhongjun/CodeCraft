# coding=utf-8
import time
from math import *
from pymatrix import *
import qz
import yuce
#一天的秒数
nd = 1*24*60*60

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
        
    #训练第一天的0点 预测第一天的0点
    ecs_first_date_zero = ecs_lines[0].split("\t")[2].strip().split()[0]+" "+"00:00:00"
    ecs_first_date_zero = time.strptime(ecs_first_date_zero, "%Y-%m-%d %H:%M:%S")
    input_first_date_zero = input_lines[-2].strip().split()[0]+" "+"00:00:00"
    input_first_date_zero = time.strptime(input_first_date_zero, "%Y-%m-%d %H:%M:%S")
    kuadu_first_last_day = (time.mktime(input_first_date_zero)-time.mktime(ecs_first_date_zero))/nd
    kuadu_first_last_day = int(kuadu_first_last_day)
    ecs_xunlian = []
    for i in range(kuadu_first_last_day):
        t = []
        for j in range(30):
            t.append(0)
        ecs_xunlian.append(t)

    for ecs_line in ecs_lines:
        ecs_line = ecs_line.strip()
        ecs_now_name = ecs_line.split("\t")[1]
        ecs_now_no = int(ecs_now_name.replace("flavor",""))

        ecs_now_date = ecs_line.split("\t")[2]
        ecs_now_date = time.strptime(ecs_now_date, "%Y-%m-%d %H:%M:%S")
        #print(ecs_now_name+" "+str(ecs_now_no)+" "+str(ecs_now_date))
        ecs_kuadu_first_now_day = (time.mktime(ecs_now_date)-time.mktime(ecs_first_date_zero))/nd
        ecs_kuadu_first_now_day = int(ecs_kuadu_first_now_day)
        ecs_xunlian[ecs_kuadu_first_now_day][ecs_now_no] = ecs_xunlian[ecs_kuadu_first_now_day][ecs_now_no] + 1
    for t in ecs_xunlian:
        print(t)
    print(len(ecs_xunlian))
    print(len(ecs_xunlian[0]))
    
    # 获得要预测的规格
    input_num = int(input_lines[2].strip())
    input_nos = []
    for i in range(input_num):
        input_line = input_lines[i+3]
        input_no = input_line.strip().split()[0].replace("flavor","")
        input_no = int(input_no)
        input_nos.append(input_no)
    print(input_nos)
    train_data = qz.quZao2(ecs_xunlian,input_nos)
    for t in train_data:
        xArr = []
        yArr = []
    
    
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