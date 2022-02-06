def mysticalArray(k, arr, n):
    ans=0
    while 1:
        f=0
        for i in range(n-1):
            if arr[i]>=arr[i+1]:
                f=1
                ans+=1
                arr[i+1]+=k
        if f==0:
            print(ans)