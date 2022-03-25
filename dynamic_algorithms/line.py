"""
/=========================================================================================\
|Sklejanie odcinków                                                                       |
|                                                                                         |
|Dany jest ciag przedziałów postaci [ai, bi]. Dwa przedziały mozna                        |
|skleic jesli maja dokładnie jeden punkt wspólny. Prosze wskazac algorytmy dla            |
|nastepujacych problemów:                                                                 |
|1. Problem stwierdzenia, czy da sie uzyskac przedział [a, b] przez sklejanie odcinków.   |
|2. Zadanie jak wyzej, ale kazdy odcinek ma koszt i pytamy o minimalny koszt uzyskania    |
|odcinka [a, b].                                                                          |
|3. Problem stwierdzenia jaki najdłuzszy odcinek mozna uzyskac sklejajac                  |
|najwyzej k odcinków.                                                                     |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|najkrótsze połaczenie z punktu a do punktu b.Na początku dołacząjąc pojedyncze odcinki   |
|a następnie łaczać je w pary                                                             |
|W pierszym przypadku należy zmodyfikować algorytm na wartości Logiczne                   |
|A w trzecim przypadku podczas nadpisywania wartości pola należy wyliczać odległośc od    |
|a do puktu b tak aby była złożeniem do k-tych odcinków do wartości globalnej             |
|                                                                                         |
|Złożoność czasowa :O(n^3) Złożoność Pamięciowa O(n^3)                                    |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Tablica odcinków                   -minimalna liczba odcinków z a do b                 |
| -punkt początkowy                                                                       |
| -punkt końcowy                                                                          |
|                                                                                         |
\=========================================================================================/
"""

from math import inf
def line(Array,a,b):
	minimum=inf
	maximum=-inf
	for i in range(len(Array)):
		minimum=min(minimum,Array[i][0],Array[i][1])
		maximum=max(maximum,Array[i][0],Array[i][1])
	lenght=maximum-minimum
	Array.sort()
	F=[[inf for _ in range(lenght+1)]for _ in range(lenght+1)]
	for i in range(len(Array)):
		F[Array[i][0]-minimum][Array[i][1]-minimum]=1
	for i in range(lenght+1):
		for j in range(i+1,lenght+1):
			for k in range(i+1,j):
				F[i][j]=min(F[i][k]+F[k][j],F[i][j])
	return F[a-minimum][b-minimum]


#end
