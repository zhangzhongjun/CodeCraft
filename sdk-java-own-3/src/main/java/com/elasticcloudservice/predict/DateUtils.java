package com.elasticcloudservice.predict;

import javax.xml.crypto.Data;
import java.util.Date;

/**
 * @author 张中俊
 * @create 2018-03-23 11:18
 **/
public class DateUtils {
    private static long nd = 1000*24*60*60;//一天的毫秒数
    private static long nh = 1000*60*60;//一小时的毫秒数
    private static long nm = 1000*60;//一分钟的毫秒数
    private static long ns = 1000;//一秒钟的毫秒数

    /**
     * 计算两个日期之间的小时数
     * @param lastDate 终点
     * @param firstDate 起点
     * @return 小时数
     */
    public static int diffOfHour(Date lastDate,Date firstDate){
        //获得两个时间的毫秒时间差异
        long diff = lastDate.getTime() - firstDate.getTime();
        //计算差多少小时
        int hours =  (int)(diff/nh) + 1;
        return hours;
    }
}
