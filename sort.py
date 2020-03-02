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
    
    def printNums(self):
        print("Alkuperäiset numerot:", self.array)
        print("Järjestetyt numerot:", self._sorted)