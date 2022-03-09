import sys
input=sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
gcds = [abs(num[1]-num[0])]

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

for j in range(2, n):
    gcds.append(gcd(abs(num[j] - num[j-1]), gcds[0]))
gcds.sort()
ans = []
for k in range(1, int(gcds[0]**0.5)+1):
    if gcds[0]%k ==0:
        ans.append(k)
        ans.append(gcds[0]//k)
ans = list(set(ans))
ans.sort()
for i in ans[1:]:
    print(i,end= ' ')