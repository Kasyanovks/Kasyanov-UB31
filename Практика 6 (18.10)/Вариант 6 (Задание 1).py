n=[int(input()) for i in range(10)]
for k in range(len(n)):
    if n[k]<0 and n[k+1]<0:
        print(n[k], n[k+1])