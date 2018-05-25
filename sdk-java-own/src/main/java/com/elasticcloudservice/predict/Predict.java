package com.elasticcloudservice.predict;

import java.util.ArrayList;
import java.util.Collections;

public class Predict {

	public static String[] predictVm(String[] ecsContent, String[] inputContent) {

		try {
			//所有的结果
			ArrayList<String> res = new ArrayList<>();

			ECSFileData ECSFileData = new ECSFileData(ecsContent);
			InputFileData inputFileData = new InputFileData(inputContent);

            ArrayList<ArrayList<Integer>> yuCeValues = PreProcessAndJianMoAndYuce.PreprocessAndJianMoAndYuce_all(ECSFileData, inputFileData);
			System.out.println("==="+yuCeValues+"===");
			int sum = 0;
			for(int i=0;i<yuCeValues.size();i++){
				res.add("flavor"+yuCeValues.get(i).get(0)+" "+yuCeValues.get(i).get(1));
				sum = sum + yuCeValues.get(i).get(1);
			}
			res.add(0,sum+"");
			res.add("");
			ArrayList<XuNiJi> xuNiJis = new ArrayList<>();
			for(int i=0;i<yuCeValues.size();i++){
				int yuCeValue = yuCeValues.get(i).get(1);
				for(int j=0;j<yuCeValue;j++) {
					XuNiJi xuNiJi = new XuNiJi(inputFileData.getXuNiJis().get(i).getName(), inputFileData.getXuNiJis().get(i).getCPU(), inputFileData.getXuNiJis().get(i).getMEM());
					xuNiJis.add(xuNiJi);
				}
			}

			Collections.sort(xuNiJis);
            res.addAll(FirstFit.FF(xuNiJis,inputFileData.getWuLiJi().getCPU(),inputFileData.getWuLiJi().getMEM()*1024));
			String[] res_arr = new String[res.size()];
			res.toArray(res_arr);
			for(String r : res_arr){
				System.out.println(r);
			}
			return res_arr;
		}catch(Exception e){
			e.printStackTrace();
		}
		return null;
	}

}
