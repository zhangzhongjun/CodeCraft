# coding=utf-8

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
