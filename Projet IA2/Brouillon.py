import numpy as np

b=[]
a=[]
for i in range(0,9):
    if (i+1)%3==0:
        a.append((i+1)*11)
        b.append(a)
        a=[]
    else:
        a.append((i+1)*11)
c=np.array(b)
print(b)
print(c)