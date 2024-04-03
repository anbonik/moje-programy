

import numpy as np
import gc
from time import perf_counter
from itertools import repeat


def INSERTION_SORT(a):
    
    
    rozmiar= a.shape[0]
    
    for j in range(1,rozmiar):
        key= a[j]
        i=j-1
        
        while i>-1 and a[i]>key:
            a[i+1]=a[i]
            i-=1
            
        a[i+1]=key
      
    return a

def INSERTION_SORT_PLUS(a):
    przypisania=0
    porownania=0
    
    rozmiar= a.shape[0]
    
    for j in range(1,rozmiar):
        key= a[j]
        przypisania+=1
        i=j-1
        
        while i>-1 and a[i]>key:
            porownania+=1
            a[i+1]=a[i]
            przypisania+=1
            i-=1
        if i>-1:    
            porownania+=1
            
        a[i+1]=key
        przypisania+=1
        
    return np.array([porownania, przypisania])


def BUBBLE_SORT(a):
    
    rozmiar= a.shape[0]
    
    for i in range(rozmiar): 
        for j in range(rozmiar - i -1):
            if a[j]>a[j+1]:
        
                pom=a[j]
                a[j]=a[j+1]
                a[j+1]=pom
    return a

def BUBBLE_SORT_PLUS(a):
    
    przypisania=0
    porownania=0
    rozmiar= a.shape[0]
    
    for i in range(rozmiar):
        for j in range(rozmiar - i -1):
            porownania+=1
            if a[j]>a[j+1]:        
                pom=a[j]
                przypisania+=1
                a[j]=a[j+1]
                przypisania+=1
                a[j+1]=pom
                przypisania+=1
        
    return np.array([porownania, przypisania])


def MERGE(A, p, s, k):
    n1 = s - p + 1
    n2 = k - s
    n1=int(n1)
    n2=int(n2)
    m=int(s)
    p=int(p)
    k=int(k)


    L = np.zeros(n1)
    R = np.zeros(n2)


    for i in range(0, n1):
        L[i] = A[p + i]

    for j in range(0, n2):
        R[j] = A[m + 1 + j]


    i = 0
    j = 0
    x = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[x] = L[i]
            i += 1
        else:
            A[x] = R[j]
            j += 1
        x += 1


    while i < n1:
        A[x] = L[i]
        i += 1
        x += 1


    while j < n2:
        A[x] = R[j]
        j += 1
        x += 1





def MERGE_SORT(A):
    
    n=A.shape[0]
    MERGE_SORT2(A,0,n-1)

def MERGE_SORT2(A,p,k):
    if p<k:
        s= np.floor((p+k)/2)
        MERGE_SORT2(A,p,s)
        MERGE_SORT2(A,s+1,k)
        MERGE(A,p,s,k)



# D[0] jest liczbą porównań, a D[1] jest liczbą przypisań
def MERGE_SORT_PLUS(A):
     D=np.zeros(2)
     n=A.shape[0]
     D[1]+=1
     MERGE_SORT2_PLUS(D,A,0,n-1)
     return D

def MERGE_SORT2_PLUS(D,A,p,k):
    if p<k:
        D[0]+=1
        s= np.floor((p+k)/2)
        D[1]+=1
        MERGE_SORT2_PLUS(D,A,p,s)
        MERGE_SORT2_PLUS(D,A,s+1,k)
        MERGE_PLUS(D,A,p,s,k)

def MERGE_PLUS(D,A, p, s, k):
    n1 = s - p + 1
    D[1]+=1
    n2 = k - s
    D[1]+=1
    n1=int(n1)
    n2=int(n2)
    m=int(s)
    p=int(p)
    k=int(k)


    L = np.zeros(n1)
    D[1]+=1
    R = np.zeros(n2)
    D[1]+=1


    for i in range(0, n1):
        L[i] = A[p + i]
        D[1]+=1

    for j in range(0, n2):
        R[j] = A[m + 1 + j]
        D[1]+=1

	
    i = 0
    D[1]+=1	 
    j = 0
    D[1]+=1	 
    x = p
    D[1]+=1	 

    while i < n1 and j < n2:
        D[0]+=3


        if L[i] <= R[j]:
            A[x] = L[i]
            D[1]+=1
            D[1]+=1
            i += 1
        else:
            A[x] = R[j]
            j += 1
            D[1]+=1
            D[1]+=1
        x += 1
        D[1]+=1

    if i < n1:
        D[0]+=2
    else:
        D[0]+=1
        
        
            
        

    while i < n1:
        A[x] = L[i]
        i += 1
        x += 1
        D[0]+=1
        D[1]+=3

    D[0]+=1


    while j < n2:
        A[x] = R[j]
        j += 1
        x += 1
        D[0]+=1
        D[1]+=3

    D[0]+=1


def MERGE_SORT21(A):
    
    n=A.shape[0]
    MERGE_SORT221(A,0,n-1)

def MERGE_SORT221(A,p,k):
    if p<k and (k-p)>4:
        s=p+ np.floor((k-p)*(2/3))
        MERGE_SORT221(A,p,s)
        MERGE_SORT221(A,s+1,k)
        MERGE(A,p,s,k)
    elif p<k:
        k=int(k)
        p=int(p)
        B=np.ones(k-p+1)
        for i in range(0,k-p+1):
            B[i]=A[i+p]
        BUBBLE_SORT(B)
        for i in range(0,k-p+1):
            A[i+p]=B[i]




# D[0] jest liczbą porównań, a D[1] jest liczbą przypisań
def MERGE_SORT_PLUS21(A):
     D=np.zeros(2)
     n=A.shape[0]
     D[1]+=1
     MERGE_SORT2_PLUS21(D,A,0,n-1)
     return D

def MERGE_SORT2_PLUS21(D,A,p,k):
    
    if p<k and (k-p)>4:
        D[0]+=1
        s=p+ np.floor((k-p)*(2/3))
        D[1]+=1
        MERGE_SORT2_PLUS21(D,A,p,s)
        MERGE_SORT2_PLUS21(D,A,s+1,k)
        MERGE_PLUS(D,A,p,s,k)
    elif p<k:
        k=int(k)
        p=int(p)
        B=np.ones(k-p+1)
        for i in range(0,k-p+1):
            B[i]=A[i+p]
        x=BUBBLE_SORT_PLUS(B)
        D[0]+=x[0]
        D[1]+=x[1]
        for i in range(0,k-p+1):
            A[i+p]=B[i]


def zmierz_raz(f, min_time=0.01):
    suma_czasu = 0
    ile_razy = 0
    ile_teraz = 1
    stan_gc = gc.isenabled()
    gc.disable()
    while suma_czasu < min_time:
        if ile_teraz == 1:
            start = perf_counter()
            f()
            stop = perf_counter()
        else:
            iterator = repeat(None, ile_teraz)
            start = perf_counter()
            for _ in iterator:
                f()
            stop = perf_counter()
        suma_czasu += stop-start
        ile_razy += ile_teraz
        ile_teraz = 9*ile_razy
    if stan_gc:
        gc.enable()
    return suma_czasu/ile_razy



def funkcja(x):

    return x*x

#legenda tablicy T zwracanej przez funkcję test
# T[a][b][c] jest trzy wymiarową tablicą
# indeksowi a są przyporządkowane funkcje w następujący sposób:
# 0=INSERTION_SORT, 1=BUBBLE_SORT,2=MERGE_SORT, 3=MERGE_SORT21
# indeksowi b jest przyporądkowana wielkosć danych na których były testowane funkcje w następujący sposób:
# 0=10,1=50,2=100,3=500,4=1000,5=5000,6=10000
# indeksowi c są przyporządkowane własności testowanych algorytmów w następujący sposób:
# 0= liczba porównań, 1= liczba przypisań, 2=czas działania


def test():
    x=1
    T=np.zeros((4,7,3))

    f=[INSERTION_SORT, BUBBLE_SORT,MERGE_SORT, MERGE_SORT21]
    f_plus=[INSERTION_SORT_PLUS, BUBBLE_SORT_PLUS,MERGE_SORT_PLUS, MERGE_SORT_PLUS21]
    n=[10,50,100,500,1000,5000,10000]

    for i in range(0,4):
        for j in range(0,7):

            A = np.random.uniform(low=-1000, high=1000, size=(n[j],))
            p=f_plus[i](A)
            T[i][j][0]=p[0]
            T[i][j][1]=p[1]


            A = np.random.uniform(low=-1000, high=1001, size=(n[j],))
            T[i][j][2]=zmierz_raz(lambda: f[i](A))

            print("wykonano "+ str(x)+ " operacji z "+ str(4*7))
            x+=1

    
    return T





#a=zmierz_raz(lambda: funkcja(100))
#print(a)        
#x= np.array([4,3,84,3,765,67,22,444,4443,4,2,32542,6,4,8,-8])  
#y= np.array([5345,765,3450,43424,0,54545432,2,6,6,5,7])
#sampl = np.random.uniform(low=-1000, high=1000, size=(2000,))
#print(INSERTION_SORT(x))
#print(INSERTION_SORT_PLUS(x))
#dlaczego jak dam ten sam x w bubble sort normalnym i plus to plus sie nie wlacza
#print(BUBBLE_SORT(x))
#print(BUBBLE_SORT_PLUS(y))
#print(MERGE_SORT21(sampl))
#print(sampl)
#print(zmierz_raz(lambda: MERGE_SORT(y)))
#print(y)

print(test())
    
    
    

