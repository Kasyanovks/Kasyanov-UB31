n=[int(input()) for i in range(10)]
s=0
for k in range(len(n)):
    if n[k]>5:
        s+=n[k]
print(s)