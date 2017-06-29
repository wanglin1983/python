#!/usr/bin/python

import sys
import random
import logger

# First Param : sort type
sortType = ''
if len(sys.argv) > 1:
    sortType = sys.argv[1]

# Init array
# array = [0, 6, 4, 3, 1, 2, 9, 5, 8, 7]
arrsize = 100 
array = []
i = 0
while i < arrsize:
    array.append(random.randint(0, arrsize))
    i = i + 1

def InsertSort(arr):
    logger.info('InsertSort')
    print arr
    arrLen = len(arr)
    index = 1
    while index < arrLen:
        insideIndex = index - 1
        key = arr[index]
        while insideIndex >= 0:
            value = arr[insideIndex]
            if value > key:
                arr[insideIndex + 1] = value
            else:
                break
            insideIndex = insideIndex - 1
        if insideIndex != index - 1:
            arr[insideIndex + 1] = key
        index = index + 1
    print arr

def BubbleSort(arr):
    logger.info('BubbleSort')
    print arr
    arrLen = len(arr)
    i = 0
    while i < arrLen:
        j = i + 1 
        while j < arrLen:
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
            j = j + 1
        i = i + 1
    print arr

if sortType == 'INSERT':
    InsertSort(array)
elif sortType == 'BUBBLE':
    BubbleSort(array)
else:
    InsertSort(array)
