def preprocess(arr,N):
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
    
def pp(arr,N):
    res = []
    for a in arr:
        res.append(preprocess(a,N))
    return res
if __name__ == "__main__":
    arr=[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1];
    N = 7
    print(preprocess(arr,N))