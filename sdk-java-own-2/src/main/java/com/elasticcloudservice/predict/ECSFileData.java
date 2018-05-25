package com.elasticcloudservice.predict;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;

/**
 * @author 张中俊
 * @create 2018-03-15 21:46
 **/
public class ECSFileData {
    private static long nd = 1000*24*60*60;//一天的毫秒数
    private static long nh = 1000*60*60;//一小时的毫秒数
    private static long nm = 1000*60;//一分钟的毫秒数
    private static long ns = 1000;//一秒钟的毫秒数

    private String[] lines;
    private Date firstDate;
    private Date lastDate;
    private HashMap<String,Integer> datas = new HashMap<>();

    public ECSFileData(String[] lines) {
        this.lines = lines;
        try{
            //获得第一天的 Date对象
            String firstDate_str = lines[0].split("\t")[2].split(" ")[0];
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            this.firstDate = sdf.parse(firstDate_str);
            //获得最后一天的 Data对象
            String lastDate_str = lines[lines.length-1].split("\t")[2];
            SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM-dd HH-mm-ss");
            this.lastDate = sdf.parse(lastDate_str);

            for(String line : lines){
                String flavorName = line.split("\t")[1];
                if(datas.get(flavorName)==null){
                    datas.put(flavorName,1);
                }else{
                    datas.put(flavorName,datas.get(flavorName)+1);
                }
            }
        }catch (ParseException e){
            e.printStackTrace();
        }
    }

    public HashMap<String, Integer> getDatas() {
        return datas;
    }

    public int diffOfHour(){
        //获得两个时间的毫秒时间差异
        long diff = lastDate.getTime() - firstDate.getTime();
        //计算差多少小时
        int hours =  (int)(diff/nh);
        return hours;
    }

    public int diffOfDay(){
        //获得两个时间的毫秒时间差异
        long diff = lastDate.getTime() - firstDate.getTime();
        //计算差多少天
        return (int)(diff/nd);
    }



}
