package com.elasticcloudservice.predict;

import com.filetool.util.FileUtil;
import org.junit.Test;

import java.io.File;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

/**
 * @author 张中俊
 * @create 2018-03-15 21:53
 **/
public class ECSFileDataTest {
    @Test
    public void readForDayTest() {
        String path = MyUtils.getFile("inputs", "data_2016_1.txt").getAbsolutePath();
        String[] lines = FileUtil.read(path, null);
        ECSFileData ECSFileData = new ECSFileData(lines);
        ArrayList<ArrayList<Integer>> days = ECSFileData.readForDay();

        for (ArrayList<Integer> day : days) {
            for (Integer num : day) {
                System.out.print(num + "\t");
            }
            System.out.println();
        }
    }


    //写文件
    @Test
    public void readForHourTest() throws ParseException {
        String path = MyUtils.getFile("inputs", "").getAbsolutePath();
        File dictionary = new File(path);
        File[] files = dictionary.listFiles();
        for (File file : files) {
            path = file.getAbsolutePath();
            System.out.println("正在处理 " + path);
            String[] lines = FileUtil.read(path, null);
            ECSFileData ECSFileData = new ECSFileData(lines);
            ArrayList<ArrayList<Integer>> res = ECSFileData.readForHour();

            String[] contents = new String[res.size()];
            for (int i = 0; i < res.size(); i++) {
                System.out.println("型号" + (i + 1) + " " + res.get(i).toString());
                contents[i] = "型号" + (i + 1) + " " + res.get(i).toString();
            }
            FileUtil.write(MyUtils.getFile("output", file.getName()).getAbsolutePath(), contents, false);
        }
    }


    //写文件
    @Test
    public void readForHourTest2() throws ParseException {
        String path = MyUtils.getFile("inputs", "").getAbsolutePath();
        File dictionary = new File(path);
        File[] files = dictionary.listFiles();
        for (File file : files) {
            path = file.getAbsolutePath();
            System.out.println("正在处理 " + path);

            //最终的结果
            ArrayList<ArrayList<Integer>> res = new ArrayList<>();

            String[] lines = FileUtil.read(path, null);
            //计算该行对应的日期
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            Date firstDate = sdf.parse(lines[0].split("\t")[2]);
            Date lastDate = sdf.parse(lines[lines.length-1].split("\t")[2]);
            int last_first_kuadu = DateUtils.diffOfHour(lastDate,firstDate)+1;
            for(int i=0;i<30;i++){
                ArrayList<Integer> temp = new ArrayList<>();
                for(int j=0;j<last_first_kuadu;j++){
                    temp.add(0);
                }
                res.add(temp);
            }

            for(String line : lines) {
                //计算型号 根据型号分析索引
                String no = line.split("\t")[1].replace("flavor","");
                int index = (new Integer(no)) - 1 ;

                String nowDate_str = line.split("\t")[2];
                Date nowDate = sdf.parse(nowDate_str);

                //获得两个时间的毫秒时间差异
                int diff = DateUtils.diffOfHour(nowDate,firstDate);
                //System.out.println("现在时间： "+sdf.format(nowDate)+" 时间相差： "+hour+" 小时");
                int yuanlai = res.get(index).get(diff);
                res.get(index).set(diff,yuanlai+1);
            }

            String[] contents = new String[res.size()];
            for (int i = 0; i < res.size(); i++) {
                System.out.println("型号" + (i + 1) + " " + res.get(i).toString());
                contents[i] = "型号" + (i + 1) + " " + res.get(i).toString();
            }
            FileUtil.write(MyUtils.getFile("output", file.getName()).getAbsolutePath(), contents, false);
        }
    }


    @Test
    public void t3() {
        String path = MyUtils.getFile("inputs", "").getAbsolutePath();
        File dictionary = new File(path);
        File[] files = dictionary.listFiles();
        for (File file : files) {
            System.out.println(file.getAbsolutePath());
            System.out.println(file.getName());
        }
    }


    //写文件
    @Test
    public void t4() throws ParseException {
        String path = MyUtils.getFile("inputs", "data_2015_1.txt").getAbsolutePath();
        String[] lines = FileUtil.read(path, null);
        ECSFileData ECSFileData = new ECSFileData(lines);
        ArrayList<Integer> arr = ECSFileData.readForHour().get(0);
        System.out.println(arr.size()+" "+arr.toString());
        ArrayList<Integer> arr_valid = new ArrayList<>();
        //去掉早上五点到晚上五点
        for(int j=0;j<arr.size()/ 24;j++){
            arr_valid.addAll(arr.subList(0+(j*24),5+(j*24)));
            arr_valid.addAll(arr.subList(17+(j*24),24+(j*24)));
        }
        System.out.println(arr_valid.size()+" "+arr_valid.toString());
    }


}
