package com.elasticcloudservice.predict;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

/**
 * 用来读取input.txt中的文件
 *
 * @author 张中俊
 * @create 2018-03-17 21:04
 **/
public class InputFileData {
    /**
     * 虚拟机的规格数
     */
    private int numGuiGe;
    /**
     * 需要预测的跨度的第一天
     */
    private Date firstDate;
    /**
     * 需要预测的跨度的最后一天
     */
    private Date lastDate;
    /**
     * 所有的虚拟机的规格
     */
    private ArrayList<XuNiJi> xuNiJis;
    /**
     * 物理机的规格
     */
    private WuLiJi wuLiJi;
    /**
     * 需要优化的维度
     */
    private String weiDu;

    /**
     * 初始化函数
     * @param lines 文件
     * @throws ParseException 日期解析错误
     */
    public InputFileData(String[] lines) throws ParseException {
        //物理机
        this.wuLiJi = new WuLiJi(Integer.valueOf(lines[0].split(" ")[0]),Integer.valueOf(lines[0].split(" ")[1]));
        //虚拟机的规格数
        this.numGuiGe = Integer.valueOf(lines[2]);
        this.xuNiJis = new ArrayList<>();
        int i;
        for(i=3;i<3+numGuiGe;i++){
            XuNiJi xuNiJi = new XuNiJi(lines[i].split(" ")[0],Integer.valueOf(lines[i].split(" ")[1]),Integer.valueOf(lines[i].split(" ")[2]));
            this.xuNiJis.add(xuNiJi);
        }
        i++;
        weiDu = lines[i];
        XuNiJi.setWeiDu(weiDu);
        i = i + 2;
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        this.firstDate = sdf.parse(lines[i]);
        i = i+1;
        this.lastDate = sdf.parse(lines[i]);
    }

    public int getNumGuiGe() {
        return numGuiGe;
    }

    public Date getLastDate() {
        return lastDate;
    }

    public ArrayList<XuNiJi> getXuNiJis() {
        return xuNiJis;
    }

    public WuLiJi getWuLiJi() {
        return wuLiJi;
    }

    public String getWeiDu() {
        return weiDu;
    }

    public int getKuaDuOfHour(){
        return DateUtils.diffOfHour(this.lastDate,this.firstDate);
    }
}
