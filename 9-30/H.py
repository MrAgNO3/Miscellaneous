testCase = int(input())
for tc in range(testCase):
    n = int(input())
    num = list(map(int,input().split()))
    if n <= 2:
        print(0)
        continue
    book = [i == 0 for i in num]
    cnt = 0
    t1,t2 = [],[]
    for f in range(n - 2):
        for s in range(f + 1,n):
            if book[f] == book[s] == True:
                for i in range(f + 1,s):
                    if not book[i] and f not in t1 and s not in t1 and i not in t1 and num[i] not in t2:
                        t1.append(f)
                        t1.append(i)
                        t1.append(s)
                        t2.append(num[i])
                        cnt += 1
    print(cnt)
