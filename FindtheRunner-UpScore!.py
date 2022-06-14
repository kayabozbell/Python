n = int(input())
arr = map(int, input().split())
a=list(arr)
maxnum=max(a)
order=0
runnerup=0
while order<n :
    if a[order]>runnerup and a[order] != maxnum:
        runnerup=a[order]
    order += 1
print(runnerup)
print(maxnum)