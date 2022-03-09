import sys
n = int(sys.stdin.readline())
arr = []
count = [0]*8001
max_count = 0
for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
    count[a] +=1
    max_count = max(max_count, count[a])
avg = round(sum(arr)/n)
arr.sort()
mid = arr[n//2]
bin = 0
cnt = 0
for i in range(-4000,4001):
    if max_count == count[i]:
        bin = i
        cnt += 1
        if cnt == 2:
            break
bum = max(arr) - min(arr)
print("%.0f"%(avg))
print(mid)
print(bin)
print(bum)