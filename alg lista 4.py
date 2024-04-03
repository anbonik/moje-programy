import math
import numpy as np
import gc
from time import perf_counter

def INSERTION_SORT(a):
    
    
    rozmiar= len(a)
    
    for j in range(1,rozmiar):
        key= a[j]
        i=j-1
        
        while i>-1 and a[i]>key:
            a[i+1]=a[i]
            i-=1
            
        a[i+1]=key
      
    return a

def BUCKETSORT(A,n):
    B= []
    a=len(A)
    for i in range(0,n):
        B.append([])

    for i in range(0,len(A)):
        B[math.floor((n)*A[i])].append(A[i])

    for i in range(0,n):
        INSERTION_SORT(B[i])

    C=[]

    for i in range(0,n):
        C+=B[i]

    return C

#A tablica którą sortujemy
#k przedział liczb który sortujemy
def COUNTINGSORT(A,k):
    C=np.zeros(k)
    B=np.zeros(len(A))

    for i in range(0,k):
        C[i]=0

    for i in range(0,len(A)):
        C[int(A[i])]+=1

    for i in range(1,k):
        C[i]+=C[i-1]

    for i in range(len(A)-1,-1,-1):
        print(int(C[int(A[i])])-1)
        B[int(C[int(A[i])])-1]=A[i]
        C[A[i]]-=1

    for i in range(0, len(A)):
    
        A[i]=B[i]

#A tablica którą sortujemy
# d podstawa systemu w ktorej zapisujemy 
#pozycja - pozycja w liczbie wedlug której sortujemu
#zakres liczby w tablicy do posortowania nie mogą być wieksze niz zakres
def COUNTING_SORT_dla_radix_sort(A,d,pozycja):
    C=np.zeros(d)
    B=np.zeros(len(A))

    for i in range(0,d):
        C[i]=0

    for i in range(0,len(A)):
        indeks=(A[i]//d**(pozycja-1))%d
        C[indeks]+=1

    for i in range(1,d):
        C[i]+=C[i-1]

    for i in range(len(A)-1,-1,-1):
        indeks=(A[i]//d**(pozycja-1))%d
        #print(int(C[int(A[i])])-1)
        B[int(C[indeks])-1]=A[i]
        C[indeks]-=1

    for i in range(0, len(A)):
    
        A[i]=B[i]


def RADIXSORT(A,d,zakres=(2**32 -1)):

    for i in range(1,int(math.log(zakres,d))):
        COUNTING_SORT_dla_radix_sort(A,d,i)

############################
#dodatkowe algorytmy do porównania
#heapsort
def heapify(A ,n, i):
    l=2*i +1
    r=2*i +2
    heap_size_A= n-1

    if l<=heap_size_A and A[l]>A[i]:
        largest=l
    else:
        largest=i

    if r<=heap_size_A and A[r]>A[largest]:
        largest=r

    if largest!=i:
        k=A[i]
        A[i]=A[largest]
        A[largest]=k

        heapify(A,n,largest)


def build_heap(A):
    heap_sizeA=len(A)

    for i in range(heap_sizeA//2 -1, -1, -1):
        
        heapify(A,heap_sizeA,i)


def HEAPSORT(A):
    build_heap(A)
    n=len(A)
    for i in range(len(A)-1, 0 ,-1):
        k=A[i]
        A[i]=A[0]
        A[0]=k
        n-=1
        heapify(A,n,0)
#################################
#quicksort
def quicksort(A,p,k):
    if p<k:
        q=partition(A,p,k)
        quicksort(A,p,q-1)
        quicksort(A,q+1,k)

def partition(A,p,k):
    x=A[k]
    i=p-1

    for j in range(p,k):
        
        if A[j]<=x:
            i+=1

            d=A[i]
            A[i]=A[j]
            A[j]=d

    d=A[i+1]
    A[i+1]=A[k]
    A[k]=d

    return i+1

def partition2(A,p,k):
    x=A[p]
    i=k+1

    for j in range(k,p,-1):
        
        if A[j]>=x:
            i-=1

            d=A[i]
            A[i]=A[j]
            A[j]=d

    d=A[i-1]
    A[i-1]=A[p]
    A[p]=d

    return i-1

def QUICKSORT(A):
    quicksort(A,0,len(A)-1)




###########################################
#               TESTY
######################################

#mierzenie czasu
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



#legenda test_radixsort
#legenda tablicy T zwracanej przez funkcję test
# T[a][b] jest dwu wymiarową tablicą
# indeksowi a są rzyporządkowane cyfry w jakich systemach liczbowych zostały zapisane liczby z tablicy
# indeksowi b jest przyporądkowana wielkosć danych na których były testowane funkcje w następujący sposób:
# odpowednie wartsci z tablicy n
def test_radixsort():
    x=1
    

    
    
    n=[10,100,10000,10000,100000,100000]
    d=[2,3,4,5,10,15,30,60,200,600,1000]

    T=np.zeros((len(d),len(n)))

    for i in range(0,len(d)):
        for j in range(0,len(n)):
           
            


            A = np.random.randint(low=0, high=(2**30 -3), size=(n[j],))
            print("i j")
            print(i)
            print(j)
            print("acacacacacacacac")
            T[i][j]=zmierz_raz(lambda: RADIXSORT(A,d[i]))
            print("cccccccccccccccc")

            print("wykonano "+ str(x)+ " operacji z "+ str(len(d)*len(n)))
            x+=1

    
    return T

#legenda test_radixsort
#legenda tablicy T zwracanej przez funkcję test
# T[a][b] jest dwu wymiarową tablicą
# odpowednie wartsci z tablicy f
# indeksowi a są numery testowanych funkcji
# indeksowi b jest przyporądkowana wielkosć danych na których były testowane funkcje w następujący sposób:
# odpowednie wartsci z tablicy n
def test_bucketsort():
    x=1
    

    f=[BUCKETSORT,INSERTION_SORT,QUICKSORT,HEAPSORT]
    
    n=[10,50,100,500,2000,5000,10000,]

    T=np.zeros((len(f),len(n)))

    for i in range(1,4):
        for j in range(0,len(n)):
            


            A = np.random.uniform(low=0, high=0.999999999999999999999, size=(n[j],))
            print("acacacacacacacac")
            T[i][j]=zmierz_raz(lambda: f[i](A))
            print("cccccccccccccccc")

            print("wykonano "+ str(x)+ " operacji z "+ str((len(f)-1)*len(n)))
            x+=1

    for j in range(0,len(n)):
            


            A = np.random.uniform(low=0, high=0.999999999999999999999, size=(n[j],))
            print("acacacacacacacac")
            T[0][j]=zmierz_raz(lambda: BUCKETSORT(A,100))
            print("cccccccccccccccc")

            print("wykonano "+ str(x)+ " operacji z "+ str(len(n)))
            x+=1

    
    return T





###############################
###############################
#################################

AA=np.array((3,2,5,4,8,2,2,3,7,5,8,9,5,7,0))
BB=np.array((3486,4356,23857,2342347,2346,))

#RADIXSORT(BB,45,100000000)
#A=[0.432,0,0.5435,0.432,0.00123,0.999999]
#C=BUCKET_SORT(A,10)
#print(C)

#print(BB)


#porównuje bucket sort z innymi algorytmami
print(test_bucketsort())


#porównuje czas działania tego algorytmu w zależności od podstawy w której jest zapisana liczba
print(test_radixsort())


    



