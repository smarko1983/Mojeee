# Bubble Sort algorithm
alist = [15, 2,4,20,4,7,1,30]
for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
print(alist)