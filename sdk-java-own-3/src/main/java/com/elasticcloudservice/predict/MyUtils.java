package com.elasticcloudservice.predict;

import java.io.File;

/**
 * @author 张中俊
 * @create 2018-03-16 22:29
 **/
public class MyUtils {

    public static File getFile(String dirname, String fileName) {
        String path = System.getProperty("user.dir");
        path = path + File.separator + dirname;
        File file = new File(path, fileName);
        return file;
    }
}
