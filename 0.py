import sys
input=sys.stdin.readline

L = int(input())
arr = list(map(int,input().split()))
n = int(input())
arr.sort()
tmp = 0
for i in range(L):
    if arr[i] ==n:
        tmp = 1
        break
    if arr[i] > n:
        k = i
        break
if tmp == 0:
    cnt = (n-arr[k-1]-1)*(arr[k]-n) + arr[k]-1-n
    print(cnt)
else:
    print(0)