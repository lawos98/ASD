"""
/=========================================================================================\
|Sprawdzanie Anagramu                                                                     |
|                                                                                         |
|Prosze zaproponowac algorytm, który majac dane dwa słowa A i B o długosci n, kazde nad   |
|alfabetem długosci k, sprawdza czy A i B sa swoimi anagramami.                           |
|Prosze zaproponowac rozwiazanie działajace w czasie O(n) (prosze zwrócic uwage, ze       |
|k moze byc duzo wieksze od n—np. dla alfabetu unicode; złozonosc pamieciowa moze         |
|byc rzedu O(n + k)).                                                                     |
|                                                                                         |
|Zliczamy na plus każdą literę w kodzie ASCII w pierwszym wyrazie i na minus w drugim     |
|jeżeli Nasza tablica jest wyzerowana oznacza to że słowa są anagramami                   |
|                                                                                         |
|Złożoność czasowa :O(n)           Złożoność Pamięciowa O(2*16)                           |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -dwa wyrazy                            -True/False                                      |
|                                                                                         |
\=========================================================================================/
"""


def check_anagrams(word1, word2):
	if len(word1) != len(word2):
		return False

	counters =[0 for _ in range(2**16)]

	for i in range(len(word1)):
		counters[ord(word1[i])] = 0

	for i in range(len(word1)):
		counters[ord(word1[i])] += 1
		counters[ord(word2[i])] -= 1

	for i in range(len(word1)):
		if counters[ord(word1[i])] != 0:
			return False

	return True


#end
