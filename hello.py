import sys
input = sys.stdin.readline

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

T = int(input())
for _ in range(T):
    n = input()
    N = sorted(map(int,input().split()))
    m = input()
    M = map(int, input().split())
    for l in M:
        print(binary(l,N,0,n-1))