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
     * 对所有的规格的虚拟机进行预测
     * @param ecsFileData ecsData.txt中的内容
     * @param inputFileData input.txt中的内容
     * @return
     * @throws ParseException
     */
    public static HashMap<String,Integer> PreprocessAndJianMoAndYuce_all(ECSFileData ecsFileData, InputFileData inputFileData) throws ParseException {
        HashMap<String,Integer> yuCeValues = new HashMap<>();

        int numOfDay = ecsFileData.diffOfDay();
        //对于每个需要预测的虚拟机 开始预测
        for(XuNiJi xuNiJi :inputFileData.getXuNiJis()) {
            int numOfXuNiJi = ecsFileData.getDatas().get(xuNiJi.getName());
            //计算训练集的一天的平均值
            double jz = (double)numOfXuNiJi/(double)numOfDay;

            int yuCeValue = (int) Math.ceil(jz * (double)inputFileData.getKuaDuOfDay());
            yuCeValues.put(xuNiJi.getName(),yuCeValue);
        }

        return yuCeValues;
    }
}
