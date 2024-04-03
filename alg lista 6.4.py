import numpy as np
import gc
from time import perf_counter
from itertools import repeat

#w algorytmach przydziału zajęć ustaliłam że tablice w których są zapisane zajecia są postaci s[1...k], f[1...k]
#dlatego wartosci s[0], f[0] będą ignorowane i nie będą brane pod uwagę przy przydziale zajęć
# dlatego należy wpisywać dane do tablic s, f zaczynając od indeksu 1

def quicksort(s,f,p,k):
    if p<k:
        q=partition(s,f,p,k)
        quicksort(s,f,p,q-1)
        quicksort(s,f,q+1,k)

def partition(s,f,p,k):
    x=f[k]
    i=p-1

    for j in range(p,k):
        
        if f[j]<=x:
            i+=1

            d=f[i]
            f[i]=f[j]
            f[j]=d

            d=s[i]
            s[i]=s[j]
            s[j]=d

    d=f[i+1]
    f[i+1]=f[k]
    f[k]=d

    d=s[i+1]
    s[i+1]=s[k]
    s[k]=d

    return i+1



#w algorytmach przydziału zajęć ustaliłam że tablice w których są zapisane zajecia są postaci s[1...k], f[1...k]
#dlatego wartosci s[0], f[0] będą ignorowane i nie będą brane pod uwagę przy przydziale zajęć
# dlatego należy wpisywać dane do tablic s, f zaczynając od indeksu 1

def generator_danych_dla_przydzialu_zajec(n):
    #tworzenie tablic s,t
    #wartosci s[0], t[0] beda ignorowane w dalszym działaniu algorytmu
    s=np.random.random_sample((n+1,))*(19-7) + 7
    t=np.random.random_sample((n+1,))*4 + 0.2
    f=s+t

    #sortowanie wzgledem tablicy
    quicksort(s,f,1,len(f)-1)


    return s,f



# ta funkcja zwraca numery zajęć(odpowiadające czasom z tablic s,t), 
def dynamiczny_przydzial_zajec(s,f):
    licznik=np.ones((len(f)+1,len(f)+1))*(-1)
    wyniki=[]

    # Tworze tablice s2, f2 by zapisac w nich sztuczne ograniczenia
    s2=np.zeros(len(f)+1)
    f2=np.zeros(len(f)+1)

    #sztuczne wartosci po za zakresem
    s2[0]=-9999999999999
    f2[0]=-9999999999999

    s2[len(f)]=999999999999999999
    f2[len(f)]=999999999999999999

    for i in range(1,len(f)):
        s2[i]=s[i]

    for i in range(1,len(f)):
        f2[i]=f[i]

    max_dynamiczny(s2,f2,0,len(f),licznik,wyniki)
    #print(licznik)

    wyniki=[]
    znajdowanie_numerow_zajec(0,len(f),licznik,wyniki)

    return wyniki

def max_dynamiczny(s,f,i,j,licznik,wyniki):
    a=-9999999999

    if licznik[i][j]>=0:
        return licznik[i][j]
    
    else:
        max=0

        for k in range(i+1,j):
            if s[k]>=f[i] and f[k]<=s[j]:
                nowy_max1=max_dynamiczny(s,f,i,k,licznik,wyniki)
                nowy_max2=max_dynamiczny(s,f,k,j,licznik,wyniki)
                nowy_max=nowy_max1+1+nowy_max2

                if nowy_max>max:
                    max=nowy_max
                    
                        

        licznik[i][j]=max
        return max
        
def znajdowanie_numerow_zajec(i,j,licznik,wynik):
    x=licznik[i][j]
    

    warunek=1
    if licznik[i][j]<=0:
        warunek=0

    k=i+1
    while warunek==1 and k<j:
        if (licznik[i][k] + 1 + licznik[k][j])==x and licznik[i][k]>=0 and  licznik[k][j]>=0:
            wynik.append(k)
            warunek=0
            znajdowanie_numerow_zajec(i,k,licznik,wynik)
            znajdowanie_numerow_zajec(k,j,licznik,wynik)
        else:
            k+=1
#w algorytmach przydziału zajęć ustaliłam że tablice w których są zapisane zajecia są postaci s[1...k], f[1...k]
#dlatego wartosci s[0], f[0] będą ignorowane i nie będą brane pod uwagę przy przydziale zajęć
# dlatego należy wpisywać dane do tablic s, f zaczynając od indeksu 1
def RECURSIVE_ACTIVITY_SELECTOR(s,f):
    f[0]=0
    return recursive_activity_selector(s,f,0)

def recursive_activity_selector(s,f,k):
    m=k+1
    while m<=len(f)-1 and s[m]<=f[k]:
        m+=1
    
    if m<= len(f)-1:
        return [m]+recursive_activity_selector(s,f,m)
    else:
        return []

#w algorytmach przydziału zajęć ustaliłam że tablice w których są zapisane zajecia są postaci s[1...k], f[1...k]
#dlatego wartosci s[0], f[0] będą ignorowane i nie będą brane pod uwagę przy przydziale zajęć
# dlatego należy wpisywać dane do tablic s, f zaczynając od indeksu 1
def ACTIVITY_SELECTOR(s,f):
    A=[1]
    m=1
    for k in range(2,len(f)):
        if s[k]>=f[m]:
            A.append(k)
            m=k

    return A

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

def test_algorytmow_przydzial_zajec():
    funkcje=[dynamiczny_przydzial_zajec,RECURSIVE_ACTIVITY_SELECTOR,ACTIVITY_SELECTOR]
    n=[5,10,50,100,500,1000]
    x=1

    T=np.zeros((len(funkcje),len(n)))

    for i in range(0,len(funkcje)):
        for j in range(0,len(n)):

            s,f=generator_danych_dla_przydzialu_zajec(n[j])



            
            T[i][j]=zmierz_raz(lambda: funkcje[i](s,f))
            print("cccccccccccccccc")

            print("wykonano "+ str(x)+ " operacji z "+ str(len(funkcje*len(n))))
            x+=1

    
    return T




def DYNAMIC_COIN_CHANGING(sum, nominaly):
    #tablica pot_sumy służy do zapisywania rozwiazan mniejszych sum
    pot_sumy=np.ones(sum+1)*(-1)
    pot_sumy[0]=0
    return dynamic_coin_change(sum,nominaly,pot_sumy)


# ilosc - ilosc monet ktore zwracamy jako reszta
def dynamic_coin_change(sum,nominaly,pot_sumy):

    if pot_sumy[sum]>=0:
        return pot_sumy[sum]
    
    else:


        #sztuczne górne ograniczenie min
        min=9999999999999999999999999999999999999999999999
        nowe_min=0
        
        
        

        for i in range(0,len(nominaly)):
            if nominaly[i]<=sum:

                nowe_min=1+ dynamic_coin_change(sum-nominaly[i],nominaly,pot_sumy)

                if nowe_min<min:
                    min=nowe_min

        pot_sumy[sum]=min
        return min


def COIN_CHANGING(sum,nominaly):

    licznik=0

    for i in range(len(nominaly)-1,-1,-1):
        while sum>=nominaly[i]:
            sum-=nominaly[i]
            licznik+=1

    return licznik


#odp na pytanie dla jakich nominałow i sumy zachłanny algorytm nie zwraca optymalnego wyniku:
# dla sum=10 i nominaly=[1,2,3,5,6] nie zwraca on optymalnego wyniku
def test_wydawanie_reszty():
    warunek=1
    # A jest tablica z nominałami
    A=[1,0,0,0,0]
    sum=0
    a=1
    b=1
    c=1
    d=1

    x=1

    while warunek==1 and a<=30:
    
        A[1]=A[0]+a

        b=1
        while warunek==1 and b<=30:
        
            A[2]=A[1]+b

            c=1
            while warunek==1 and c<=30:
            
                A[3]=A[2]+c

                d=1

                while warunek==1 and d<=30:
                
                    A[4]=A[3]+d

                    sum=1

                    while warunek==1 and sum<=200:
                        dynamiczne=DYNAMIC_COIN_CHANGING(sum,A)
                        zachlanne=COIN_CHANGING(sum,A)
                        print(dynamiczne)
                        print(zachlanne)
                        print(sum)
                        print(A)

                        if dynamiczne!=zachlanne:
                            warunek=0
                            print("Udalo sie")

                        else:
                            sum+=1

                        print("wykonano "+ str(x)+ " operacji z "+ str((13**4)*153))
                        x+=1

                    d+=1

                c+=1

            b+=1

        a+=1

    return sum,A

#w algorytmach przydziału zajęć ustaliłam że tablice w których są zapisane zajecia są postaci s[1...k], f[1...k]
#dlatego wartosci s[0], f[0] będą ignorowane i nie będą brane pod uwagę przy przydziale zajęć
# dlatego należy wpisywać dane do tablic s, f zaczynając od indeksu 1

#print(generator_danych_dla_przydzialu_zajec(80))
s,f=generator_danych_dla_przydzialu_zajec(20)
#print(s)
#print(f)
print(dynamiczny_przydzial_zajec(s,f))
print(RECURSIVE_ACTIVITY_SELECTOR(s,f))
print(ACTIVITY_SELECTOR(s,f))
print(test_algorytmow_przydzial_zajec())

print(DYNAMIC_COIN_CHANGING(10,[1,2,3,5,6]))
print(COIN_CHANGING(10,[1,2,3,5,6]))
#print(test_wydawanie_reszty())


