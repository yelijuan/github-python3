#codng=utf-8

import os
print(dir(os))
aa=[]
for i in range(len(dir(os))):
    try:
        j=dir(os)[i].index("O")
    except ValueError:
        j=-1
    if j>0:
        aa.append(dir(os)[i])

print(aa)
        
    