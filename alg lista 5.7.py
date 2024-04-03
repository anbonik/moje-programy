import numpy as np
import gc
from time import perf_counter


# Juz dla n=24 działanie tego algorytmu zaczyna długo trwać

def naive_cut_rod(p,n):
    if n==0:
        return 0
    

    
    #zakladam ze cena za kawalek prenta nie moze byc ujemna
    q=-999999999999999999999999999

    for i in range(1,n+1):
        naive_cut_dla_mniejszych_kawalkow =p[i-1] + naive_cut_rod(p,(n-i))
        if q<( naive_cut_dla_mniejszych_kawalkow):
            q=naive_cut_dla_mniejszych_kawalkow

    return q



# n- dlugosc listy z cenami kawalkow prenta
def generowanie_cen(n):
    A = np.random.randint(low=1, high=50, size=(int(n+1)))

    for i in range(0,int(n+1)):
        A[i]+=A[i-1]
    #print(A)
    return A

def print_solution_memorized_cut_rod(p,n):
    r,s= memorized_cut_rod(p,n)
    
    

    while n>0:
        print(s[int(n)])
        n=n-s[int(n)]



def memorized_cut_rod(p,n):
    r=np.zeros(n+1)
    s=np.zeros(n+1)
    r[0]=0


    for i in range(1,n+1):
        r[i]=-9999999999999999999999999

    cut_rod_aux(p,r,n,s)
    return r,s

def cut_rod_aux(p,r,n,s):
    
    if n==0:
        return 0
    #if n==1:
     #   r[1]=p[0]
      #  return p[0]
        
    
    if r[n]>=0:
        return r[n]
    
    q=-9999999999999999999999999

    for i in range(1,n+1):
        memorized_cut_dla_mniejszych_kawalkow =p[i-1] + cut_rod_aux(p,r,n-i,s)
        if q<( memorized_cut_dla_mniejszych_kawalkow):
            q=memorized_cut_dla_mniejszych_kawalkow
            s[n]=i

    r[n]=q
    return q




def iteracyjny_cut_rod(p,n):
    r=np.zeros(n+1)
    s=np.zeros(n+1)
    r[0]=0

    for j in range(1,n+1):
        q=-99999999999999
        for i in range(1,j+1):
            if q<(p[i-1] + r[j-i]):
                q=p[i-1] + r[j-i]
                s[j]=i

        r[j]=q

    return r,s

def print_solution_iteracyjne_cut_rod(p,n):
    r,s= iteracyjny_cut_rod(p,n)
    
    

    while n>0:
        print(s[int(n)])
        n=n-s[int(n)]


#n rozmiar tablicy
#k zakres liczb zanajdujacych sie w tablicy
#generuje tablice dla algorytmow LCS
def generowanie_tablic_XY(n,k):
    A = np.random.randint(low=1, high=(k+1), size=n)
    return A
#X Y tablice w których szukamy najdłuższego podciągu
# i okresla indeksy elementów w tablicy X
# j okresla indeksy elementów w tablicy Y
def naiwny_LCS(X,Y):
    return naiwny_LCS_2(X,Y,len(X)-1,len(Y)-1)

def naiwny_LCS_2(X,Y,i,j):

    
    if X[i]==Y[j]:
        #licznik+=1
        if i==0 or j==0:
            return 1
        else:
            return  1 + naiwny_LCS_2(X,Y,i-1,j-1)
    else:
        if i==0 and j==0:
            return 0
        
        elif i==0 and j>0:
            return naiwny_LCS_2(X,Y,i,j-1)
        
        elif i>0 and j==0:
            return  naiwny_LCS_2(X,Y,i-1,j)
        
        else:
            a= naiwny_LCS_2(X,Y,i-1,j)
            b= naiwny_LCS_2(X,Y,i,j-1)

            if a<b:
                return b
            else:
                return a


# rekurencyjny lcs z pamietaniem

def memorised_LCS(X,Y):
    n=len(X)
    m=len(Y)
    r=np.zeros((n,m))
    for i in range(0,n):
        for j in range(0,m):
            r[i][j]=-3

    return memorised_LCS_2(X,Y,n-1,m-1,r)

def memorised_LCS_2(X,Y,i,j,r):
    #print(r)

    if r[i][j]>=0:
        return r[i][j]

    elif X[i]==Y[j]:
        #licznik+=1
        if i==0 or j==0:
            r[i][j]=1
            return 1
        else:
            r[i][j]=1 + memorised_LCS_2(X,Y,i-1,j-1,r)
            return  r[i][j]
    else:
        if i==0 and j==0:
            r[i][j]=0
            return  r[i][j]
        
        elif i==0 and j>0:
            r[i][j]= memorised_LCS_2(X,Y,i,j-1,r)
            return  r[i][j]
        
        elif i>0 and j==0:
            r[i][j]=  memorised_LCS_2(X,Y,i-1,j,r)
            return  r[i][j]
        
        else:
            a= memorised_LCS_2(X,Y,i-1,j,r)
            b= memorised_LCS_2(X,Y,i,j-1,r)

            if a<b:
                r[i][j]= b
                return  r[i][j]
            else:
                r[i][j]= a
                return  r[i][j]

#legenda tablicy b:
#wartosc 1 oznacza strzalke skierowana w lewa strone <--
#wartosc 2 oznacza strzalke skierowana na ukos w gore lewo strone ^
#                                                                  \
#wartosc 3 oznacza strzalke skierowana w gore  ^
#                                              |

def iteracyjny_LCS(X,Y):
    n=len(X)
    m=len(Y)
    c=np.ones((n+1,m+1))
    b=np.ones((n+1,m+1))

    for i in range(0,n+1):
        c[i][0]=0

    for j in range(0,m+1):
        c[0][j]=0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1] +1
                b[i][j]=2
            elif c[i-1][j]<=c[i][j-1]:
                c[i][j]=c[i][j-1]
                b[i][j]=1
            else:
                c[i][j]=c[i-1][j]
                b[i][j]=3

    return b,c

def print_solution_iteracyjny_LCS(X,Y):
    A=[]

    n=len(X)
    m=len(Y)

    b,c=iteracyjny_LCS(X,Y)
    
    i=n
    j=m

    while i>0 and j>0:
        
        if b[i][j]==2:
            A.append(X[i-1])
            i-=1
            j-=1
        elif b[i][j]==1:
            j-=1

        else:
            i-=1

    lenA=len(A)
    B=np.zeros(lenA)

    for i in range(0,lenA):
        B[i]=A[lenA-i-1]

    return B

#testy czasu działania róznych algorytmow lcs

def zmierz_raz(f, min_time=0.01):
    suma_czasu = 0
    ile_razy = 0
    ile_teraz = 1
    stan_gc = gc.isenabled()
    gc.disable()
    
    start = perf_counter()
    f()
    stop = perf_counter()
        
        
    return stop-start
#legenda tablicy T
#T[a][b]
# a odpowiada numerowi testowanej funkcji z tablicy f
#b odpowiada wielkosci danych  zapisanych w tablicy n i wynosi n[b]
# naive_cut_rod nie testowałam tego algorytmu (bo jest zbyt wolny)dla wszystkich wielkosci danych
# dlatego w tablicy T od pewnego miejsca sa przypisane zera do niego
def test_algorytmow_cut_rod():

    x=0
    

    f=[naive_cut_rod,memorized_cut_rod,iteracyjny_cut_rod]
    
    n=[4,8,16,24,19,25,50,100,]

    T=np.zeros((len(f),len(n)))

    for j in range(0,4):
            #print("i")
            #print(i)
            #print("j")
            #print(j)
            #print("aaaaaaaaaaaaaaaaaaaaa")

            
            


            p=generowanie_cen(n[j]*(np.floor(1.2)))
            #print("acacacacacacacac")
            T[0][j]=zmierz_raz(lambda: f[0](p,n[j]))
            #print("cccccccccccccccc")
            x+=1

            print("wykonano "+ str(x)+ " operacji z "+ str(4+2*len(n)))
            

    for i in range(1,len(f)):
        for j in range(0,len(n)):
            #print("i")
            #print(i)
            #print("j")
            #print(j)
            #print("aaaaaaaaaaaaaaaaaaaaa")

            
            


            p=generowanie_cen(n[j]*(np.floor(1.2)))
            #print("acacacacacacacac")
            T[i][j]=zmierz_raz(lambda: f[i](p,n[j]))
            #print("cccccccccccccccc")
            x+=1

            print("wykonano "+ str(x)+ " operacji z "+ str(4+2*len(n)))
            

    
    return T






#B=[ 13,  71,  83 ,120 ,140, 188 ,215 ,243 ,289 ,294]
x=9
#B=generowanie_cen(x+3)
#print(naive_cut_rod(B,x))
#print(memorized_cut_rod(B,x))
#print(iteracyjny_cut_rod(B,x))
#print("yyyyyyyyyyyyyy")
#print(print_solution_iteracyjne_cut_rod(B,x))
#print("kkkkkkkkkkkkkkkk")
#print(print_solution_memorized_cut_rod(B,x))
X=generowanie_tablic_XY(20,10)
Y=generowanie_tablic_XY(20,10)
#print(naiwny_LCS(X,Y))
#print(memorised_LCS(X,Y))
#print("uuuuuuuuuuu")
#print(iteracyjny_LCS(X,Y))
#print("tttttttt")
#print(print_solution_iteracyjny_LCS(X,Y))
print(test_algorytmow_cut_rod())
