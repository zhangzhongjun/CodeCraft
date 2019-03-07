# 2018华为软件精英挑战赛(Code Craft)

![logo](imgs/logo.png)

> 云计算中，物理机可以虚拟出多个虚拟机。精确预测虚拟机的分布并寻找最大利润率的虚拟机部署方案：在保证预测精确度的前提下，使得云平台的利润率最大化。本人主要负责预测部分和部署部分的代码实现，并参与了预测方案比较和选择。

## 各个文件
官方文档
文件夹 初赛文档 是初赛的时候释放的参考文件
2018软挑大赛指导书\.pdf 是注册流程等的教学
赛题问题大全（最新汇总）20180314\.pdf 是对一些问题的回答

java语言：
sdk-java-own 将整个项目的框架搭建了起来，使用线性回归分析 进行预测

sdk-java-own2 使用求取平均值 进行预测

sdk-java-own3 使用求取最后n条记录的平均值 进行预测


python语言：
sdk-python_局部加权线性回归 使用 局部加权线性回归 进行预测

sdk-python_局部加权线性回归_按天  使用 局部加权线性回归 进行预测 上面的一个项目是按照小时取点的，这个项目是按照天取点的

sdk-python-平均值 使用平均值进行预测

sdk-python-平均值-按天-去噪 使用平均值进行预测，按天取点，并且加入去噪的逻辑

sdk-python-星期映射 星期映射，大致思想是取最后一个星期的数据，比如要预测星期1的销售量为上一个星期1的销售量，预测星期2的销售量为上一个星期2的销售量，预测星期3的销售量为上一个星期3的销售量  等等

sdk-python-指数平滑 使用指数平滑进行预测

sdk-python-指数平滑-动态alpha  使用指数平滑进行预测 并动态调制参数的值

他山之石
tinynumpy https://github.com/wadetb/tinynumpy

## 结果 
网址：http://codecraft.devcloud.huaweicloud.com/home/index

西北赛区44名
账号 asuren  密码：

## 代码托管
### 准备阶段：配置用户名和邮箱
```cmd
git config --global user.email "18835109707@163.com"
git config --global user.name "asuren"
```
### 准备阶段：生成公钥并提交给DevCloud
`C:\Users\zhang\.ssh`目录下
* id_rsa 私钥
* id_rsa.pub 公钥
* known_hosts 信任主机列表
1. 生成新密钥：
```cmd
ssh-keygen -t rsa -C "您的email"
```
在回车中会提示你输入一个密码，这个密码会在你提交项目时使用，如果为空的话提交项目时则不用输入，建议采用不输入密码方式。
密钥生成后您可以在你本机系统盘下，您的用户文件夹里发现一个.ssh文件，其中的id_rsa.pub文件里储存的即为刚刚生成的ssh公钥。
2. 使用命令直接复制密钥到剪贴板
```cmd
clip < C:/Users/zhang/.ssh/id_rsa.pub
```
3. 粘贴到网页上
###  在网页上新建一个代码库
1. 粘贴代码库（组委会已经做好了）的地址，推荐使用git协议。
2. 回到cmd 
```cmd
git clone git@codehub.devcloud.huaweicloud.com:7e63ee4315234b48b210814f35cef9a4/JavaTest.git
```

## 比赛——本地调试
1. 下载SDK
```cmd
git clone git@codehub.devcloud.huaweicloud.com:cf1cfc46d47a438b9e2c5c7a1e333ed0/sdk-java.git
```
2. 打开项目目录
```cmd
cd sdk-java
```
3. 修改Predict.java
```cmd
cd code/ecs/src/com/elasticcloudservice/predict
rm -rf Predict.java
```
4. 使用build.sh编译后打包;
```cmd
sh build.sh
```
5. 如果编译成功会在bin路径下生成可执行二进制文件"ecs.jar"；
6. 打开bin目录
```cmd
cd bin
```
7. 调用并调试程序，trainData input output
```cmd
sh startup.sh /home/controller/初赛文档/用例示例/TrainData_2015.1.1_2015.2.19.txt /home/controller/初赛文档/用例示例/input_5flavors_cpu_7days.txt /home/controller/初赛文档/用例示例/output.txt 
```
8. 在你指定的目录下寻找output.txt

## 比赛——提交代码
1. 将修改之后文件拷贝至git管理的文件夹下
2. `git status`
3. `git add --all`
4. `git commit --m "提交的log"`
5. `git push`

## 3.17
按照水哥要求，按照小时对原始数据进行预处理
```java
//写文件
@Test
public void readForHourTest() throws ParseException {
    String path = MyUtils.getFile("inputs","").getAbsolutePath();
    File dictionary = new File(path);
    File[] files = dictionary.listFiles();
    for(File file : files){
        path = file.getAbsolutePath();
        System.out.println("正在处理 "+path );
        String[] lines = FileUtil.read(path,null);
        PreprocessData preprocessData = new PreprocessData(lines);
        ArrayList<ArrayList<Integer>> res   = preprocessData.readForHour();

        String []contents = new String[res.size()];
        for(int i=0;i<res.size();i++){
            System.out.println("型号"+(i+1)+" "+res.get(i).toString());
            contents[i] = "型号"+(i+1)+" "+res.get(i).toString();
        }
  FileUtil.write(MyUtils.getFile("output",file.getName()).getAbsolutePath(),contents,false);
    }
}
```

## 3.23
### 新开了一个项目：sdk-java-own-2
采用求取平均值的做法，拿到了60分

### 新开了一个项目：sdk-java-own-3
采用求最后300条数据的平均值的做法，拿到70分

### 采用局部加权线性回归函数
```cmd
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python\src\ecs\ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
## 3.24
### 对项目：sdk-java-own-3
采用求最后100条数据的平均值的做法，拿到60分
采用求最后200条数据的平均值的做法，拿到71.5分
采用求最后300条数据的平均值的做法，拿到70分
采用求最后400条数据的平均值的做法，拿到87分
采用求最后500条数据的平均值的做法，拿到81分
采用求最后600条数据的平均值的做法，拿到78分

采用求最后400条数据的平均值的做法，还是拿到87分
采用求最后401条数据的平均值的做法，拿到相同分数
### 新建项目：sdk-python
位置：F:\睿云实验室\华为\sdk-python
搭建了python项目的框架

### 新建项目：sdk-python2

## 3.26
练习赛的进程已经过半，我们要加快进度了。sdk-python这个项目主要是完成局部加权线性回归。（参考文献：https://blog.csdn.net/HerosOfEarth/article/details/51969517 ）
## 3.27
使用一个轻量级的numpy的开源项目，实现了with out numpy
```cmd
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python-提交版\src\ecs\ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
## 3.28
程序一直跑奔溃，怀疑：
1. 引入了自己写的类——我把所有代码写在一个文件中了。之后的实验也表明不是这个错误
2. 环境不一样？因为本地是windows，而测试环境是ubuntu
  在我的阿里云上运行：
```cmd
python /home/admin/sdk-python-提交版/src/ecs/ecs.py /home/admin/初赛文档/用例示例/TrainData_2015.1.1_2015.2.19.txt /home/admin/初赛文档/用例示例/input_5flavors_cpu_7days.txt  /home/admin/初赛文档/用例示例/output.txt
```
在实验室的ubuntu上运行：
```cmd
python /home/controller/sdk-python-提交版/src/ecs/ecs.py /home/controller/初赛文档/用例示例/TrainData_2015.1.1_2015.2.19.txt /home/controller/初赛文档/用例示例/input_5flavors_cpu_7days.txt  /home/controller/初赛文档/用例示例/output.txt
```

终于找出问题了，不是自定义类的问题，也不是环境问题，而是输出了中文，我把所有的print语句删除了就没事了

k = 500，得到了3.055分
k = 300，拿到了2.896分
k = 1，拿到了0分
k = 1000，拿到了3.144分

这分数也太低了，不会是装箱时候出问题了吧。我决定再写一个python版本的平均值
新建了项目sdk-python-平均值
```cmd
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python-平均值\src\ecs\ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
平均值法，使用401条数据，正常情况下应该和java的得分相同（76分），但是只得了8分。基本可以确认是装箱部分出错了

## 3.29
装箱部分的问题已经解决，不过奇怪的是，同样是采用了400条数据
```cmd
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python_局部加权线性回归\src\ecs\ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
k=1000	54.709分
k=500       72.943分
k=475	73.978分
k=450    75.526分
k=425	72.641分
k=400	73.149分
k=300	71.04分
k=200	69.135分
k=50	30分
## 3.30
```cmd
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python_局部加权线性回归_副本\src\ecs\ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
### 使用阈值为3的去噪方法
k=475 去噪	54.46分
k=200 去噪	61.437分
### 使用阈值为4的去噪方法
k=450		68.135分
### 使用正态分布的思路去噪
取均值=1 计算方差
K=1000	46.107
k=450	71.647
K=300	69.654
K=100	48.971
K=200	69.51
K=250	67.457

### 使用python3 为了画图
```cmd
python F://睿云实验室//华为//sdk-python_局部加权线性回归_副本//src//ecs//ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```

## 3.31
水哥总是说数据有问题，今天我打算把提取数据的程序单独拿出来，成立一个新的项目——ProcessDataset

## 4.3
时间过的很快，忽然发现自己没有完成ProcessDataset项目
我打算使用平均值的那个项目测试 排序方式 对成绩的影响
```cmd
F:\PythonDev\py27\python.exe F://睿云实验室//华为//sdk-python-平均值//src//ecs//ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
修改排序方式对成绩没有影响
k=400  得分为75.811
k=200  得分为64.404
k=450  得分为73.494

## 4.3
开始检查ProcessDataset项目
代码没错啊 以2015.1为例，2015-01-01 19:03:32到2015-01-30 00:02:47  一共是29天，29*24=696 
又因为2015-01-01是从19点开始的，再减一个19，就是677个小时啊

## 4.4
我决定开始实现按照星期映射的那个算法，新建了一个项目 sdk-python-星期映射
```cmd
F:\PythonDev\py27\python.exe F://睿云实验室//华为//sdk-python-星期映射//src//ecs//ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
从最后一条记录向上找，找全一个星期

## 4.9
1. 使用天作为时间间隔
2. 最后一天没有请求数据，注意训练集的结尾
3. 将装箱问题规约到0-1背包问题，比如说要优化内存，则：
* 将内存的利用率规约为价值
* 将cpu不超分作为约束条件
4. 去噪的思路：对请求数据做一阶差分，一阶差分符合正态分布，使用平均值+2\*标准差 平均值-2\*标准差  作为阈值


  我实现markov模型，老大的同学实现GM(1,1)模型

## 4.10
水哥给的matlab源码
马尔科夫
```matlab
clc
clear all
close all

load('train_data.mat');
load('test_data.mat');

%去除异常数据
for i = 1:15
    temp1 = mean(train_data(:,i));
    temp2 = std(train_data(:,i));
    kt_min = temp1 - 0.5*temp2;
    kt_max = temp1 + 2*temp2;
    temp3 = mean(train_data(train_data(:,i)>=kt_min|train_data(:,i)<=kt_max,i));
    train_data(train_data(:,i)<kt_min|train_data(:,i)>kt_max,i) = round(temp3);
    test_data(test_data(:,i)<kt_min|test_data(:,i)>kt_max,i) = round(temp3);
end

N = 7; %预测未来N点
[Seq_Len, Flavor_Num] = size(train_data); %时间序列长度,待预测规格数
Seq_Pre = zeros(N, Flavor_Num);           %初始化预测序列矩阵
P_Order = max(train_data)+1;     %计算状态转移矩阵阶数(0台也为一种状态)
for i = 1:Flavor_Num
    
    %初始化状态转移矩阵
    Pi = zeros(P_Order(i));
    for j = 1 : Seq_Len - 1
        Pi(train_data(j,i)+1,train_data(j+1,i)+1) = Pi(train_data(j,i)+1,train_data(j+1,i)+1) + 1;
    end
    for j = 1 : P_Order(i)
        sum_Pri = sum( Pi(j,:));
        if sum_Pri ~= 0
           Pi(j,:) = Pi(j,:)/sum( Pi(j,:));
        end
    end
    
    %初始化状态矩阵
    S0 = zeros(1,P_Order(i));
    S0(train_data(Seq_Len,i)+1) = 1;
   
    %预测
    Sk = S0;
    for k = 1:N
        Sk = Sk * Pi;
        Sk_Pmax = find(Sk == max(Sk))-1;
        Seq_Pre(k,i) = round(mean(Sk_Pmax));
    end
end

%预测总和
Pre_SumSeq = sum(Seq_Pre);
Act_SumSeq = sum(test_data);
Score = my_score(Act_SumSeq,Pre_SumSeq);
disp('Markov模型预测结果：');
disp(['实际数据：',num2str(Act_SumSeq)]);
disp(['预测数据：',num2str(Pre_SumSeq)]);
disp(['得分：',num2str(Score)]);

%绘图
plot(Pre_SumSeq,'b-.'); hold on; plot(Act_SumSeq,'b-'); hold off;
title('Markov模型预测');
legend('预测数据','实际数据');
```
灰度模型
```matlab
clc
clear all
close all

load('train_data.mat');
load('test_data.mat');

%去除异常数据
for i = 1:15
    temp1 = mean(train_data(:,i));
    temp2 = std(train_data(:,i));
    kt_min = temp1 - 0.5*temp2; kt_max = temp1 + 2*temp2;
    temp3 = mean(train_data(train_data(:,i)>=kt_min|train_data(:,i)<=kt_max,i));
    train_data(train_data(:,i)<kt_min|train_data(:,i)>kt_max,i) = round(temp3);
    test_data(test_data(:,i)<kt_min|test_data(:,i)>kt_max,i) = round(temp3);
end

N = 7; %预测未来N点
[Seq_Len, Flavor_Num] = size(train_data); %时间序列长度,待预测规格数
Seq_Pre = zeros(N, Flavor_Num);           %初始化预测序列矩阵
for i = 1:15
    Seq_fi = cumsum(train_data(:,i));               %做AGO累加处理
    z = zeros(Seq_Len-1,1);
    for j = 1:Seq_Len-1
        z(j)=0.5*(Seq_fi(j)+Seq_fi(j+1));%计算紧邻均值，也就是白化背景值
    end
    B=[-z,ones(Seq_Len-1,1)];
    u = inv(B'*B)*B'*train_data(2:Seq_Len,i);
    %利用GM(1,1)具体表达式计算原始序列的AGO
    forecast1=(train_data(1,i)-u(2)/u(1)).*exp(-u(1).*(Seq_Len-1:Seq_Len+N-1))+u(2)/u(1);
    exchange=diff(forecast1);          %把AGO输出值进行累减
    Seq_Pre(:,i)=exchange;         %输出灰色模型预测值
end

Pre_SumSeq = round(sum(Seq_Pre));
Act_SumSeq = sum(test_data);
Score = my_score(Act_SumSeq,Pre_SumSeq);
disp('GM(1,1)模型预测结果：');
disp(['实际数据：',num2str(Act_SumSeq)]);
disp(['预测数据：',num2str(Pre_SumSeq)]);
disp(['得分：',num2str(Score)]);

%绘图
plot(Pre_SumSeq,'b-.'); hold on; plot(Act_SumSeq,'b-'); hold off;
title('GM(1,1)模型预测');
legend('预测数据','实际数据');
```
水哥的嘱托
```
我的train_data是55*15的矩阵，test_data是7*15的矩阵
去噪部分先不管
```

## 4.10 快4.11
完成了灰度模型
现在开始写按照天统计台数的逻辑 训练集是2015_12 测试集是2016_1的最后七天
```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\4.9合组讨论\ecs.py F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```
```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\4.9合组讨论\ecs.py F://睿云实验室//华为//4.9合组讨论//训练集.txt F://睿云实验室//华为//4.9合组讨论//input.txt  F://睿云实验室//华为//4.9合组讨论//output.txt
```
## 4.11 晚上
k=20 然后测试局部加权线性回归 按天
```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python_局部加权线性回归_按天\src\ecs\ecs.py F://睿云实验室//华为//4.9合组讨论//训练集.txt F://睿云实验室//华为//4.9合组讨论//input.txt  F://睿云实验室//华为//4.9合组讨论//output.txt
```

```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python-提交版\src\ecs\ecs.py F://睿云实验室//华为//4.9合组讨论//训练集.txt F://睿云实验室//华为//4.9合组讨论//input.txt  F://睿云实验室//华为//4.9合组讨论//output.txt
```

## 4.12
```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\4.9合组讨论\ecs.py F://睿云实验室//华为//4.9合组讨论//训练集.txt F://睿云实验室//华为//4.9合组讨论//input.txt  F://睿云实验室//华为//4.9合组讨论//output.txt
```

## 4.13
最后400条求平均值，加去噪
```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python-平均值-最后400条-去噪\src\ecs\ecs.py F://睿云实验室//华为//4.9合组讨论//训练集.txt F://睿云实验室//华为//4.9合组讨论//input.txt  F://睿云实验室//华为//4.9合组讨论//output.txt
```
一些代码段

###  训练集的时间跨度
```python
#########训练集的时间跨度#####训练第一天的0点 预测第一天的0点##################
ecs_first_date_zero = ecs_lines[0].split("\t")[2].strip().split()[0]+" "+"00:00:00"
ecs_first_date_zero = time.strptime(ecs_first_date_zero, "%Y-%m-%d %H:%M:%S")
input_first_date_zero = input_lines[-2].strip().split()[0]+" "+"00:00:00"
input_first_date_zero = time.strptime(input_first_date_zero, "%Y-%m-%d %H:%M:%S")
kuadu_first_last_day = (time.mktime(input_first_date_zero)-time.mktime(ecs_first_date_zero))/nd
kuadu_first_last_day = int(kuadu_first_last_day)
#print(u"时间跨度为"+str(kuadu_first_last_day))
#########训练集的时间跨度#####训练第一天的0点 预测第一天的0点##################
```
### 获取训练集中的数据 行数为虚拟机的规格 列数是天数
```python
##########获取训练集中的数据 行数为虚拟机的规格 列数是天数##################
ecs_xunlian = []
for i in range(30):
	t = []
	for j in range(kuadu_first_last_day):
		t.append(0)
	ecs_xunlian.append(t)

for ecs_line in ecs_lines:
	ecs_line = ecs_line.strip()
	ecs_now_name = ecs_line.split("\t")[1]
	ecs_now_no = int(ecs_now_name.replace("flavor",""))

	ecs_now_date = ecs_line.split("\t")[2]
	ecs_now_date = time.strptime(ecs_now_date, "%Y-%m-%d %H:%M:%S")
	#print(ecs_now_name+" "+str(ecs_now_no)+" "+str(ecs_now_date))
	ecs_kuadu_first_now_day = (time.mktime(ecs_now_date)-time.mktime(ecs_first_date_zero))/nd
	ecs_kuadu_first_now_day = int(ecs_kuadu_first_now_day)
	ecs_xunlian[ecs_now_no][ecs_kuadu_first_now_day] = ecs_xunlian[ecs_now_no][ecs_kuadu_first_now_day] + 1
	
	
print(u"训练集中的数据")
print(len(ecs_xunlian))
print(len(ecs_xunlian[0]))
temp = pymatrix.matrix(ecs_xunlian)
print(temp)
	
##########获取训练集中的数据 行数为虚拟机的规格 列数是天数##################
```
### 去噪的代码
```python
###############去噪的代码################
#获得要预测的规格
input_num = int(input_lines[2].strip())
input_nos = []
for i in range(input_num):
input_line = input_lines[i+3]
input_no = input_line.strip().split()[0].replace("flavor","")
input_no = int(input_no)
input_nos.append(input_no)
train_data = fluth_data.quZao2(ecs_xunlian,input_nos)
'''
for t in train_data:
print(t)
print(len(train_data))
print(len(train_data[0]))
'''
##############去噪的代码################
```
### 获得预测跨度
```python
###########获得预测跨度####################
#预测的第一天 预测的最后一天
input_first_date = input_lines[-2].strip()
input_first_date = time.strptime(input_first_date, "%Y-%m-%d %H:%M:%S")
input_last_date = input_lines[-1].strip()
input_last_date = time.strptime(input_last_date, "%Y-%m-%d %H:%M:%S")

kuadu_first_last_day = (time.mktime(input_last_date)-time.mktime(input_first_date))/nd
kuadu_first_last_day = int(kuadu_first_last_day)
#print(u"时间跨度为："+str(kuadu_first_last_day))
###########获得预测跨度####################
```

###  获得物理机的规格
```python
################# 获得物理机的规格###############
input_wuLiJi_cpu = int(input_lines[0].split(" ")[0])
input_wuLiJi_mem = int(input_lines[0].split(" ")[1])
########################获得物理机的规格#########
```
### 获得需要预测的虚拟机的所有信息 name cpu mem
```python
############## 获得需要预测的虚拟机的所有信息 name cpu mem####
#input文件中需要预测的虚拟机[("flavor1",12,1024),("flavor1",12,1024)]
input_xuNiJis = []
i = 3
while(i<3 + int(input_lines[2].strip())):
	input_now_flavor_name = input_lines[i].strip().split(" ")[0]
	input_now_flavor_CPU = int(input_lines[i].strip().split(" ")[1])
	input_now_flavor_MEM = int(input_lines[i].strip().split(" ")[2])
	input_now_flavor = [input_now_flavor_name,input_now_flavor_CPU,input_now_flavor_MEM]
	input_xuNiJis.append(input_now_flavor)
	i = i + 1
print(input_xuNiJis)
############## 获得需要预测的虚拟机的所有信息 name cpu mem####
```
### 需要预测的规格数
```python
# 获得要预测的规格
input_num = int(input_lines[2].strip())
```
### 优化的维度 装箱 输出结果
```python
##################### 优化的维度 装箱 输出结果#####################
input_weidu = input_lines[3+int(input_lines[2].strip())+1].strip()
if(input_weidu=="CPU"):
	zx_wuLiJis,_ = memory_alloction.get_memory_allocation(input_wuLiJi_cpu,input_wuLiJi_mem,cpus,mems,names)
elif(input_weidu=="MEM"):
	zx_wuLiJis,_ = memory_alloction.get_memory_allocation(input_wuLiJi_mem,input_wuLiJi_cpu,mems,cpus,names)
else:
	print("出错了，别玩了")
print(zx_wuLiJis)
#开始输出结果
result=[]
sum_t = 0
for input_xuNiJi in input_xuNiJis:
	input_xuNiJi_name = input_xuNiJi[0]
	input_xuNiJi_num = yuce_flvorname_flavornum_s.get(input_xuNiJi_name)
	sum_t = sum_t + input_xuNiJi_num
	result.append(input_xuNiJi_name+" "+str(input_xuNiJi_num))
result.insert(0,str(sum_t))
result.append("")
result.append(len(zx_wuLiJis))
print(result)
for i in range(0,len(zx_wuLiJis),1):
	zx_wuLiJi = zx_wuLiJis[i]
	sss = str(i+1)
	temp = {}
	for xuNiJi in zx_wuLiJi :
		if(temp.has_key(xuNiJi)):
			temp[xuNiJi] = temp[xuNiJi] + 1
		else:
			temp[xuNiJi] = 1
	print(temp)
	for name in temp:
		sss = sss+" "+name+" "+str(temp[name])
	print(sss)
	result.append(sss.strip())

return result
```

## 4.13 10点
阈值为40 N=2 64
阈值为100 N=2 64
阈值为100 N=1 58
```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python_局部加权线性回归_修改之后\src\ecs\ecs.py F://睿云实验室//华为//4.9合组讨论//训练集.txt F://睿云实验室//华为//4.9合组讨论//input.txt  F://睿云实验室//华为//4.9合组讨论//output.txt
```

新的去噪 修改了逆向的bug

## 修复bug
```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python-指数平滑\ecs.py F://睿云实验室//华为//3个月的数据集//训练集.txt F://睿云实验室//华为//3个月的数据集//input.txt  F://睿云实验室//华为//3个月的数据集//output.txt
```

```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python-指数平滑\ecs.py  F://睿云实验室//华为//初赛文档//用例示例//TrainData_2015.1.1_2015.2.19.txt F://睿云实验室//华为//初赛文档//用例示例//input_5flavors_cpu_7days.txt  F://睿云实验室//华为//初赛文档//用例示例//output.txt
```


```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\sdk-python-指数平滑\ecs.py  /home/admin/初赛文档/用例示例/TrainData_2015.1.1_2015.2.19.txt /home/admin/初赛文档/用例示例/input_5flavors_cpu_7days.txt  /home/admin/初赛文档/用例示例/output.txt
```

```bash
F:\PythonDev\py27\python.exe F:\睿云实验室\华为\4.14预备上传\sdk-python_局部加权线性回归_修改之后\src\ecs\ecs.py F://睿云实验室//华为//3个月的数据集//训练集.txt F://睿云实验室//华为//3个月的数据集//input.txt  F://睿云实验室//华为//3个月的数据集//output.txt
```

## 最后提交的代码
嗯 最后使用的是星期映射
