package com.elasticcloudservice.predict;

import java.util.TreeMap;

/**
 * 阶段2的输出
 * @author 张中俊
 * @create 2018-03-12 16:14
 **/
public class Phase2_Output {
    /**
     * 物理机的信息
     */
    private WuLiJi wuLiJi;
    /**
     * 该物理机中的虚拟机
     */
    private TreeMap<String, Integer> xuNiJis;

    public void addNewXuNiJi(XuNiJi xuNiJi) {
        if (this.xuNiJis.keySet().contains(xuNiJi.getName())) {
            int num = this.xuNiJis.get(xuNiJi.getName());
            this.getXuNiJis().put(xuNiJi.getName(), num + 1);
        } else {
            this.getXuNiJis().put(xuNiJi.getName(), 1);
        }
    }

    public void setWuLiJi(WuLiJi wuLiJi) {
        this.wuLiJi = wuLiJi;
    }

    public void setXuNiJis(TreeMap<String, Integer> xuNiJis) {
        this.xuNiJis = xuNiJis;
    }

    public WuLiJi getWuLiJi() {

        return wuLiJi;
    }

    public TreeMap<String, Integer> getXuNiJis() {
        return xuNiJis;
    }

    public Phase2_Output(WuLiJi wuLiJi, TreeMap<String, Integer> xuNiJis) {
        this.wuLiJi = wuLiJi;
        this.xuNiJis = xuNiJis;
    }

    public Phase2_Output(WuLiJi wuLiJi) {
        this.wuLiJi = wuLiJi;
        this.setXuNiJis(new TreeMap<String, Integer>());
    }


    public Phase2_Output() {
        this.setXuNiJis(new TreeMap<String, Integer>());
    }

    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer();
        for (String key : this.getXuNiJis().keySet()) {
            int num = this.getXuNiJis().get(key);
            sb.append(key + " ");
            sb.append(num + " ");
        }
        return sb.toString();
    }
}

