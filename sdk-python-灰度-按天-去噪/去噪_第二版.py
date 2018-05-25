import math
arr=list([1]*20)
arr.append(3)
arr.append(3)
arr.append(3)
arr = arr + list([1]*27)

arr = list([1, 3, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1])
print("数据总数："+str(len(arr)))

print("原始数据："+str(arr))
diff = list([])

for i in range(1,len(arr),1):
    diff.append(arr[i]-arr[i-1])
diff_sum = sum(diff)

diff_average = diff_sum/len(diff)
print("均值："+str(diff_average))

diff_delta = 0
for i in range(0,len(diff),1):
    diff_delta = diff_delta + math.pow(diff[i]-diff_average,2)
diff_delta = diff_delta/len(diff)
print("标准差："+str(diff_delta))
diff_delta = math.sqrt(diff_delta)
print("标准差："+str(diff_delta))

yuzhi_high = diff_average + 2 * diff_delta
yuzhi_low = diff_average - 2 * diff_delta
print("阈值（高点）"+str(yuzhi_high))
print("阈值（低点）"+str(yuzhi_low))


for i in range(0,len(diff),1):
    if diff[i]>yuzhi_high:
        arr[i+1] = arr[i]
        print(str(diff[i])+"偏大")
    elif diff[i]<yuzhi_low:
        arr[i] = arr[i-1]
        print(str(diff[i])+"偏小")
    else:
        pass
        
print("去噪之后的数据："+str(arr))