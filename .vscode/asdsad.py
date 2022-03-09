a = int(input())
b = list(map(int,input().split()))
num = a
for i in range(a):
    if b[i] == 1:
        num -= 1
    elif b[i] == 2:
        continue
    elif b[i] == 3:
        continue
    elif b[i]%2 == 0:
        num -= 1
    else:
        for x in range(500):
            if b[i] == 2*x+5:
                for k in range(x+1):
                    if b[i]%(2*k+3)==0:
                        num -= 1
                        break
print(num)