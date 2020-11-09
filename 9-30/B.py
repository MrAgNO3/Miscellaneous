testCase = int(input())
def func(arr,k):
    t,cnt = -1,0
    for i in range(len(arr)):
        if arr[i] != t:
            cnt += 1
        t = arr[i]
        if cnt == k + 1:
            return [0] * i + [j - arr[i - 1] for j in arr[i:]]
    return [0] * len(arr)
for tc in range(testCase):
    m,flag = 0,0
    n,k = map(int,input().split())
    num = list(map(int,input().split()))
    while num.count(0) != len(num):
        t = num.copy()
        num = func(num,k)
        if t == num:
            flag = 1
            break
        m += 1
    print(-1 if flag else m)
