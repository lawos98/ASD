"""
/=========================================================================================\
|Znajdowanie najkrótszego przedziału z wszystkimi kolorami                                |
|                                                                                         |
|Dana jest tablica A zawierajaca n elementów, z których kazdy ma jeden z k kolorów.       |
|Prosze podac mozliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie,    |
|ze wsród elementów A[i],A[i + 1], . . . ,A[j] wystepuja wszystkie k kolorów oraz         |
|wartosc j − i jest minimalna (innymi słowy, szukamy najkrótszego przedziału z            |
|wszystkimi kolorami).                                                                    |
|                                                                                         |
|Algorytm opiera się na stworzeniu okna i rozszerzaniu w prawo jeżeli braukje nam         |
|kolorow i zmniejszaniu go przesuwajac lewy.Następnie zwracamy najkrótszą długość         |
|poprawnie skonstruowanego okna                                                           |
|                                                                                         |
|Złożoność czasowa :O(n)           Złożoność Pamięciowa O(k)                              |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -Szukana wartość                                    |
| -Liczba kolorów                                                                         |
|                                                                                         |
\=========================================================================================/
"""
def colors(Array,k):
	Array_color=[0 for _ in range(k)]
	left,right=0,1
	counter=1
	best_left=left
	best_lenght=len(Array)
	Array_color[Array[0]]=1
	while right<len(Array) and left<right:
		Array_color[Array[right]]+=1
		if Array_color[Array[right]]==1:
			counter+=1
		while counter==k:
			if right-left+1<best_lenght:
				best_lenght=right-left+1
				best_left=left
			Array_color[Array[left]]-=1
			left+=1
			if Array_color[Array[left-1]]==0:
				counter-=1
		right+=1
	return best_left,best_left+best_lenght-1


#end
