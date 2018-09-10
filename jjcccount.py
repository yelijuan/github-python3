#coding=utf-8

import re
class heheda:

    def __init__(self,str2):
        self.str1=str2
        self.ss = re.split(r"([/s+*-])", str2)  
        
    def chu(self):
            i=self.ss.index("/")
            chu1=int(self.ss[i-1])/int(self.ss[i+1])
            self.ss.insert(i-1,chu1)
            self.ss.pop(i)
            self.ss.pop(i)
            self.ss.pop(i)
            if len(self.ss)==1:
                return chu1
            else:
                self.ss
            
    
    def cheng(self):
            i=self.ss.index("*")
            chu1=int(self.ss[i-1])*int(self.ss[i+1])
            self.ss.insert(i-1,chu1)
            self.ss.pop(i)
            self.ss.pop(i)
            self.ss.pop(i)
            if len(self.ss)==1:
                return chu1
            else:
                self.ss
    def jia(self):
            i=self.ss.index("+")
            chu1=int(self.ss[i-1])+int(self.ss[i+1])
            self.ss.insert(i-1,chu1)
            self.ss.pop(i)
            self.ss.pop(i)
            self.ss.pop(i)
            if len(self.ss)==1:
                return chu1
            else:
                self.ss
                
            
            
    def jian(self):
            i=self.ss.index("-")
            chu1=int(self.ss[i-1])-int(self.ss[i+1])
            self.ss.insert(i-1,chu1)
            self.ss.pop(i)
            self.ss.pop(i)
            self.ss.pop(i)
            if len(self.ss)==1:
                return chu1
            else:
                self.ss
                
    def jisuan(self):
        for a in range(0,len(self.ss)):
            try:
                i=self.ss.index("/")
            except ValueError:
                i=-1
            try:
                j=self.ss.index("*")
            except ValueError:
                j=-1
            
            if i>0 and j>0:
                if i<j:
                    self.chu()
                else:
                    self.cheng()
            elif i>0 and j<0:
                    self.chu()
            elif i<0 and j>0:
                    self.cheng()
            else:
                
                try:
                    a=self.ss.index("+")
                except  ValueError:
                    a=-1  
                try:
                    b=self.ss.index("-")
                except  ValueError:
                    b=-1 
                if a>0 and b>0 :
                    if a<b:  
                        self.jian()
                    else:
                        self.jia()
                elif a>0 and b<0:
                    self.jia()
                elif a<0 and b>0:
                    self.jian()
                elif len(self.ss)==1:
                    return self.ss[0]
                else:
                    return int(self.ss[0:])
                    

