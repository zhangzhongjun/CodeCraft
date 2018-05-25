#coding=utf-8
def preprocess(arr,N):
    N = int(N)
    t1 = len(arr) % N
    t2 = int(len(arr) / N)
    
    res = []
    for i in range(t2):
        temp = arr[t1+N*i:t1+N*i+N:1]
        #print(temp)
        #print(sum(temp))
        res.append(sum(temp))
        #print(i,t1+N*i,t1+N*i+N)
    return res
    
'''
将arr按照N分片
'''
def pp(arr,N):
    res = []
    for a in arr:
        temp = preprocess(a[1::1],N)
        res.append([0]+temp)
    return res
    
'''
增加一列0
'''
def pp2(arr):
    res = []
    for a in arr:
        a = [0]+a
        res.append(a)
    return res
    
if __name__ == "__main__":
    arr=[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1];
    arr = arr[1::1]
    N = 7
    print(preprocess(arr,N))