"""
/=========================================================================================\
|Sortowanie wartości ze zbioru Log(n)                                                     |
|                                                                                         |
|Dana jest tablica A o długosci n. Wartosci w tablicy pochodza ze zbioru B, gdzie         |
|SBS = log n. Prosze zaproponowac mozliwie jak najszybszy algorytm sortowania tablicy A.  |
|                                                                                         |
|Algorytm opiera się znajdowaniu unikalnych wartości i dodawaniu ich do tablicy           |
|zliczającej z wyszukiwaniem binarnym odpowiednich wartości.Następnie sortujemy przez     |
|zliczanie wyszukując odpowiedniego pojemnika też wyszukiwaniem binarnym                  |
|                                                                                         |
|Złożoność czasowa :O(n)           Złożoność Pamięciowa O(n)                              |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Tablica                                            |
|                                                                                         |
\=========================================================================================/
"""


def ad d_one(Numbers, Count, left, right, value):
    pivot=left+(right-left)//2
    if Numbers[pivot]==value:
        Count[pivot]+=1
        return
    if left==right:
        Numbers+=[value]
        Count+=[1]
        index= len(Numbers) - 1
        while Numbers[index]<Numbers[index - 1] and index>0:
            Numbers[index - 1], Numbers[index]= Numbers[index], Numbers[index - 1]
            Count[index-1],Count[index]=Count[index],Count[index-1]
            index-=1
        return
    if Numbers[pivot]<value:
        add_one(Numbers, Count, pivot + 1, right, value)
    else:
        add_one(Numbers, Count, left, pivot - 1, value)

def binary_select(Array,left,right,value):
    pivot=left+(right-left)//2
    if Array[pivot]==value:
        return pivot
    if Array[pivot]<value:
        return binary_select(Array, pivot + 1, right, value)
    else:
        return binary_select(Array, left, pivot - 1, value)

def countsort(Array,Count,Numbers):
    n=len(Numbers)
    output=[0]*len(Array)
    for i in range(1,n):
        Count[i]+=Count[i-1]
    for i in range(len(Array)-1,-1,-1):
        x=binary_select(Numbers,0,len(Numbers)-1,Array[i])
        output[Count[x]-1]=Array[i]
        Count[x]-=1
    for i in range(len(Array)):
        Array[i]=output[i]

def sort(Array):
    Count=[1]
    Numbers=[Array[0]]
    for i in range(1,len(Array)):
        add_one(Numbers,Count,0,len(Numbers)-1,Array[i])
    countsort(Array,Count,Numbers)


#end
