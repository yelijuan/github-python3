#coding=utf-8
from itertools import count
def avg1(*argslist):
    sum=0
    for i in range(len(argslist)):
        if str(argslist[i]).isalnum()==True:
            sum +=argslist[i]
            avg=sum/len(argslist)
 
        else :
            return argslist[i],"is not num,only num"
            break
    
        if i==len(argslist)-1:
            return round(avg,2) 
        else:
            continue    
    
