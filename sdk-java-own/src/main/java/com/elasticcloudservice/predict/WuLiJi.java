package com.elasticcloudservice.predict;

/**
 * @author 张中俊
 * @create 2018-03-12 9:02
 **/
public class WuLiJi {
    private int CPU;
    private int MEM;

    public WuLiJi(int CPU, int MEM) {
        this.CPU = CPU;
        this.MEM = MEM;
    }

    public void setCPU(int CPU) {
        this.CPU = CPU;
    }

    public void setMEM(int MEM) {
        this.MEM = MEM;
    }

    public int getCPU() {
        return CPU;
    }

    public int getMEM() {
        return MEM;
    }

    public boolean canXuNi(XuNiJi xuNiJi){
        if(this.CPU>=xuNiJi.getCPU() && this.MEM>=xuNiJi.getMEM())
            return true;
        return false;
    }

    public void xuNi(XuNiJi xuNiJi){
        this.setCPU(this.CPU-xuNiJi.getCPU());
        this.setMEM(this.MEM-xuNiJi.getMEM());
    }

    @Override
    public String toString() {
        return "物理机CPU:"+this.CPU+" MEM:"+this.MEM;
    }
}
