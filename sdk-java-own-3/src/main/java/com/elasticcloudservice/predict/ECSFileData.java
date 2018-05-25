package com.elasticcloudservice.predict;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

/**
 * 用于读取ECS文件中的数据
 *
 * @author 张中俊
 * @create 2018-03-15 21:46
 **/
public class ECSFileData {
    /**
     * key是规格的名字，value是该种规格的请求数
     */
    private HashMap<String,Integer> datas = new HashMap<>();
    /**
     * 预测的时间跨度
     */
    private int numOfHour;

    public ECSFileData(String[] lines,int tiaoShu) {
        try{
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

            ArrayList<String> lines_last = new ArrayList<>();
            for(int i=lines.length-tiaoShu ;i<lines.length;i++){
                lines_last.add(lines[i]);
            }
            String d1 = lines_last.get(0).split("\t")[2];
            Date date1 = sdf.parse(d1);
            String d2 = lines_last.get(lines_last.size()-1).split("\t")[2];
            Date date2 = sdf.parse(d2);
            this.numOfHour = DateUtils.diffOfHour(date2,date1);

            for(String line : lines_last){
                    String flavorName = line.split("\t")[1];
                    if (datas.get(flavorName) == null) {
                        datas.put(flavorName, 1);
                    } else {
                        datas.put(flavorName, datas.get(flavorName) + 1);
                    }
            }
        }catch (ParseException e){
            e.printStackTrace();
        }
    }

    public HashMap<String, Integer> getDatas() {
        return datas;
    }

    public int getNumOfHour() {
        return numOfHour;
    }
}
