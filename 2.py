def maxWater(a, n) : 
    res = 0;
    for i in range(1, n - 1):
        l = a[i];
        for j in range(i):
            l = max(l, a[j]);
        r = a[i];
         
        for j in range(i + 1 , n):
            r = max(r, a[j]);
        res = res + (min(l, r) - a[i]);
    return res;
a= list(map(int,input().split(',')))
n = len(a);     
print(maxWater(a, n));
