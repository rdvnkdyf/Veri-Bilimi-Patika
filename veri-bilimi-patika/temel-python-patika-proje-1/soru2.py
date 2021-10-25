""" 
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""
def reverse_array(arr):
    arr.reverse()
    for i in range(0,len(arr)):
        arr[i].reverse()

    return arr
input_array=[[1, 2], [3, 4], [5, 6, 7]]


print("ouputput:--------",reverse_array(input_array))