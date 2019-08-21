import numpy as np
import math

class Graph(object):
    def __init__(self,size):
        self.adjMatrix =np.zeros((size,size))
        self.size=size
        self.EdgeCount=0
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        self.EdgeCount+=1
        
    def removeEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
        self.EdgeCount-=1


    def len(self):
        return self.size

    def Edges(self):
        return self.EdgeCount

l=[]
def IsomorpismCheck(g1,g2):
    if g1.len()==g2.len() and g1.Edges()==g2.Edges():
        s=g1.len()

        a=np.arange(s)
        b=np.arange(s)
        heapPermutation(a,b,s,s)
        k=False
        
        for i in range(math.factorial(s)):
            P=np.zeros((s,s))
            for j in range(s):
                P[(l[i][j][0])][(l[i][j][1])]=1
            D=np.dot(P,g2.adjMatrix)
            Pt=np.transpose(P)
            SS=np.dot(D,Pt)
            if (np.array_equal(SS,g1.adjMatrix)):
                print("Graphs are Isomorphic")
                k=True
                break

            if k:
                break

        if k==False:
            print("Graphs are not Isomorphic")
        
    else:
        print ("Graphs are not Isomorphic")


def heapPermutation(a,b, size,  n ):
    
    if (size == 1):
        x=list(zip(b,a))
        l.append(x)
        
         
    for i in range(size):
        heapPermutation(a,b,size-1,n)
        if (size%2==1):
            temp=a[0]
            a[0]=a[size-1]
            a[size-1]=temp
        else:
            temp=a[i]
            a[i]=a[size-1]
            a[size-1]=temp




g1=Graph(6)
g2=Graph(6)

g1.addEdge(0,1)
g1.addEdge(0,3)
g1.addEdge(0,5)
g1.addEdge(1,2)
g1.addEdge(1,4)
g1.addEdge(2,3)
g1.addEdge(2,5)
g1.addEdge(3,4)
g1.addEdge(4,5)


g2.addEdge(0,1)
g2.addEdge(0,3)
g2.addEdge(0,5)
g2.addEdge(1,2)
g2.addEdge(1,4)
g2.addEdge(2,3)
g2.addEdge(3,4)
g2.addEdge(4,5)

IsomorpismCheck(g1,g2)
