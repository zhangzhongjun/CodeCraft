# coding=utf-8
import time
from math import *
import fluth_data
import pymatrix
import memory_alloction
#一天的秒数
nd = 1*24*60*60
#一小时的秒数
nh = 1*60*60
#一分钟的秒数
nm = 1*60
#一秒钟的秒数
ns = 1

#使用最后几条的记录
num_jilu = 450

#################################################
# 注意ecs_lines里面的每一个元素都是带回车换行符的
#
#
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
        
    #########训练集的时间跨度#####训练第一天的0点 预测第一天的0点##################
    ecs_first_date_zero = ecs_lines[0].split("\t")[2].strip().split()[0]+" "+"00:00:00"
    ecs_first_date_zero = time.strptime(ecs_first_date_zero, "%Y-%m-%d %H:%M:%S")
    input_first_date_zero = input_lines[-2].strip().split()[0]+" "+"00:00:00"
    input_first_date_zero = time.strptime(input_first_date_zero, "%Y-%m-%d %H:%M:%S")
    kuadu_first_last_day = (time.mktime(input_first_date_zero)-time.mktime(ecs_first_date_zero))/nd
    kuadu_first_last_day = int(kuadu_first_last_day)
    #print(u"时间跨度为"+str(kuadu_first_last_day))
    #########训练集的时间跨度#####训练第一天的0点 预测第一天的0点##################
    
    
    ##########获取训练集中的数据 行数为虚拟机的规格 列数是天数##################
    ecs_xunlian = []
    for i in range(30):
        t = []
        for j in range(kuadu_first_last_day):
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
        ecs_xunlian[ecs_now_no][ecs_kuadu_first_now_day] = ecs_xunlian[ecs_now_no][ecs_kuadu_first_now_day] + 1
        
    '''    
    print(u"训练集中的数据")
    print(len(ecs_xunlian))
    print(len(ecs_xunlian[0]))
    temp = pymatrix.matrix(ecs_xunlian)
    print(temp)
    ''' 
    ##########获取训练集中的数据 行数为虚拟机的规格 列数是天数##################
    
    


    ###############去噪的代码################
    #获得要预测的规格
    input_num = int(input_lines[2].strip())
    input_nos = []
    for i in range(input_num):
        input_line = input_lines[i+3]
        input_no = input_line.strip().split()[0].replace("flavor","")
        input_no = int(input_no)
        input_nos.append(input_no)
    train_data = fluth_data.quZao2(ecs_xunlian,input_nos)
    ##############去噪的代码################
    
    
    ###########获得预测跨度####################
    #预测的第一天 预测的最后一天
    input_first_date = input_lines[-2].strip()
    input_first_date = time.strptime(input_first_date, "%Y-%m-%d %H:%M:%S")
    input_last_date = input_lines[-1].strip()
    input_last_date = time.strptime(input_last_date, "%Y-%m-%d %H:%M:%S")
    
    kuadu_first_last_day = (time.mktime(input_last_date)-time.mktime(input_first_date))/nd
    kuadu_first_last_day = int(kuadu_first_last_day)
    #print(u"时间跨度为："+str(kuadu_first_last_day))
    ###########获得预测跨度####################
    
    ###############获得虚拟机名和预测台数的对应####################
    yuce_flvorname_flavornum_s = {}
    #print(u"===去噪之后===")
    for t in train_data:
        name = "flavor"+str(t)
        num = sum(train_data[t][:30:1])
        num = float(num)/float(30)*float(kuadu_first_last_day)
        num = ceil(num)
        yuce_flvorname_flavornum_s[name] = int(num)
        #print(str(t)+" "+str(train_data[t]))
        #print(u"预测值："+str(num))
    print("==============")
    ######################################################

    ###################获得names cpus mems这三个序列######################
    cpus = []
    mems = []
    names = []
    #input文件中需要预测的虚拟机[("flavor1",12,1024),("flavor1",12,1024)]
    input_xuNiJis = []
    i = 3
    while(i<3 + int(input_lines[2].strip())):
        input_now_flavor_name = input_lines[i].strip().split(" ")[0]
        input_now_flavor_CPU = int(input_lines[i].strip().split(" ")[1])
        input_now_flavor_MEM = int(input_lines[i].strip().split(" ")[2])/1024
        input_now_flavor = [input_now_flavor_name,input_now_flavor_CPU,input_now_flavor_MEM]
        input_xuNiJis.append(input_now_flavor)
        nums = yuce_flvorname_flavornum_s[input_now_flavor_name]
        for j in range(nums):
            names.append(input_now_flavor_name)
            cpus.append(input_now_flavor_CPU)
            mems.append(input_now_flavor_MEM)
        i = i + 1
    
    
    print(names)
    print(mems)
    print(cpus)
    ###################获得names cpus mems这三个序列######################
    
    ################# 获得物理机的规格###############
    input_wuLiJi_cpu = int(input_lines[0].split(" ")[0])
    input_wuLiJi_mem = int(input_lines[0].split(" ")[1])
    ########################获得物理机的规格#########
    
    
    ##################### 优化的维度 装箱 输出结果#####################
    input_weidu = input_lines[3+int(input_lines[2].strip())+1].strip()
    if(input_weidu=="CPU"):
        zx_wuLiJis,_ = memory_alloction.get_memory_allocation(input_wuLiJi_cpu,input_wuLiJi_mem,cpus,mems,names)
    elif(input_weidu=="MEM"):
        zx_wuLiJis,_ = memory_alloction.get_memory_allocation(input_wuLiJi_mem,input_wuLiJi_cpu,mems,cpus,names)
    else:
        print("出错了，别玩了")
    print(zx_wuLiJis)
    #开始输出结果
    result=[]
    sum_t = 0
    for input_xuNiJi in input_xuNiJis:
        input_xuNiJi_name = input_xuNiJi[0]
        input_xuNiJi_num = yuce_flvorname_flavornum_s.get(input_xuNiJi_name)
        sum_t = sum_t + input_xuNiJi_num
        result.append(input_xuNiJi_name+" "+str(input_xuNiJi_num))
    result.insert(0,str(sum_t))
    result.append("")
    result.append(len(zx_wuLiJis))
    print(result)
    for i in range(0,len(zx_wuLiJis),1):
        zx_wuLiJi = zx_wuLiJis[i]
        sss = str(i+1)
        temp = {}
        for xuNiJi in zx_wuLiJi :
            if(temp.has_key(xuNiJi)):
                temp[xuNiJi] = temp[xuNiJi] + 1
            else:
                temp[xuNiJi] = 1
        print(temp)
        for name in temp:
            sss = sss+" "+name+" "+str(temp[name])
        print(sss)
        result.append(sss.strip())
    
    return result
    ##################### 优化的维度 装箱 输出结果#####################