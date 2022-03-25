"""
/=========================================================================================\
|Sortowanie pozycyjne                                                                     |
|                                                                                         |
|Algorytm sortowania porządkujący stabilnie ciągi wartości (liczb, słów) względem         |
|konkretnych cyfr, znaków itp, kolejno od najmniej znaczących do najbardziej              |
|znaczących pozycji                                                                       |
|W skrócie jest to counting sort po każdej pozycji w kluczach                             |
|                                                                                         |
|Złożoność czasowa :O(d(n+k))             Złożoność Pamięciowa O(n+k)                     |
|Gdzie d-liczba cyft w kluczu ,k-liczba róźnych cyft                                      |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Tablica                                            |
| -system liczbowy                                                                        |
\=========================================================================================/
"""

def sort_by_digit(A,system,digit_number):
    def get_number(value,system,digit_number):
        for _ in range(digit_number):
            value//=system
        return value%system

    Array_count=[0] * system
    for value in A:
        Array_count[get_number(value,system,digit_number)] += 1
    for i in range(1, system):
        Array_count[i] += Array_count[i - 1]

    Resualt=[0]*len(A)
    for index in range(len(A)-1,-1,-1):
        value=get_number(A[index],system,digit_number)
        Array_count[value] -= 1
        Resualt[Array_count[value]] = A[index]

    return Resualt

def radix_sort(A,system):
    maksimum_value=max(A)
    digits=0
    while maksimum_value>0:
        digits+=1
        maksimum_value//=system
    for i in range(digits):
        A=sort_by_digit(A,system,i)
    return A


#end
