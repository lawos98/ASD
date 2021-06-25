"""
/=========================================================================================\
|Scieżka w drzewie                                                                        |
|                                                                                         |
|Dane jest drzewo ukorzenione T, gdzie kazdy wierzchołek v ma potencjalnie ujemna         |
|wartosc value(v). Prosze zaproponowac algorytm, który znajduje                           |
|wartosc najbardziej wartosciowej sciezki w drzewie T.                                    |
|                                                                                         |
|Algorytm opiera się programowaniu dynamicznym a mianowicie funkcji która zwraca          |
|ścieżkę z największą sumą od i-tego wezła w całym jego pod_drzewie                       |
|następnie przechodzimy po kazdym wezle i wyliczamy najdłuższą sciezke w grafie           |
|pomiedzy trzema przypadkami albo najdłuzsza ścieżke do danego wezła,albo połaczenie      |
|prawej jak i lewej strony scieżkami lub żadna ścieżka czyli 0                            |
|                                                                                         |
|Złożoność czasowa :O(n) Złożoność Pamięciowa O(n)                                        |
|                                                                                         |
|Wejscie:                            Wyjście:                                             |
| -Drzewo                               -maksymalna suma ścieżki                          |
|                                                                                         |
\=========================================================================================/
"""

class Node:
	def __init__(self, value=None, left_side=None, right_side=None):
		self.left = left_side
		self.right = right_side
		self.path = None
		self.value = value

def path_in_tree(root):
	resualt=0
	def count(root):
		nonlocal resualt
		if root==None:return
		count(root.left)
		count(root.right)
		left_node=root.left
		right_node=root.right
		if left_node==None and right_node==None:
			root.path=root.value
			resualt=max(resualt,root.path)
		elif right_node==None:
			root.path=max(0,left_node.path)+root.value
			resualt=max(resualt,root.path)
		elif left_node==None:
			root.path=max(0,right_node.path)+root.value
			resualt=max(resualt,root.path)
		else:
			root.path=max(0,right_node.path,left_node.path)+root.value
			resualt=max(resualt,root.path,left_node.path+right_node.path+root.value)

	count(root)
	return resualt

#end
