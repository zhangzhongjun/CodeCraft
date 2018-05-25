package com.elasticcloudservice.predict;

import java.util.ArrayList;

/**
 * @author 张中俊
 * @create 2018-03-16 21:37
 **/
public class RegressionLineWrapper {

    /**
     * 进行预测
     * @param temp 要预测的数据，x轴为1 2 3 ... ，y轴为temp中的值
     * @return 预测得到的直线
     */
    public static RegressionLine yuCe(ArrayList<Integer> temp) {
        RegressionLine line = new RegressionLine();

        ArrayList<DataPoint> data = new ArrayList<>();
        for(int i=1;i<temp.size();i++) {
            if(temp.get(i) != temp.get(i-1)){
                System.out.println(i+" "+temp.get(i));
                DataPoint dp = new DataPoint(i,temp.get(i));
                data.add(dp);
            }
        }
        return new RegressionLine(data,temp.size());
    }


}
