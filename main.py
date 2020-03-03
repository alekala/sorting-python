# -*- coding: utf-8 -*-

from random import randint
from sort import Sort

'''
Generoi listan, jossa on `count`
määrä numeroita 0-9 välillä
'''
def genNums(count):
    numbers = []
    for i in range(count):
        numbers.append(randint(0, 9))
    return numbers

sorter = Sort(genNums(10))
# sortedArray = sorter.insertionSort()
sortedArray = sorter.mergeSort()
sorter.printNums()