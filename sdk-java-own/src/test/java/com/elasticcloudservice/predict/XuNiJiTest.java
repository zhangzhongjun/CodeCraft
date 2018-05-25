package com.elasticcloudservice.predict;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

/**
 * @author 张中俊
 * @create 2018-03-23 9:24
 **/
public class XuNiJiTest {
    @Test
    public void t1(){
        XuNiJi.setWeiDu("CPU");
        XuNiJi xu1 = new XuNiJi("flavor1",12,12);
        XuNiJi xu2 = new XuNiJi("flavor2",10,12);
        XuNiJi xu3 = new XuNiJi("flavor3",12,12);
        XuNiJi xu4 = new XuNiJi("flavor4",1,12);
        XuNiJi xu5 = new XuNiJi("flavor5",50,12);
        XuNiJi xu6 = new XuNiJi("flavor6",13,12);

        ArrayList<XuNiJi> xus = new ArrayList<>();
        xus.add(xu1);
        xus.add(xu2);
        xus.add(xu3);
        xus.add(xu4);
        xus.add(xu5);
        xus.add(xu6);

        Collections.sort(xus);
        for(XuNiJi xuNiJi: xus){
            System.out.println(xuNiJi.getName());
        }
    }
}
