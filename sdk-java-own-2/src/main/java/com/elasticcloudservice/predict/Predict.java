package com.elasticcloudservice.predict;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Predict {

	public static String[] predictVm(String[] ecsContent, String[] inputContent) {

		try {
			//所有的结果
			ArrayList<String> res = new ArrayList<>();

			ECSFileData ecsFileData = new ECSFileData(ecsContent);
			InputFileData inputFileData = new InputFileData(inputContent);

            HashMap<String,Integer> yuCeValues = PreProcessAndJianMoAndYuce.PreprocessAndJianMoAndYuce_all(ecsFileData, inputFileData);

			ArrayList<XuNiJi> xuNiJis = new ArrayList<>();
			int sum = 0;
			for(XuNiJi xuNiJi : inputFileData.getXuNiJis()){
				int yuCeValue = yuCeValues.get(xuNiJi.getName());
				sum = sum + yuCeValue;
				res.add(xuNiJi.getName()+" "+yuCeValue);
				for(int j=0;j<yuCeValue;j++) {
					XuNiJi temp = new XuNiJi(xuNiJi.getName(), xuNiJi.getCPU(), xuNiJi.getMEM());
					xuNiJis.add(temp);
				}
			}
			res.add(0,sum+"");

			res.add("");

			Collections.sort(xuNiJis);
            res.addAll(FirstFit.FF(xuNiJis,inputFileData.getWuLiJi().getCPU(),inputFileData.getWuLiJi().getMEM()*1024));
			String[] res_arr = new String[res.size()];
			//返回
			res.toArray(res_arr);
			return res_arr;
		}catch(Exception e){
			e.printStackTrace();
		}
		return null;
	}

}
