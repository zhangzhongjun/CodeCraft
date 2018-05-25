package com.elasticcloudservice.predict;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;

/**
 * @author 张中俊
 * @create 2018-03-15 21:46
 **/
public class ECSFileData {
    private String[] lines;
    private Date firstDate;
    private Date lastDate;

    public ECSFileData(String[] lines) {
        this.lines = lines;
        try{
            //获得第一天的 Date对象
            String firstDate_str = lines[0].split("\t")[2];
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH-mm-ss");
            this.firstDate = sdf.parse(firstDate_str);
            //获得最后一天的 Data对象
            String lastDate_str = lines[lines.length-1].split("\t")[2];
            SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM-dd HH-mm-ss");
            this.lastDate = sdf.parse(lastDate_str);
        }catch (ParseException e){
            e.printStackTrace();
        }
    }

    /**
     * 按照天读取数据
     *
     * @return 每天的所有请求的总数
     */
    public ArrayList<ArrayList<Integer>> readForDay(){
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        int [] nums = new int[30];
        Arrays.fill(nums,0);
        String lastDate = "";
        for(String line : lines){
            String nowDate = line.split("\t")[2].split(" ")[0];
            if(nowDate.equals(lastDate)){
                String no = line.split("\t")[1].replace("flavor","");
                int index = new Integer(no);
                nums[index-1]  = nums[index-1] + 1;
            }else {
                //昨天的记录 入库
                ArrayList<Integer> temp = new ArrayList<>();
                for(int num : nums ){
                    temp.add(num);
                }
                res.add(temp);
                //重置
                Arrays.fill(nums,0);
                //加1
                String no = line.split("\t")[1].replace("flavor","");
                int index = new Integer(no);
                nums[index-1]  = nums[index-1] + 1;
                //更新
                lastDate = nowDate;
            }
        }

        //最后一天的记录 入库
        ArrayList<Integer> temp = new ArrayList<>();
        for(int num : nums ){
            temp.add(num);
        }
        res.add(temp);
        return res;
    }

    /**
     * 按照小时读取数据 list 的 list<br>
     *     考虑冗余，设置了30，代表30种规格
     *
     *
     *
     * @return 按照小时统计的请求总数
     * @throws ParseException 解析日期异常
     */
    public ArrayList<ArrayList<Integer>> readForHour() throws ParseException {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        //计算差多少小时
        int hour = DateUtils.diffOfHour(lastDate,firstDate);

        //开始分配内存空间 30指有30种型号的虚拟机
        for(int i=0;i<30;i++){
            ArrayList<Integer> arr = new ArrayList<Integer>();
            //50是设置的一个冗余量
            for (int j=0;j<hour+50;j++)
                arr.add(0);
            res.add(arr);
        }

        for(String line : lines) {
            //计算型号 根据型号分析索引
            String no = line.split("\t")[1].replace("flavor","");
            int index = (new Integer(no)) - 1 ;

            String nowDate_str = line.split("\t")[2];
            //计算该行对应的日期
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            Date nowDate = sdf.parse(nowDate_str);


            //获得两个时间的毫秒时间差异
            hour = DateUtils.diffOfHour(lastDate,firstDate);
            //System.out.println("现在时间： "+sdf.format(nowDate)+" 时间相差： "+hour+" 小时");
            res.get(index).set((int)hour,res.get(index).get((int) hour) + 1);
        }
        return res;
    }

    public String[] getLines() {
        return lines;
    }

    public Date getFirstDate() {
        return firstDate;
    }

    public Date getLastDate() {
        return lastDate;
    }
}
