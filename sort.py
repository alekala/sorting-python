# -*- coding: utf-8 -*-

'''
Erilaisia järjestämisalgoritmejä,
järjestää muodostimen `array`
'''
class Sort:
    def __init__(self, array):
        self.array = array
        # Luo uusi lista, jotta saadaan
        # uusi objekti eikä osoittaja
        self._sorted = list(self.array)

    '''
    Järjestää listan `array` O(n^2)
    tehokkuudella lisäysjärjestämisellä
    '''
    def insertionSort(self):
        _sorted = self._sorted
        for i in range(len(_sorted)):
            j = i-1
            while j >= 0 and _sorted[j] > _sorted[j+1]:
                temp = _sorted[j]
                _sorted[j] = _sorted[j+1]
                _sorted[j+1] = temp
                j -= 1
        self._sorted = _sorted
        return _sorted
    
    '''
    Järjestää listan `array` O(n log n)
    tehokkuudella lomitusjärjestämisellä
    '''
    def mergeSort(self):
        _sorted = self._sorted
        # Luodaan lista, jossa `_sorted`
        # määrä None elementtejä, jotta voidaan
        # käyttää listaa kuin tavallisessa ohjelmoinnissa
        temp = [None] * len(self._sorted)

        def merge(a1, b1, a2, b2):
            a, b = a1, b2
            for i in range(a, b):
                if (a2 > b2) or (a1 <= b1 and _sorted[a1] <= _sorted[a2]):
                    temp[i] = _sorted[a1]
                    a1 += 1
                else:
                    temp[i] = _sorted[a2]
                    a2 += 1
            for i in range(a, b):
                _sorted[i] = temp[i]

        def sort(leftIndex, rightIndex):
            if leftIndex == rightIndex:
                return
            x = (leftIndex+rightIndex)//2
            sort(leftIndex, x)
            sort(x+1, rightIndex)
            merge(leftIndex, x, x+1, rightIndex)
        
        sort(0, len(_sorted)-1)
        return _sorted
    
    def printNums(self):
        print("Alkuperäiset numerot:", self.array)
        print("Järjestetyt numerot:", self._sorted)