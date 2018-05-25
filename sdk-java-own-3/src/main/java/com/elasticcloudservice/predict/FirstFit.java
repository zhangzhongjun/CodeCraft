package com.elasticcloudservice.predict;

import java.util.ArrayList;

/**
 * 伪代码如下（First-Fit）：
 * 对于预测出来的每个虚拟机v∈N_t
 * 从物理服务器集合H选择首次能满足需求的物理服务器h^first
 * 如果 r_v≤R_(h^first )：
 * 放置到该台物理服务器
 * 物理服务器做资源扣减 R_(h^first )=R_(h^first )-r_v
 * 否则：
 * 开启一台新的物理服务器 h^new
 * 虚拟机放置到新的物理服务上并作资源扣减 R_(h^new )=R_(h^new )-r_v
 * 更新所用物理服务器集合 H^'
 * 更新剩余虚拟机集合 N_t^'
 *
 * @author 张中俊
 * @create 2018-03-12 17:14
 **/
public class FirstFit {

    /**
     *
     * @param xuNiJis 最好先排过序的，先放“西瓜”，后放“芝麻”，效果更好
     * @param CPU 物理服务器的CPU
     * @param MEM 物理服务器的MEM
     * @return 结果
     */
    public static ArrayList<String> FF(ArrayList<XuNiJi> xuNiJis, int CPU, int MEM){
        //物理机的编号
        int No = 1;
        ArrayList<Phase2_Output> outputs = new ArrayList<Phase2_Output>();
        outputs.add(new Phase2_Output(new WuLiJi(CPU,MEM)));

        for(XuNiJi xuNiJi : xuNiJis){
            boolean flag = false;
            for(Phase2_Output output : outputs){
                if(output.getWuLiJi().canXuNi(xuNiJi)){
                    output.getWuLiJi().xuNi(xuNiJi);
                    output.addNewXuNiJi(xuNiJi);
                    flag = true;
                    break;
                }
            }
            if(!flag){
                //开启一个新的物理机
                Phase2_Output output = new Phase2_Output(new WuLiJi(CPU,MEM));
                output.getWuLiJi().xuNi(xuNiJi);
                output.addNewXuNiJi(xuNiJi);
                outputs.add(output);
            }
        }

        ArrayList<String> res = new ArrayList<>();
        //先把物理机的台数写上
        res.add(outputs.size()+"");
        int i=1;
        for(Phase2_Output output : outputs){
            res.add(i+" "+output.toString().trim());
            i++;
        }

        return res;
    }
}
