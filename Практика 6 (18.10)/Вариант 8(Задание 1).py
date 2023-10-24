l=int(input())
s=1
f=0
n=[int(input()) for i in range(l)]
for k in n:
    s*=k
    f+=k
print(s, f)