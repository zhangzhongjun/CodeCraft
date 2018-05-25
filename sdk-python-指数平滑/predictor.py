# coding=utf-8
import time
import math
import fluth_data
import pymatrix
import memory_alloction
import preprocess
#一天的秒数
nd = 1*24*60*60


#################################################
#
#
#
# 注意ecs_lines里面的每一个元素都是带回车换行符的
#
#
#
#################################################
def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        #print ('ecs information is none')
        return result
    if input_lines is None:
        #print ('input file information is none')
        return result
        
    #### 去掉所有的空行
    ecs_lines_new = []
    for ecs_line in ecs_lines:
        if(ecs_line.strip()!=""):
            ecs_lines_new.append(ecs_line)
    
    input_lines_new = []
    for input_line in input_lines:
        if(input_line.strip()!=""):
            input_lines_new.append(input_line)
            
    
    
    # 获得要预测的规格
    input_num = int(input_lines_new[1].strip())
    
    
    #训练第一天的0点 预测第一天的0点
    ecs_first_date_zero = ecs_lines_new[0].split("\t")[2].strip().split()[0]+" "+"00:00:00"
    ecs_first_date_zero = time.strptime(ecs_first_date_zero, "%Y-%m-%d %H:%M:%S")
    input_first_date_zero = input_lines_new[6+input_num].strip().split()[0]+" "+"00:00:00"
    input_first_date_zero = time.strptime(input_first_date_zero, "%Y-%m-%d %H:%M:%S")
    kuadu_first_last_day = (time.mktime(input_first_date_zero)-time.mktime(ecs_first_date_zero))/nd
    kuadu_first_last_day = int(kuadu_first_last_day)
    ##print(u"时间跨度为"+str(kuadu_first_last_day))
    # 行数为虚拟机的规格 列数是天数
    ecs_xunlian = []
    for i in range(30):
        t = []
        for j in range(kuadu_first_last_day):
            t.append(0)
        ecs_xunlian.append(t)

    for ecs_line in ecs_lines_new:
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
    
    # 获得要预测的规格
    input_num = int(input_lines_new[1].strip())
    input_nos = []
    for i in range(input_num):
        input_line = input_lines_new[i+2]
        input_no = input_line.strip().split()[0].replace("flavor","")
        input_no = int(input_no)
        input_nos.append(input_no)
    train_data = fluth_data.quZao2(ecs_xunlian,input_nos)
    
    # 增加一列0
    train_data = preprocess.pp2(train_data)

    '''
    print("======增加0之后=======")
    for t in train_data:
        print(t)
    print(len(train_data))
    print(len(train_data[0]))
    '''
    
    ###########获得预测跨度####################
    #预测的第一天 预测的最后一天
    input_first_date = input_lines_new[-2].strip()
    input_first_date = time.strptime(input_first_date, "%Y-%m-%d %H:%M:%S")
    input_last_date = input_lines_new[-1].strip()
    input_last_date = time.strptime(input_last_date, "%Y-%m-%d %H:%M:%S")
    
    kuadu_first_last_day_2 = (time.mktime(input_last_date)-time.mktime(input_first_date))/nd
    kuadu_first_last_day_2 = int(kuadu_first_last_day_2)
    #print(u"预测时间跨度为："+str(kuadu_first_last_day_2))
    ###########################################
    
    temp = math.ceil(kuadu_first_last_day_2/2.0)
    #print("temp="+str(temp))
    #分片
    train_data = preprocess.pp(train_data,temp)
    
    '''
    print(u"========分片之后============")
    for t in train_data:
        print(t)
    print(len(train_data))
    print(len(train_data[0]))
    '''
    
    ##########开始预测############################
    yuce_flvorname_flavornum_s = {}
    s1 = [0]*len(train_data[0])
    s2 = [0]*len(train_data[0])
    s3 = [0]*len(train_data[0])
    alpha = [0.6]*30
    for i in range(len(train_data)):
        #print(u"====规格"+str(i+1)+"=======")
        t = train_data[i]
        
        s1[0] = t[1]
        for j in range(1,len(s1),1):
            s1[j] = alpha[i]*train_data[i][j]+(1-alpha[i])*s1[j-1]
        s2[0] = s1[1]
        for j in range(1,len(s2),1):
            s2[j] = alpha[i]*s1[j]+(1-alpha[i])*s2[j-1]
        s3[0] = s2[1]
        for j in range(1,len(s3),1):
            s3[j] = alpha[i]*s2[j]+(1-alpha[i])*s3[j-1]
        #print("s1= "+str(s1))
        #print("s2= "+str(s2))
        #print("s3= "+str(s3))
        
        a = 3.0 * s1[-1] - 3 * s2[-1] + s3[-1]
        b = alpha[i]/(2.0*(1-alpha[i])**2) * ((6-5 * alpha[i])*s1[-1] - 2*(5 - 4 * alpha[i])*s2[-1] + (4 - 3 * alpha[i]) * s3[-1])
        c = alpha[i]**2/(2*((1-alpha[i])**2)) * (s1[-1] - 2*s2[-1] + s3[-1])
        #print("a= "+str(a))
        #print("b= "+str(b))
        #print("c= "+str(c))
        
        yuce1 = a + b + c
        yuce2 = (a + 2 * b + 4 * c) * ((temp-1)/temp)
        
        yuce = yuce1 + yuce2
        yuce = round(yuce)
        if yuce < 0:
            yuce = 0
        #print(u"预测值为 "+str(yuce))
        name = "flavor"+str(i+1)
        yuce_flvorname_flavornum_s[name] = int(yuce)
    
    ###############获得虚拟机名和预测台数的对应####################

    ######################################################

    ###################获得names cpus mems这三个序列######################
    cpus = []
    mems = []
    names = []
    #input文件中需要预测的虚拟机[("flavor1",12,1024),("flavor1",12,1024)]
    input_xuNiJis = []
    i = 2
    while(i<2 + input_num):
        input_now_flavor_name = input_lines_new[i].strip().split(" ")[0]
        input_now_flavor_CPU = int(input_lines_new[i].strip().split(" ")[1])
        input_now_flavor_MEM = int(input_lines_new[i].strip().split(" ")[2])/1024
        input_now_flavor = [input_now_flavor_name,input_now_flavor_CPU,input_now_flavor_MEM]
        input_xuNiJis.append(input_now_flavor)
        nums = yuce_flvorname_flavornum_s[input_now_flavor_name]
        for j in range(nums):
            names.append(input_now_flavor_name)
            cpus.append(input_now_flavor_CPU)
            mems.append(input_now_flavor_MEM)
        i = i + 1
    
    
    #print(names)
    #print(mems)
    #print(cpus)
    
    ################# 获得物理机的规格###############
    input_wuLiJi_cpu = int(input_lines_new[0].split(" ")[0])
    input_wuLiJi_mem = int(input_lines_new[0].split(" ")[1])
    ########################获得物理机的规格#########
    
    
    ##################### 优化的维度 装箱###########################
    input_weidu = input_lines_new[-3].strip()
    if(input_weidu=="CPU"):
        zx_wuLiJis,_ = memory_alloction.get_memory_allocation(input_wuLiJi_cpu,input_wuLiJi_mem,cpus,mems,names)
        
    elif(input_weidu=="MEM"):
        zx_wuLiJis,_ = memory_alloction.get_memory_allocation(input_wuLiJi_mem,input_wuLiJi_cpu,mems,cpus,names)
        
    else:
        pass
        #print("出错了，别玩了")
    #print(zx_wuLiJis)
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
    #print(result)
    for i in range(0,len(zx_wuLiJis),1):
        zx_wuLiJi = zx_wuLiJis[i]
        sss = str(i+1)
        temp = {}
        for xuNiJi in zx_wuLiJi :
            if(temp.has_key(xuNiJi)):
                temp[xuNiJi] = temp[xuNiJi] + 1
            else:
                temp[xuNiJi] = 1
        #print(temp)
        for name in temp:
            sss = sss+" "+name+" "+str(temp[name])
        #print(sss)
        result.append(sss.strip())
    
    return result