package com.elasticcloudservice.predict;

import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

/**
 * @author 张中俊
 * @create 2018-03-16 22:31
 **/
public class PreProcessAndJianMoAndYuce {

    /**
     * 处理数据集 并 进行建模
     * @param ECSFileData 经过预处理的原始文件
     * @param guiGe 为了方便测试，添加了guiGe这个参数。我认为将来还是一起返回所有规格的会方便点
     * @return
     * @throws ParseException
     */
    public static RegressionLine PreProcessAndJianMo_JustOne(ECSFileData ECSFileData, int guiGe) throws ParseException {
        //获得每一个小时的请求量
        ArrayList<ArrayList<Integer>> num_hour_s = ECSFileData.readForHour();
        ArrayList<Integer> num_hour = num_hour_s.get(guiGe-1);
        //System.out.println("规格："+guiGe+" "+num_hour.toString());
        //num_hour_valid是有效的点
        ArrayList<Integer> num_hour_valid = new ArrayList<>();
        //去掉早上五点到晚上五点
        for(int j=0;j<num_hour.size() / 24;j++){
            num_hour_valid.addAll(num_hour.subList(0+(j*24),5+(j*24)));
            num_hour_valid.addAll(num_hour.subList(18+(j*24),24+(j*24)));
        }
        //System.out.println(arrs.toString());
        //计算累加和
        ArrayList<Integer> sums = new ArrayList<>();
        int sum = num_hour_valid.get(0);
        for(int j=0;j<num_hour_valid.size();j++){
            sums.add(sum);
            sum = sum + num_hour_valid.get(j);
        }
        //System.out.println(sums.toString());
        // 开始回归预测
        return RegressionLineWrapper.yuCe(sums);
    }

    /**
     * 对所有的规格的虚拟机进行预测
     * @param ECSFileData ecsData.txt中的内容
     * @param inputFileData input.txt中的内容
     * @return
     * @throws ParseException
     */
    public static ArrayList<ArrayList<Integer>> PreprocessAndJianMoAndYuce_all(ECSFileData ECSFileData, InputFileData inputFileData) throws ParseException {
        //是一个map，key是型号，而value是预测得到的直线
        HashMap<Integer,RegressionLine> rls = new HashMap<>();
        ArrayList<ArrayList<Integer>> yuCeValues = new ArrayList<>();
        //获得每一个小时的请求量
        ArrayList<ArrayList<Integer>> num_hour_s = ECSFileData.readForHour();
        for(XuNiJi xuNiJi :inputFileData.getXuNiJis()) {
            int index = Integer.valueOf(xuNiJi.getName().replace("flavor","")) - 1;
            ArrayList<Integer> num_hour = num_hour_s.get(index);
            //System.out.println("规格："+guiGe+" "+num_hour.toString());
            //num_hour_valid是去掉早上五点到晚上五点，按照小时的点
            ArrayList<Integer> num_hour_valid = new ArrayList<>();
            //去掉早上五点到晚上五点
            for (int j = 0; j < num_hour.size() / 24; j++) {
                num_hour_valid.addAll(num_hour.subList(0 + (j * 24), 5 + (j * 24)));
                num_hour_valid.addAll(num_hour.subList(18 + (j * 24), 24 + (j * 24)));
            }
            //System.out.println(arrs.toString());
            //计算累加和
            ArrayList<Integer> sums = new ArrayList<>();
            int sum = num_hour_valid.get(0);
            for (int j = 0; j < num_hour_valid.size(); j++) {
                sums.add(sum);
                sum = sum + num_hour_valid.get(j);
            }
            System.out.println(sums.toString());
            //开始去除异常值 认为平均每天增加2台是不合理的
            ArrayList<DataPoint> points = new ArrayList<>();
            points.add(new DataPoint(0,sums.get(0)));
            for(int i=1;i<sums.size();i++){
                float caiZhi = (float)sums.get(i)-points.get(points.size()-1).getY();
                float xieLv = caiZhi/(i-sums.size());
                if(xieLv < 5 /*&& sums.get(i)!=points.get(points.size()-1).getY()*/){
                    points.add(new DataPoint(i,sums.get(i)));
                }
            }
            System.out.println(points);
            rls.put(index+1,new RegressionLine(points,points.size()));
            //rls.put(index+1,RegressionLineWrapper.yuCe(sums));
        }

        for (XuNiJi xuNiJi : inputFileData.getXuNiJis()) {
            System.out.println("===============================================");
            int index = Integer.valueOf(xuNiJi.getName().replace("flavor","")) - 1;
            System.out.println("规格"+(index+1)+":");
            RegressionLine rl = rls.get(index+1);
            //rl.printSums();
            rl.printLine();
            int lastValue = Integer.valueOf((String) rl.getListY().get(rl.getListY().size() - 1));
            //获得预测集最后累加的结果
            System.out.println("训练集最后的结果："+lastValue);

            //获得训练集的最后一个日期
            Date date = inputFileData.getLastDate();
            // 训练集的点数
            System.out.println("训练集的点数： "+rl.getPn_shiji());
            //测试集的点数
            //System.out.println("测试集的点数："+ ECSFileData.diffOfHour(date));
            //float yuCeJieGuo = rl.at(rl.getPn_shiji() + ECSFileData.diffOfHour(date));
            float yuCeJieGuo = 0;
            //上取整
            int yuceJieGuo_shangQuZheng = (int) Math.ceil(yuCeJieGuo);
            int yuceValue = Math.max(0,yuceJieGuo_shangQuZheng - lastValue);
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(index+1);
            temp.add(yuceValue);
            yuCeValues.add(temp);
            System.out.println("测试集结束之后的结果："+yuCeJieGuo);
            System.out.println("===============================================");
        }

        return yuCeValues;
    }
}
