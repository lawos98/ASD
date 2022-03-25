"""
/=========================================================================================\
|Algorytm sortowania przez wstawianie                                                     |
|                                                                                         |
|Polega na Wyciąganiu elementu i porówaniu z kolejnymi elementami zbioru posortowanego,   |
|póki nie napotkasz elementu równego lub elementu większego ,lub nie znajdziemy się       |
|na początku/końcu zbioru uporządkowanego.                                                |
|                                                                                         |
|Złożoność czasowa :O(n^2)           Złożoność Pamięciowa O(1)                            |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Operacje na wcześniej podanej Tablicy              |
|                                                                                         |
\=========================================================================================/
"""



def Insertion_sort(Array):
	n=len(Array)
	for i in range(1,n):
		index=i-1
		value=Array[i]
		while(index>=0 and Array[index]>value):
			Array[index+1]=Array[index]
			index-=1
		Array[index+1]=value


#end
