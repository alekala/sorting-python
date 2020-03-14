# -*- coding: utf-8 -*-

'''
Erilaisia järjestämisalgoritmejä,
järjestää muodostimen `array` luokan
muuttujaan `_sorted`
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
        for index in range(len(_sorted)):
            leftIndex = index-1
            while leftIndex >= 0 and _sorted[leftIndex] > _sorted[leftIndex+1]:
                temp = _sorted[leftIndex]
                _sorted[leftIndex] = _sorted[leftIndex+1]
                _sorted[leftIndex+1] = temp
                leftIndex -= 1
        self._sorted = _sorted
        return _sorted
    
    '''
    Järjestää listan `array` O(n log n)
    tehokkuudella lomitusjärjestämisellä
    '''
    def mergeSort(self):
        _sorted = self._sorted

        '''
        Jakaa listan `inputList`
        osiksi kunnes listoissa yksi alkio
        '''
        def __split(inputList):
            listLength = len(inputList)
            middlePoint = listLength // 2
            return inputList[:middlePoint], inputList[middlePoint:]

        '''
        Kasaa sekä järjestää
        listat `leftList` ja `rightList`,
        palauttaa listat yhdistettynä
        '''
        def __merge(leftList, rightList):
            if len(leftList) == 0:
                return leftList
            elif len(rightList) == 0:
                return rightList
        
            leftIndex = 0
            rightIndex = 0
            _merged = []
            targetLength = len(leftList) + len(rightList)

            while len(_merged) < targetLength:
                if leftList[leftIndex] <= rightList[rightIndex]:
                    _merged.append(leftList[leftIndex])
                    leftIndex += 1
                else:
                    _merged.append(rightList[rightIndex])
                    rightIndex += 1

                if rightIndex == len(rightList):
                    _merged += leftList[leftIndex:]
                    break
                elif leftIndex == len(leftList):
                    _merged += rightList[rightIndex:]
                    break
            return _merged

        '''
        Kutsuu funktioita `split`
        ja `merge`, kunnes lista `_sorted`
        on järjestetty
        '''
        def __sort(inputList):
            if len(inputList) <= 1:
                return inputList
            left, right = __split(inputList)
            return __merge(__sort(left), __sort(right))
        
        _sorted = __sort(self._sorted)
        self._sorted = _sorted
        return _sorted
    
    '''
    Järjestää listan `array`
    parhaassa tapauksessa tehokkuudella
    O(n log n) ja huonoimmassa tapauksessa
    tehokkuudella O(n^2)
    '''
    def quickSort(self):
        _sorted = self._sorted

        '''
        Jakaa listan `inputList` pienempiin
        osiin ja järjestää listan siirtämällä
        osan pivotin oikealle puolelle
        '''
        def __partition(inputList, start, end):
            pivot = inputList[start]
            low = start + 1
            high = end

            while True:
                while low <= high and inputList[high] >= pivot:
                    high -= 1
                
                while low <= high and inputList[low] <= pivot:
                    low += 1
                
                if low <= high:
                    inputList[low], inputList[high] = inputList[high], inputList[low]
                else:
                    break
            
            inputList[start], inputList[high] = inputList[high], inputList[start]
            return high
        
        def __sort(inputList, start, end):
            if start >= end:
                return
            part = __partition(inputList, start, end)
            __sort(inputList, start, part-1)
            __sort(inputList, part+1, end)
        
        __sort(_sorted, 0, len(_sorted)-1)
        self._sorted = _sorted
        return _sorted

    def printNums(self):
        print("Alkuperäiset numerot:", self.array)
        print("Järjestetyt numerot:", self._sorted)