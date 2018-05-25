package com.elasticcloudservice.predict;

/**
 * 虚拟机，种类数 和  每种的规格  是固定的
 *
 * @author 张中俊
 * @create 2018-03-12 8:51
 **/
public class XuNiJi implements Comparable<XuNiJi>{
    private static String weiDu;
    private String name;
    private int CPU;
    private int MEM;
    private static int [] cpus = {1,1,1,2,2,2,4,4,4,8,8,8,16,16,16};
    private static int [] mems = {1024,2048,4096,2048,4096,8192,4096,8192,16384,8192,16384,32768,16384,32768,65536};
    public XuNiJi(String name,int CPU, int MEM) {
        this.name = name;
        this.CPU = CPU;
        this.MEM = MEM;
    }

    public static void setWeiDu(String weiDu) {
        XuNiJi.weiDu = weiDu;
    }

    public static String getWeiDu() {
        return weiDu;
    }

    public String getName() {
        return name;
    }

    public int getCPU() {
        return CPU;
    }

    public int getMEM() {
        return MEM;
    }

    public void setCPU(int CPU) {
        this.CPU = CPU;
    }

    public void setMEM(int MEM) {
        this.MEM = MEM;
    }

    /**
     * 得到第n台虚拟机
     * @param nth
     * @return
     */
    public static XuNiJi getNthXuNiJi(int nth){
        String name = "flavor"+nth;
        return new XuNiJi(name,cpus[nth-1],mems[nth-1]);
    }

    @Override
    public String toString() {
        return this.name+" CPU:"+this.CPU+" MEM:"+this.MEM;
    }

    @Override
    public int compareTo(XuNiJi o) {
        if(XuNiJi.weiDu.equals("MEM")){
            return o.getMEM() - this.getMEM();
        }else if(XuNiJi.weiDu.equals("CPU")){
            return o.getCPU() -  this.getCPU();
        }else{
            System.err.println("错误，使用了错误的维度");
        }
        return 0;
    }
}

