case = int(input())
for testCase in range(case):
    num = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    p = [a[0]]
    for i in range(1,num - 1):
        if a[i] == p[-1]:
            p.append(b[i] if b[i] != p[-1] else c[i])
        else:
            p.append(a[i])
    if a[num - 1] == p[0] or a[num - 1] == p[-1]:
        if b[num - 1] != p[0] and b[num - 1] != p[-1]:
            p.append(b[num - 1])
        else:
            p.append(c[num - 1])
    else:
        p.append(a[num - 1])
    print(' '.join([str(i) for i in p]))
