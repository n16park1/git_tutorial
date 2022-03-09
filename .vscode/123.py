def find_same_string(L):
    n = len(L)
    a = set()
    for i in range(n):
        for j in range(i+1,n):
            if L[i] == L[j]:
                a.add(L[i])
    return a

L = list(map(int,input().split()))
print(find_same_string(L))
    
