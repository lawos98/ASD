"""
/=========================================================================================\
|Znajdowanie elementu dominującego                                                        |
|                                                                                         |
|Mamy dana tablice A z n liczbami. Prosze zaproponowac algorytm o złozonosci              |
|O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która wystepuje w A na      |
|ponad połowie pozycji.                                                                   |
|                                                                                         |
|Przechodzimy po tablicy zliczając wystąpienia aktualniej wartości, w przeciwym wypadku   |
|znajdując inną wartość zmiejaszamy nasz licznik.W przypadku wyzerowania się licznika     |
|zmieniamy aktualna wartość.Następnie przechodzimy jeszcze raz po tablicy i sprawdzamy    |
|czy nasza wartość wystepuje ponad połowę pozycji                                         |
|                                                                                         |
|Złożoność czasowa :O(n)           Złożoność Pamięciowa O(1)                              |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica                            -lider                                              |
|                                                                                         |
\=========================================================================================/
"""


def leader(Array):
	n=len(Array)
	counter=1
	number=Array[0]
	for i in range(1,n):
		if number==Array[i]:
			counter+=1
		else:
			counter-=1
			if counter==0:
				number=Array[i]
				counter=1
	counter=0
	for i in range(n):
		if Array[i]==number:
			counter+=1
	if counter>n//2:
		return number
	return False


#end
