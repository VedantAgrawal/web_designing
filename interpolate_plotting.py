import random
import os
from numpy import*
import numpy.polynomial.polynomial as P
import matplotlib.pyplot as plt
# class-Interpolation

class Interpolate:
    
    
    def solve(self,U,V,method):
        if(method=="newton"):
            return (self.Newton(U,V))
        else:
            return (self.Lagrange(U,V))
    def pattern(self,cofficient):
        l=len(cofficient);
        temp=[];
        for i in range(l-1):
            temp.append(str(cofficient[l-(i+1)])+'x^'+str(l-(i+1))+str('+'))
        temp.append(str(cofficient[0])+'x^'+str(0));
        str1=''.join(temp)
        return(str1)    

    def Lagrange(self,U,V):                                                
       
        
       
        n=len(U)                                                           
        w=(-1*U[0],1)                                                      
        for i in range(1,n):
            w=P.polymul(w,(-1*U[i],1))                                    
        result=array([0.0 for i in range(len(w)-1)])                    
        derivative=P.polyder(w)                                             
        for i in range(n):
            result+=(P.polydiv(w,(-1*U[i],1))[0]*V[i])/P.polyval(U[i],derivative)


        temp=list(result);
        cofficient=temp
        l=len(cofficient);
        temp=[];
        for i in range(l-1):
            temp.append(str(cofficient[l-(i+1)])+'x^'+str(l-(i+1))+str('+'))
        temp.append(str(cofficient[0])+'x^'+str(0));
        str1=''.join(temp)
        return(str1)   
                                                         
   
    
    def plot(self,U,V,ctr):
        X1=arange(min(U)-2,max(U)+2,0.1)
        x=[1]
        for i in range(len(U)):
            x=P.polymul(x,[-1*U[i],1])
        plt.axis([-10,10,min(V)-1,max(V)+1])
        b=[0]
        for i in range(len(U)):
            a=P.polydiv(x,[-1*U[i],1])
            b=P.polyadd(P.polymul((P.polydiv(a[0],P.polyval(U[i],a[0])))[0],[V[i]]),b)
            Y=P.polyval(X1,P.polymul((P.polydiv(a[0],P.polyval(U[i],a[0])))[0],[V[i]]))
            plt.plot(X1,Y,'y')
        plt.plot(U,V,'ro')
        X1=arange(-5,5,0.1)
        Y=P.polyval(X1,b)
        plt.plot(X1,Y,'b',label='Required Polynomial')
        plt.plot((-8,8),(0,0),'k')
        
        plt.grid(b=True, which='both', color='0.65',linestyle='-')
        Y=list(Y)
        plt.plot((0,0),(-max(Y)-5,max(Y)+5),'k')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.legend(loc=1)
        filename = "this_plot"+str(ctr)+".png"
        path = "C:\\Users\HP\Anaconda3\static"
        fullpath = os.path.join(path, filename)
        plt.savefig(fullpath)

