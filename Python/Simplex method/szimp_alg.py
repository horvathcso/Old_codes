"""
Created on Fri Mar 26 09:27:45 2021

@author: Csongor
"""


import numpy as np
import fractions
import copy

class Fraction(fractions.Fraction):
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


class Szimplex:
    
    def __init__(self, file):
        """
        Fájl beolvasása, adatok elmentése belőle
        """
        self.list= []
        self.b=[]
        with open(file, "r") as f:
            count=0
            for l in f:
                if count>2:
                    line=l.split(' ')
                    self.list.append([int(line[i]) for i in range(self.n)])
                    self.b.append([int(line[self.n])])
                elif count==0:    
                    self.n=int(l) #változók száma
                elif count==1:
                    self.m=int(l) #sorok száma
                elif count==2:
                    line=l.split(' ')
                    self.c=[int(e) for e in line]
                count+=1
    
    def add_ident(self):
        """
        Az osztályban lévő mátrixhoz egy identitás mátrix hozzácsatolása
        """
        for i,lin in enumerate(self.list):
            for j in range(self.m-1):
                if j!=i:
                    lin.append(0)
                else:
                    lin.append(1)
        self.c=[0 for _ in self.c]
        for _ in range(self.m-1):
            self.c.append(-1)

        
            
    def diag(self, bazis):
        """
        A diagonalizációs eljárás, illetve a szimplex tábla létrehozása, elmentése
        """
        count=0
        matrix=np.hstack((np.array(self.list),np.array(self.b)))+Fraction()
        for i in bazis:
            if matrix[count,i]==0:
                c=count+1
                while True:
                    if matrix[c,i]!=0:
                        slack=copy.deepcopy(matrix[count,:])
                        matrix[count,:]=copy.deepcopy(matrix[c,:])
                        matrix[c,:]=slack
                        break
                    c+=1
            if matrix[count,i]!=1:
                matrix[count,:]=matrix[count,:]*(1/matrix[count,i])
            for j in range(len(matrix)):
                if count!=j and matrix[j,i]!=0:
                    matrix[j,:]=matrix[j,:]-matrix[count,:]*matrix[j,i]
            count+=1

        self.matrix=np.array(matrix)
        self.table=np.column_stack([matrix[:,i] for i in range(len(matrix[0])) if not i in bazis ])
        self.c1=self.c-np.matmul([self.c[i] for i in bazis],matrix[:,:-1])
        self.c_=np.array([self.c1[i] for i in range(len(matrix[0])-1) if not i in bazis])
        self.idbazis=[[i] for i in bazis]
        self.id=[[i] for i in range(len(matrix[0]-1)) if not i in bazis]
        
    def pivotalas(self,i,j):
        """
            Pivotálás az aktuális self.tabel (i,j) eleme alapján

        """
        table=copy.deepcopy(self.table)
        c_=copy.deepcopy(self.c_)
        for k in range(len(self.table)):
            for l in range(len(self.table[0])):
                if l!=j and k!=i:
                    self.table[k][l]=table[k][l]-table[k][j]*table[i][l]/table[i][j]
                elif k==i and l!=j:
                    self.table[k][l]=table[i][l]/table[i][j]
                elif k!=i and l==j:
                    self.table[k][l]=-1*table[k][j]/table[i][j]
                elif  k==i and l==j:
                    self.table[k][l]=1/table[i][j]
        for l in range(len(self.table[0])-1):
            if l!=j:
                self.c_[l]=c_[l]-c_[j]*table[i][l]/table[i][j]
            else:
                self.c_[l]=-1*c_[j]/table[i][j]
        j_=self.id[j]
        self.id[j]=self.idbazis[i]
        self.idbazis[i]=j_
       
        
    def y_vizsg(self): 
        """
        y=c_bB^-1, yA vizsgálata
        """
        min=0
        minhely=self.n+2+self.m
        for i,e in enumerate(self.c_):
            if e>=min and minhely>int(self.id[i][0]) and e !=0:
                minhely=int(self.id[i][0])
                min=e
        if min==0:
            return False   
        elif min>0:
            for i,e in enumerate(self.id):
                if e[0]==minhely:
                    self.j_=minhely
                    self.j=i
                    break
            return True
        
    def x_vizsg(self):
        """
        x vizsgálata, hogy melyik bázisoszlop kerüljön ki
        """
        x_=-1*self.table[:,self.j]
        kisebb_null=False
        l=[]
        for i,e in enumerate(x_) :
            if e<0:
                kisebb_null=True
                l.append([-1*self.table[i,-1]/e,int(self.idbazis[i][0])])
        if kisebb_null==True:
            l=sorted(l,key=lambda x:x[0])
            minhely=l[0][1]
            for i in l:
                if i[0]==l[0][0] and minhely>i[1]:
                    minhely=i[1]
                else: break
            for i,e in enumerate(self.idbazis):
                if e[0]==minhely:
                    self.i=i
                    break
            return True
        else: 
            self.novelo=[None for i in range(self.n)]  
            for i in range(len(self.novelo)):
                if  i!=self.j_:
                    for j,e in enumerate(self.id):
                        if e[0]==i:
                            self.novelo[i]=0
                if i==self.j_:
                    self.novelo[i]=1
                else:
                    for j,e in enumerate(self.idbazis):
                        if e[0]==i:
                            self.novelo[i]=x_[j]
            return False
            
             
    def get_y(self):
        """
        A végén az y kiiratásához kiszámolja y értékét az aktuális bázishoz
        mj: Ez még nem szép (itt van lebegőpontos számolás is és utánna törté kerekítés), 
        de még Gaus eliminációval ezt nem írtam meg
        """
        val=np.array(self.list)
        l=[[j for j in val[:,i[0]]] for i in self.idbazis]
        l=np.transpose(l)
        l=l.astype('float64')
        A= np.matmul([self.c[i[0]] for i in self.idbazis],np.linalg.inv(l))
        return np.array([Fraction.from_float(x).limit_denominator(6**9)for x in A])
        
        
    def algoritmus(self, bazis):
        """
        Maga az algorimus, ami megfelelően hívja az osztály függvényeit
        """
        self.diag(bazis)
        while True:
            bol=self.y_vizsg()
            if bol==False:
                x=[None for _ in range(self.n)]
                for i,e in enumerate(self.idbazis):
                    x[e[0]]=self.table[i,-1]
                for i in self.id:
                    if i[0] != self.id[-1][0]:
                        x[i[0]]=0
                y=self.get_y()
                x=np.array(x)
                x_=", ".join([str(i) for i in x])
                y=", ".join([str(i) for i in y])
                print(f"Optimális x,y megoldáspár: \n x: {x_}\n y: {y}")
                print(f"És az optimum: {np.matmul(self.c,x)}")
                break
            
            bol=self.x_vizsg()
            if bol==False:
                novelo=", ".join([str(i) for i in self.novelo])
                print(f"A duál feladat nem megoldható. A primál nem korlátos.\n Növelő irány: {novelo}")
                break
            self.pivotalas(self.i,self.j)
            
    def algoritmus_id(self, bazis):
        """
        Maga az algorimus, ami megfelelően hívja az osztály függvényeit, csak kicsit módosítva arra az esetre,
        mikor van plusz id mátrix
        """
        self.diag(bazis)
        while True:
            bol=self.y_vizsg()
            if bol==False:
                x=[None for _ in range(self.n+self.m-1)]
                for i,e in enumerate(self.idbazis):
                    x[e[0]]=self.table[i,-1]
                for i in self.id:
                    if i[0] != self.id[-1][0]:
                        x[i[0]]=0
                optimum=np.matmul(self.c,x)
                if optimum !=0:
                    print(f"Nem oldható meg a primál feladat, mivel az egységmátrixszal kiegészített problémában a maximum: {str(optimum)}")
                    return False
                else:
                    return True
            bol=self.x_vizsg()
            if bol==False:
                print(f"Elromlott az algoritmus. Error. Ilyen nem lehet")
                break
            self.pivotalas(self.i,self.j)
            
    def get_bazis(self, bazis):
        """
        Az id utáni futtatáshoz ki kellhet egészíteni a bázist ftln oszlopokkal 
        """
        def test_indipendent(bazis,i):
            ind=copy.deepcopy(bazis)
            ind.append(i)
            arr=copy.deepcopy(np.array(self.list))
            l=np.array([[ arr[:,i] for i in ind]])
            l=np.transpose(l)
            return indipendency(l)
        i=0
        while len(bazis)<self.m-1:
           if i not in bazis:      
               if test_indipendent(bazis,i)==True:
                   bazis.append(i)
                   i+=1
               else: i+=1
           else: i+=1
           if i>self.n:
               return False
        return True
          
def indipendency(l):
    """
    Fv, ami eldönti, hogy egy listák listájának oszlopai lin ftlnek-e
    """
    count=0
    l=np.array(l)
    for i in range(len(l[0])):
            if l[count][i]==0:
                bol=False
                for c in range(count+1, len(l)):
                    if l[c][i]!=0:
                        slack=copy.deepcopy(l[count])
                        l[count]=copy.deepcopy(l[c])
                        l[c]=slack
                        bol=True
                        break
                    c+=1
                if bol==False:
                    return False
            if l[count,i]!=1:
                l[count]=l[count]*(1/l[count,i])
            for j in range(len(l)):
                if count!=j and l[j,i]!=0:
                    l[j]=l[j]-l[count]*l[j,i]
            count+=1
            if count>=len(l):
                break
    return True      
        
def szimp(filename):
    """
    Összerendezve az elvégzendő lépései az algoritmusnak, hogy csak file névvel hívható legyen
    """
    s=Szimplex(filename) 
    if s.n<s.m-1:
        print("Nincs megoldása a primál feladatnak")
        return 
    
    i=copy.deepcopy(s)  
    i.add_ident()        
    bol=i.algoritmus_id([i.n+j for j in range(i.m-1)])

    if bol==False:
        return
    else:
        bazis=list(filter(lambda x: x<s.n, i.idbazis[:][0]))
        if len(bazis)==s.m-1:
            s.algoritmus(bazis)
        else :
            bol=s.get_bazis(bazis)
            if bol==True:  
                s.algoritmus(bazis)
            else: return
           
szimp("file.txt")